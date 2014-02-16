import unittest
import vim_darkdrop as sut


@unittest.skip("Don't forget to test!")
class VimDarkdropTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_darkdrop_example()
        self.assertEqual("Happy Hacking", result)
