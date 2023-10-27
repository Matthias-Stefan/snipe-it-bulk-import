__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller import IController
from src.execution import UploadExecutor
from src.model import Asset, Upload
from src.view.tabs import UploadTab

import threading

from pathlib import Path


class UploadController(IController):
    """Initialize an instance of the UploadController class.

    This class manages the uploading of data from a CSV file to a system. It uses an UploadExecutor to perform the
    upload in a separate thread.

    :param parent: The parent controller or component.
    :type parent: src.controller.IController
    """
    def __init__(self, parent=None):
        super(UploadController, self).__init__(parent)

        self._model = Upload()
        self._view = UploadTab(controller=self, model=self._model)

    def post_init(self):
        """Perform any post-initialization tasks, if necessary.

        :rtype: None
        """
        return

    def execute(self, **kwargs):
        """Execute the data upload process.

        This method starts the upload process in a separate thread, allowing the main application to remain responsive.

        :param kwargs: Additional keyword arguments for execution.
        :type kwargs: dict
        :rtype: None
        """
        def _execute():
            self.progress_reset()
            self.progress_advance(0, "Start uploading")
            UploadExecutor.process_csv(self._model.filepath)
            self.progress_advance(100, "Task finished", timeout=1)

        thread: threading.Thread = threading.Thread(target=_execute)
        thread.daemon = True
        thread.start()

    @property
    def view(self):
        """Get the associated view for this controller.

        :rtype: src.view.tabs.upload_tab.UploadTab
        """
        return self._view

    @property
    def model(self):
        """Get the associated model for this controller.

        :rtype: src.model.upload.Upload
        """
        return self._model

    @property
    def filepath(self):
        """The filepath of the CSV file to be uploaded.

        :rtype: str
        """
        return self._model.filepath

    @filepath.setter
    def filepath(self, value):
        path = Path(value)
        if path.is_file() and path.suffix == ".csv":
            self._model.filepath = value
