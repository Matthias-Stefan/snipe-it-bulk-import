__author__ = "Matthias Stefan"
__version__ = "1.0.0"

import sys

from src.manager import Endpoint
from src.manager.logger import Logger
from src.utility import Singleton, TooManyRequestsError, profile_function

import requests

from functools import wraps
from typing import Callable


@Singleton
class SnipeManager:
    """Initialize an instance of the SnipeManager class.

    The SnipeManager class is a singleton responsible for managing connections to the Snipe-IT API.

    :rtype: None
    """
    def __init__(self):
        self._url = None
        self._token = None
        self._header = None

    @staticmethod
    def http_validation(callback: Callable):
        """A decorator for validating HTTP responses.

        This decorator validates HTTP responses and handles exceptions for status code and error responses.

        :rtype: typing.Callable
        """
        @Logger.log_function
        @wraps(callback)
        def wrapper(*args, **kwargs):
            response = callback(*args, **kwargs)

            if response.status_code == 429:
                Logger.error("HTTP Validation: Too many requests")
                raise TooManyRequestsError("too many requests")

            if not 200 <= response.status_code <= 300:
                Logger.error(f"HTTP Validation: Status code {response.status_code}, Response: {response.text}")
                raise Exception(response.status_code, response.text)

            response_ = response.json()
            if 'status' in response_ and \
                    response_['status'] == 'error':
                Logger.error(f"HTTP Validation: Error response - {response.text}")
                raise Exception(response.text)
            return response
        return wrapper

    def post_init(self, url, token):
        """Initialize Snipe-IT API connection parameters.

        This method initializes the URL and token for connecting to the Snipe-IT API.

        :type url: str
        :param url: The URL of the Snipe-IT API.

        :type token: str
        :param token: The API token for authentication.

        :rtype: None
        """
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
        except Exception:
            Logger.error("Unable to connect to the Snipe-IT instance.")
            sys.exit(1)

    @staticmethod
    def execute_now(endpoint: Endpoint):
        """Execute an HTTP endpoint request.

        This method executes an HTTP endpoint request and handles the TooManyRequestsError.

        :type endpoint: Endpoint
        :param endpoint: An instance of the Endpoint class.

        :rtype: None
        """
        if endpoint is None or endpoint.callback is None:
            raise Exception(f"Endpoint is not valid: {endpoint}")
        try:
            response = endpoint.callback(*endpoint.get_params())
            return response
        except TooManyRequestsError:
            Logger.warning("Snipe-IT has encountered a high volume of requests and responded with an error.")

    @http_validation
    def get(self, endpoint_url, payload):
        """Make an HTTP GET request.

        This method sends an HTTP GET request to the specified endpoint URL.

        :type endpoint_url: str
        :param endpoint_url: The URL for the GET request.

        :type payload: dict
        :param payload: The payload for the GET request.

        :rtype: requests.Response
        :return: The HTTP response object.
        """
        if not self._url or not self._header:
            Logger.warning(f"Incomplete configuration: URL: {self._url}, header: {self._header}")
            return None
        response = requests.get(url=self._url+endpoint_url, json=payload, headers=self._header, verify=False)
        return response

    @http_validation
    def post(self, endpoint_url, payload):
        """Make an HTTP POST request.

        This method sends an HTTP POST request to the specified endpoint URL.

        :type endpoint_url: str
        :param endpoint_url: The URL for the POST request.

        :type payload: dict
        :param payload: The payload for the POST request.

        :rtype: requests.Response
        :return: The HTTP response object.
        """
        if not self._url or not self._header:
            Logger.warning(f"Incomplete configuration: URL: {self._url}, header: {self._header}")
            return None
        Logger.info(f'HTTP POST Payload: {payload}')
        response = requests.post(url=self._url+endpoint_url, json=payload, headers=self._header, verify=False)
        return response

    @http_validation
    def put(self, endpoint_url, payload):
        """Make an HTTP PUT request.

        This method sends an HTTP PUT request to the specified endpoint URL.

        :type endpoint_url: str
        :param endpoint_url: The URL for the PUT request.

        :type payload: dict
        :param payload: The payload for the PUT request.

        :rtype: requests.Response
        :return: The HTTP response object.
        """
        if not self._url or not self._header:
            Logger.warning(f"Incomplete configuration: URL: {self._url}, header: {self._header}")
            return None
        response = requests.put(url=self._url+endpoint_url, json=payload, headers=self._header, verify=False)
        return response

    @http_validation
    def patch(self, endpoint_url, payload):
        """Make an HTTP PATCH request.

        This method sends an HTTP PATCH request to the specified endpoint URL.

        :type endpoint_url: str
        :param endpoint_url: The URL for the PATCH request.

        :type payload: dict
        :param payload: The payload for the PATCH request.

        :rtype: requests.Response
        :return: The HTTP response object.
        """
        if not self._url or not self._header:
            Logger.warning(f"Incomplete configuration: URL: {self._url}, header: {self._header}")
            return None
        response = requests.patch(url=self._url+endpoint_url, json=payload, headers=self._header, verify=False)
        return response

    @profile_function
    def request_all_sit_models(self):
        """Request all SIT models from Snipe-IT.

        This method sends HTTP requests to retrieve all models from the Snipe-IT API.

        :rtype: Generator
        :return: A generator yielding response rows and total count.
        """
        offset = 0
        limit = 500
        while True:
            get_endpoint = Endpoint()
            get_endpoint.value = '/models'
            get_endpoint.callback = self.get
            get_endpoint.payload = {'limit': limit, 'offset': offset}
            response = self.execute_now(get_endpoint).json()
            yield response['rows'], response['total']
            offset += limit
            if offset < response['total']:
                continue
            break

    @profile_function
    def request_all_status_labels(self):
        """Request all status labels from Snipe-IT.

        This method sends HTTP requests to retrieve all status labels from the Snipe-IT API.

        :rtype: Generator
        :return: A generator yielding response rows and total count.
        """
        offset = 0
        limit = 500
        while True:
            get_endpoint = Endpoint()
            get_endpoint.value = '/statuslabels'
            get_endpoint.callback = self.get
            get_endpoint.payload = {'limit': limit, 'offset': offset}
            response = self.execute_now(get_endpoint).json()
            yield response['rows'], response['total']
            offset += limit
            if offset < response['total']:
                continue
            break
