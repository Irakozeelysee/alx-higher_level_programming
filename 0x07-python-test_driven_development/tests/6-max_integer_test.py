#!usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer

"""unittest for max_integer function
"""


class TestMaxInteger(unittest.TestCase):
    """test cases for max_integer"""

    def test_ModuleDoc(self):
        """check the module's doc style"""
        self.assertTrue(__import__("6-max_integer").__doc__)

    def test_FunctionDoc(self):
        """check the function's doc style"""
        self.assertTrue(__import__("6-max_integer").max_integer.__doc__)

    def test_emptyList(self):
        """empty list case"""
        self.assertEqual(None, max_integer([]))

    def test_oneElementInList(self):
        """one element in the list case"""
        self.assertEqual(13, max_integer([13]))

    def test_argNotList(self):
        """arg not a list"""
        self.assertRaises(TypeError, max_integer("not a list"))

    def test_NoArg(self):
        """no argument"""
        self.assertRaises(TypeError, max_integer())

    def test_listMixedNoInt(self):
        """list elements not all int"""
        self.assertRaises(TypeError, max_integer([13, "h", 44, "C"]))


if __name__ == "__main__":
    unittest.main()
