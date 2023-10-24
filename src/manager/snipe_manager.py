__author__ = "Matthias Stefan"
__version__ = "0.1.0"

import sys
import time

from src.utility import Singleton, TooManyRequestsError, profile_function

import requests

from typing import Callable
from queue import Queue


class Endpoint:
    def __init__(self):
        self.value: str = ""
        self.callback: Callable = None
        self.payload: dict = {}

    def get_params(self):
        return self.value, self.payload


class Work:
    def __init__(self, endpoint: Endpoint):
        self.is_valid = True
        self.endpoint = endpoint


class EndpointQueue(Queue):
    def __init__(self):
        super().__init__()

    def add_work(self, endpoint: Endpoint):
        if endpoint is None or endpoint.callback is None:
            raise Exception(f"Endpoint is not valid: {endpoint}")
        self.put(Work(endpoint))


@Singleton
class SnipeManager:
    def __init__(self):
        self._url = None
        self._token = None
        self._header = None

    @staticmethod
    def http_validation(callback: Callable):
        def wrapper(*args, **kwargs):
            response = callback(*args, **kwargs)

            if response.status_code == 429:
                raise TooManyRequestsError("too many requests")

            if not 200 <= response.status_code <= 300:
                raise Exception(response.status_code, response.text)

            response_ = response.json()
            if 'status' in response_ and \
                    response_['status'] == 'error':
                raise Exception(response.text)
                # TODO: Logger
            return response
        return wrapper

    def post_init(self, url, token):
        self._url = url
        self._token = token
        self._header = {"Authorization": f"Bearer {self._token}",
                        "Accept": "application/json",
                        "Content-Type": "application/json"}
        get_endpoint = Endpoint()
        get_endpoint.value = '/users/me'
        get_endpoint.callback = self.get
        try:
            self.execute_now(get_endpoint)
        except Exception as e:
            print(e)
            # TODO: Logging
            sys.exit(1)

    @staticmethod
    def execute_now(endpoint: Endpoint):
        if endpoint is None or endpoint.callback is None:
            raise Exception(f"Endpoint is not valid: {endpoint}")
        work = Work(endpoint)
        while work.is_valid:
            try:
                response = work.endpoint.callback(*work.endpoint.get_params())
                work.is_valid = False
                return response
            except TooManyRequestsError:
                time.sleep(1)

    @http_validation
    def get(self, endpoint_url, payload):
        if not self._url or not self._header:
            return None
        response = requests.get(url=self._url+endpoint_url, json=payload, headers=self._header, verify=False)
        return response

    @http_validation
    def post(self, endpoint_url, payload):
        if not self._url or not self._header:
            return None
        response = requests.post(url=self._url+endpoint_url, json=payload, headers=self._header, verify=False)
        return response

    @http_validation
    def put(self, endpoint_url, payload):
        if not self._url or not self._header:
            return None
        response = requests.put(url=self._url+endpoint_url, json=payload, headers=self._header, verify=False)
        return response

    @http_validation
    def patch(self, endpoint_url, payload):
        if not self._url or not self._header:
            return None
        response = requests.patch(url=self._url+endpoint_url, json=payload, headers=self._header, verify=False)
        return response

    @profile_function
    def request_all_sit_models(self):
        offset = 0
        while True:
            get_endpoint = Endpoint()
            get_endpoint.value = '/models'
            get_endpoint.callback = self.get
            get_endpoint.payload = {'limit': 0, 'offset': offset}
            response = self.execute_now(get_endpoint).json()
            yield response['rows'], response['total']
            offset += 500
            if offset < response['total']:
                continue
            break

    @profile_function
    def request_all_status_labels(self):
        offset = 0
        while True:
            get_endpoint = Endpoint()
            get_endpoint.value = '/statuslabels'
            get_endpoint.callback = self.get
            get_endpoint.payload = {'limit': 0, 'offset': offset}
            response = self.execute_now(get_endpoint).json()
            yield response['rows'], response['total']
            offset += 500
            if offset < response['total']:
                continue
            break
