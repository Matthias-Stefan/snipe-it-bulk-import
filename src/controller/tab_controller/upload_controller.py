__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller import IController
from src.model import Asset, Upload
from src.manager import SnipeManager, Endpoint
from src.view.tabs import UploadTab

import csv
import threading

from pathlib import Path


class UploadController(IController):
    def __init__(self, parent=None):
        super(UploadController, self).__init__(parent)

        self._model = Upload()
        self._view = UploadTab(controller=self, model=self._model)

    def post_init(self):
        return

    def execute(self, **kwargs):
        def _execute():
            self.progress_reset()
            self.progress_advance(0, "Start uploading")
            with open(self._model.filepath, newline='', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file, delimiter=';')
                snipe_manager: SnipeManager = SnipeManager()
                if 'model_id' in reader.fieldnames:
                    for row in reader:
                        asset = Asset.from_csv(row)
                        endpoint = Endpoint()
                        endpoint.callback = snipe_manager.post
                        endpoint.value = '/hardware'
                        endpoint.payload = asset.get(validate_not_none=True)
                        snipe_manager.execute_now(endpoint)
                    self.progress_advance(100, "Uploaded successfully")
                elif 'checkout_id' in reader.fieldnames:
                    for row in reader:
                        # NOTE: get asset_id from asset_tag
                        endpoint = Endpoint()
                        endpoint.callback = snipe_manager.get
                        if row['asset_tag'] is None:
                            continue
                        endpoint.value = f"/hardware/bytag/{row['asset_tag']}"
                        asset = snipe_manager.execute_now(endpoint).json()

                        # NOTE: checkin asset
                        if 'assigned_to' in asset and asset['assigned_to'] is not None:
                            endpoint = Endpoint()
                            endpoint.callback = snipe_manager.post
                            endpoint.value = f"/hardware/{asset['id']}/checkin"
                            endpoint.payload = {'status_id': asset['status_label']['id']}
                            snipe_manager.execute_now(endpoint).json()

                        # NOTE: checkout
                        if row['checkout_to_{user/asset/location}'] == 'user':
                            # NOTE: get target
                            endpoint = Endpoint()
                            endpoint.callback = snipe_manager.get
                            endpoint.value = f"/users/{row['checkout_id']}"
                            target = snipe_manager.execute_now(endpoint).json()

                            # Note: checkout
                            endpoint = Endpoint()
                            endpoint.callback = snipe_manager.post
                            endpoint.value = f"/hardware/{asset['id']}/checkout"
                            endpoint.payload = {"checkout_to_type": "user",
                                                "assigned_user": target['id']}
                            snipe_manager.execute_now(endpoint)

                        elif row['checkout_to_{user/asset/location}'] == 'location':
                            # NOTE: get target
                            endpoint = Endpoint()
                            endpoint.callback = snipe_manager.get
                            endpoint.value = f"/locations/{row['checkout_id']}"
                            target = snipe_manager.execute_now(endpoint).json()

                            # Note: checkout
                            endpoint = Endpoint()
                            endpoint.callback = snipe_manager.post
                            endpoint.value = f"/hardware/{asset['id']}/checkout"
                            endpoint.payload = {"checkout_to_type": "location",
                                                "assigned_location": target['id']}
                            snipe_manager.execute_now(endpoint)

                        elif row['checkout_to_{user/asset/location}'] == 'asset':
                            # NOTE: get target
                            endpoint = Endpoint()
                            endpoint.callback = snipe_manager.get
                            if row['asset_tag'] is None:
                                continue
                            endpoint.value = f"/hardware/bytag/{row['checkout_id']}"
                            target = snipe_manager.execute_now(endpoint).json()

                            # Note: checkout
                            endpoint = Endpoint()
                            endpoint.callback = snipe_manager.post
                            endpoint.value = f"/hardware/{asset['id']}/checkout"
                            endpoint.payload = {"checkout_to_type": "asset",
                                                "assigned_asset": target['id']}
                            snipe_manager.execute_now(endpoint)

        thread: threading.Thread = threading.Thread(target=_execute)
        thread.daemon = True
        thread.start()

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model

    @property
    def filepath(self):
        return self._model.filepath

    @filepath.setter
    def filepath(self, value):
        path = Path(value)
        if path.is_file() and path.suffix == ".csv":
            self._model.filepath = value
