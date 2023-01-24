import unittest

from main import QRCodeGenerator

import os

class TestQRCodeGenerator(unittest.TestCase):
    def test_create(self):
        # Test create method with a text
        qr = QRCodeGenerator("https://www.example.com", "qr_code.png")
        qr.create()
        self.assertTrue(os.path.exists("qr_code.png"))
        os.remove("qr_code.png") # delete file after test

    def test_from_text(self):
        # Test from_text method
        qr = QRCodeGenerator.from_text("https://www.example.com", "qr_code.png")
        self.assertEqual(qr.data, "https://www.example.com")
        self.assertEqual(qr.file_name, "qr_code.png")

if __name__ == '__main__':
    unittest.main()
