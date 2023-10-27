__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.execution import IExecution
from src.model import Asset
from src.manager import Endpoint


class ModelUploadExecutor(IExecution):
    def process_row(self, row):
        """
        Process a single row of data.

        This method processes a row of data to upload a new asset model to the Snipe-IT system.

        :param row: A row of data representing an asset model.
        :type row: dict
        """
        asset = Asset.from_csv(row)
        endpoint = Endpoint()
        endpoint.callback = self._snipe_manager.post
        endpoint.value = '/hardware'
        endpoint.payload = asset.get(validate_not_none=True)
        self._snipe_manager.execute_now(endpoint)
