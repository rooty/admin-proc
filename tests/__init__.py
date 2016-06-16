import unittest

import config
from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config.TEST_DATABASE_URI)
        self.client = self.app.test_client()
