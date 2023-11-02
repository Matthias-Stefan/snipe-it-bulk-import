__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import UploadController, MainController
from src.execution import UploadExecutor

from unittest import TestCase
from unittest.mock import patch, mock_open


def basic_app():
    from kivymd.app import MDApp

    class TestApp(MDApp):
        def __init__(self, **kwargs):
            super(TestApp, self).__init__(**kwargs)
            self.main_controller = MainController()
            self.controller = UploadController(self.main_controller)
    return TestApp()


class TestUploadController(TestCase):
    @patch("threading.Thread")
    def test_execute_thread_start(self, thread_exe):
        test_app = basic_app()
        test_app.controller.execute()
        thread_exe.assert_called()

    @patch("src.execution.upload_executor.UploadExecutor.process_csv")
    def test_execute_progress_updates(self, process_csv_call):
        test_app = basic_app()
        with patch.object(test_app.controller, 'progress_advance') as progress_advance_mock:
            test_app.controller.execute()()
            process_csv_call.assert_called()
            progress_advance_mock.assert_any_call(0, "Start uploading")
            progress_advance_mock.assert_any_call(100, "Task finished", timeout=1)


class TestUploadExecutor(TestCase):
    def test_dispatch_model_upload(self):
        test_file = r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\tests\app\test_data\test_create_asset.csv"
        with patch("src.execution.model_upload_executor.ModelUploadExecutor.process_row") as process_row_call:
            upload_executor = UploadExecutor()
            upload_executor.process_csv(test_file)
            expected_call = {
                'id': '',
                'name': 'Eizo 24 Zoll 16:9',
                'asset_tag': '',
                'model_id': '42',
                'serial': 'YrhEQgijqm',
                'purchase_date': '01.11.2023',
                'purchase_cost': '299.99',
                'order_number': '8081',
                'assigned_to': '',
                'notes': '',
                'image': '',
                'user_id': '',
                'created_at': '',
                'updated_at': '',
                'physical': '',
                'deleted_at': '',
                'status_id': '1',
                'archived': '',
                'warranty_months': '',
                'depreciate': '',
                'supplier_id': '',
                'requestable': '',
                'rtd_location_id': '',
                'accepted': '',
                'last_checkout': '',
                'expected_checkout': '',
                'company_id': '',
                'assigned_type': '',
                'last_audit_date': '',
                'next_audit_date': '',
                'location_id': '',
                'checkin_counter': '',
                'checkout_counter': '',
                'requests_counter': '',
                'model_number': '',
                'alt_barcode': '',
                'user_can_checkout': '',
                'category': '',
                'manufacturer': '',
                '_snipeit_screen_type_36': 'Full HD Screen',
                '_snipeit_type_of_usage_20': '',
                '_snipeit_room_27': '',
                '_snipeit_fixed_asset_number_3': ''
            }
            process_row_call.assert_any_call(expected_call)

    def test_dispatch_model_upload_with_wrong_executor(self):
        test_file = r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\tests\app\test_data\test_create_asset.csv"
        with patch("src.execution.checkout_upload_executor.CheckoutUploadExecutor.process_row") :
            upload_executor = UploadExecutor()

            with self.assertRaises(AttributeError):
                upload_executor.process_csv(test_file)

    def test_dispatch_checkout_upload(self):
        test_file = r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\tests\app\test_data\test_checkout.csv"
        with patch("src.execution.checkout_upload_executor.CheckoutUploadExecutor.process_row") as process_row_call:
            upload_executor = UploadExecutor()
            upload_executor.process_csv(test_file)
            expected_call = {
                'asset_tag': '15133',
                'checkout_to_{user/asset/location}': 'asset',
                'checkout_id': '15132',
                'status_id': '1',
            }
            process_row_call.assert_any_call(expected_call)

    def test_dispatch_checkout_upload_with_wrong_executor(self):
        test_file = r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\tests\app\test_data\test_checkout.csv"
        with patch("src.execution.model_upload_executor.ModelUploadExecutor.process_row") :
            upload_executor = UploadExecutor()

            with self.assertRaises(AttributeError):
                upload_executor.process_csv(test_file)

