import unittest
from humble import *

class HumbleTests(unittest.TestCase):
	#export
	def test_hello(self):
	    self.assertNotEquals("hella",hello())
	    self.assertEquals("hello",hello())

if __name__ == "__main__":
    unittest.main()
