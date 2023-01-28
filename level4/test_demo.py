import unittest

class Mytestcase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(true,true)
    def test_add(self):
            self.asertEqual(30,20+10)
if __name__=='__main__':
    unittest.main()
