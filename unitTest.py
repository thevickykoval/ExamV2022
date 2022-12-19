import unittest
import piram as app

class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app
    
    def test_piram(self):
        self.assertEqual(app.piram(1), 1)
        self.assertEqual(app.piram(2), 3)
        self.assertEqual(app.piram(3), 6)

if __name__ == '__main__':
    unittest.main()