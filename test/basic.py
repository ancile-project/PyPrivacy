import unittest
from pyprivacy.decorators import *
from pyprivacy.primitives import *

@TransformDecorator()
def test(data):
    return 5

class MyTestCase(unittest.TestCase):
    def test_something(self):
        dpp = DataPolicyPair('ANYF*')
        dpp._data = 8
        res = test(data=dpp)
        self.assertEqual(res._data, 5)


if __name__ == '__main__':
    unittest.main()
