#!/usr/bin/python3
"""
unittest for max_integer function
"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """test cases for max_integer"""

    def test_ModuleDoc(self):
        """check the module's doc style"""
        doc = __import__("6-max_integer").__doc__
        self.assertTrue(len(doc) > 1)

    def test_FunctionDoc(self):
        """check the function's doc style"""
        doc = max_integer.__doc__
        self.assertTrue(len(doc) > 1)

    def test_MaxAtBeginning(self):
        """max at the beginning of the list case"""
        self.assertEqual(100, max_integer([100, 5, 4]))

    def test_MaxAtMid(self):
        """max at the middle of the list case"""
        self.assertEqual(45, max_integer([10, 5, 45, 44, 4]))

    def test_MaxAtEnd(self):
        """max at the end of the list case"""
        self.assertEqual(544, max_integer([10, 5, 45, 44, 4, 544]))

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
        with self.assertRaises(TypeError):
            max_integer([13, "h", 44, "C"])


if __name__ == "__main__":
    unittest.main()
