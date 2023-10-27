__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.execution import IExecution
from src.manager import Endpoint


class CheckoutUploadExecutor(IExecution):

    def process_row(self, row):
        """
        Process a single row of data for checking out and uploading assets.

        :param row: A row of data containing information about the asset checkout.
        :type row: dict
        :return: None
        """
        # 1) get asset_id from asset_tag
        endpoint = Endpoint()
        endpoint.callback = self._snipe_manager.get
        if row['asset_tag'] is None:
            return
        endpoint.value = f"/hardware/bytag/{row['asset_tag']}"
        asset = self._snipe_manager.execute_now(endpoint).json()

        # 2) checkin asset
        if 'assigned_to' in asset and asset['assigned_to'] is not None:
            endpoint = Endpoint()
            endpoint.callback = self._snipe_manager.post
            endpoint.value = f"/hardware/{asset['id']}/checkin"
            endpoint.payload = {'status_id': asset['status_label']['id']}
            self._snipe_manager.execute_now(endpoint).json()

        # 3) checkout
        if row['checkout_to_{user/asset/location}'] == 'user':
            # 3.1.1) get target
            endpoint = Endpoint()
            endpoint.callback = self._snipe_manager.get
            endpoint.value = f"/users/{row['checkout_id']}"
            target = self._snipe_manager.execute_now(endpoint).json()

            # 3.1.2) checkout
            endpoint = Endpoint()
            endpoint.callback = self._snipe_manager.post
            endpoint.value = f"/hardware/{asset['id']}/checkout"
            endpoint.payload = {"checkout_to_type": "user",
                                "assigned_user": target['id']}
            self._snipe_manager.execute_now(endpoint)

        elif row['checkout_to_{user/asset/location}'] == 'location':
            # 3.2.1) get target
            endpoint = Endpoint()
            endpoint.callback = self._snipe_manager.get
            endpoint.value = f"/locations/{row['checkout_id']}"
            target = self._snipe_manager.execute_now(endpoint).json()

            # 3.2.2) checkout
            endpoint = Endpoint()
            endpoint.callback = self._snipe_manager.post
            endpoint.value = f"/hardware/{asset['id']}/checkout"
            endpoint.payload = {"checkout_to_type": "location",
                                "assigned_location": target['id']}
            self._snipe_manager.execute_now(endpoint)

        elif row['checkout_to_{user/asset/location}'] == 'asset':
            # 3.3.1) get target
            endpoint = Endpoint()
            endpoint.callback = self._snipe_manager.get
            if row['asset_tag'] is None:
                return
            endpoint.value = f"/hardware/bytag/{row['checkout_id']}"
            target = self._snipe_manager.execute_now(endpoint).json()

            # 3.3.2) checkout
            endpoint = Endpoint()
            endpoint.callback = self._snipe_manager.post
            endpoint.value = f"/hardware/{asset['id']}/checkout"
            endpoint.payload = {"checkout_to_type": "asset",
                                "assigned_asset": target['id']}
            self._snipe_manager.execute_now(endpoint)

