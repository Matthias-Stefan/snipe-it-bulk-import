__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.manager import SnipeManager, Endpoint

from unittest import TestCase
from unittest.mock import patch, MagicMock


def basic_app():
    from kivymd.app import MDApp

    class TestApp(MDApp):
        def __init__(self, **kwargs):
            super(TestApp, self).__init__(**kwargs)
            self.manager = SnipeManager()
    return TestApp()


class TestSnipeManager(TestCase):
    def test_singleton(self):
        test_app = basic_app()
        manager = SnipeManager()
        self.assertEqual(id(test_app.manager), id(manager))

    def test_post_init(self):
        test_app = basic_app()
        with self.assertRaises(SystemExit):
            test_app.manager.post_init(None, None)

    def test_execute_now_with_exception(self):
        test_app = basic_app()
        with self.assertRaises(Exception):
            test_app.manager.execute_now(None)
        with self.assertRaises(Exception):
            test_app.manager.execute_now(Endpoint())

    def test_execute_now_with_success(self):
        test_app = basic_app()
        dummy_endpoint = MagicMock()
        dummy_response = "Test"

        with patch.object(dummy_endpoint, 'callback', return_value=dummy_response):
            response = test_app.manager.execute_now(dummy_endpoint)
        self.assertEqual(response, dummy_response)
