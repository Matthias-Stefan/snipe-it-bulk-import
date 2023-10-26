__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import IController
from src.model import Upload
from src.template import ITemplate, CreateCheckoutTemplate
from src.view.tabs import CheckoutTab

import subprocess
import threading


class CheckoutController(IController):
    def __init__(self, parent=None):
        super(CheckoutController, self).__init__(parent)
        self._model = Upload()
        self._view = CheckoutTab(controller=self, model=self._model)

    def post_init(self):
        return

    def execute(self, **kwargs):
        def _execute():
            self.progress_reset()
            self.progress_advance(0, "Start creating csv")
            self.progress_advance(10, "Prepare Template", timeout=1)
            create_checkout_template: ITemplate = CreateCheckoutTemplate(
                filepath=self.filepath
            )
            file = create_checkout_template.create()
            self.progress_advance(20, "Open Excel", timeout=1)
            if self.autostart:
                from src.controller import MainController
                if isinstance(self.parent, MainController):
                    excel_path = self.parent.get_settings_controller().excel_path
                    if self.auto_upload:
                        self.progress_advance(30, "Wait for Excel to close", timeout=1)
                        subprocess.call([excel_path, file])
                        upload_controller = self.parent.get_upload_controller()
                        upload_controller.filepath = str(file)
                        upload_controller.execute()
                    else:
                        subprocess.Popen([excel_path, file])
            self.progress_advance(100, "Task finished", timeout=1)

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
        """Filepath of the CSV to be uploaded.

        :type: pathlib.Path
        """
        return self.model.filepath

    @filepath.setter
    def filepath(self, value):
        self.model.filepath = value

    @property
    def autostart(self):
        """Determine if Excel should be automatically invoked.

        :type: bool
        """
        return self.model.autostart

    @autostart.setter
    def autostart(self, value):
        self.model.autostart = value

    @property
    def auto_upload(self):
        """Determine if CSV should be automatically uploaded.

        :type: bool
        """
        return self.model.auto_upload

    @auto_upload.setter
    def auto_upload(self, value):
        self.model.auto_upload = value
