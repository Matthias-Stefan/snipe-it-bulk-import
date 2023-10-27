__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import IController
from src.model import Upload
from src.template import ITemplate, CreateCheckoutTemplate
from src.view.tabs import CheckoutTab

import subprocess
import threading


class CheckoutController(IController):
    """
    Initialize an instance of the CheckoutController class.

    This class controls the checkout process, including generating a CSV file based on a template and opening it in
    Excel.

    :param parent: The parent controller or component.
    :type parent: src.controller.IController
    """
    def __init__(self, parent=None):
        super(CheckoutController, self).__init__(parent)
        self._model = Upload()
        self._view = CheckoutTab(controller=self, model=self._model)

    def post_init(self):
        return

    def execute(self, **kwargs):
        """
        Execute the checkout process.

        This method starts the checkout process by preparing a CSV template, opening it in Excel, and optionally
        uploading it.

        :param kwargs: Additional keyword arguments.
        """
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
        """Get the associated view for this controller.

        :rtype: src.view.tabs.checkout_tab.CheckoutTab
        """
        return self._view

    @property
    def model(self):
        """Get the model associated with this controller.

        :rtype: src.model.checkout.Checkout
        """
        return self._model

    @property
    def filepath(self):
        """The filepath of the CSV to be uploaded.

        :type: pathlib.Path
        """
        return self.model.filepath

    @filepath.setter
    def filepath(self, value):
        self.model.filepath = value

    @property
    def autostart(self):
        """Whether Excel should be automatically invoked.

        :type: bool
        """
        return self.model.autostart

    @autostart.setter
    def autostart(self, value):
        self.model.autostart = value

    @property
    def auto_upload(self):
        """Whether the CSV should be automatically uploaded.

        :type: bool
        """
        return self.model.auto_upload

    @auto_upload.setter
    def auto_upload(self, value):
        self.model.auto_upload = value
