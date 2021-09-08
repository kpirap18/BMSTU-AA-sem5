import unittest
import random
from time import time
import string

from main import levenshtein_matrix, levenshtein_recursive, levenshtein_matrix_recursive, damerau_levenshtein_recursive

def RandomString(strLength = 5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(strLength))

class TestDistanse(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(self.function("", ""), 0)

    def testSame(self):
        self.assertEqual(self.function("abc", "abc"), 0)
        self.assertEqual(self.function("0", "0"), 0)

    def testDifferent(self):
        self.assertEqual(self.function("a", ""), 1)
        self.assertEqual(self.function("", "1"), 1)
        self.assertEqual(self.function("b", "c"), 1)
        self.assertEqual(self.function("bc", "b"), 1)
        self.assertEqual(self.function("bc", "c"), 1)
        self.assertEqual(self.function("ab", "cd"), 2)


class TestLevDistanse(TestDistanse):
    def setUp(self):
        self.function = levenshtein_matrix

    def testTypo(self):
        self.assertEqual(self.function("ac", "ca"), 2)
        self.assertEqual(self.function("abc", "cba"), 2)


class TestDamLevDistanse(TestDistanse):
    def setUp(self):
        self.function = damerau_levenshtein_recursive

    def testTypo(self):
        self.assertEqual(self.function("ac", "ca"), 1)
        self.assertEqual(self.function("abc", "cba"), 2)


class TestTwoFunctions(unittest.TestCase):
    n = 15

    def testCompareSameLen(self):
        for i in range(TestTwoFunctions.n):
            str1 = RandomString(5)
            str2 = RandomString(5)
            self.assertEqual(self.f1(str1, str2), self.f2(str1, str2))

    def testCompareDifLen(self):
        for i in range(TestTwoFunctions.n):
            str1 = RandomString(3)
            str2 = RandomString(5)
            self.assertEqual(self.f1(str1, str2), self.f2(str1, str2))

    def testCompareEmpty(self):
        for i in range(TestTwoFunctions.n):
            str1 = RandomString(4)
            str2 = RandomString(0)
            self.assertEqual(self.f1(str1, str2), self.f2(str1, str2))


class TestLev(TestTwoFunctions):
    def setUp(self):
        self.f1 = levenshtein_recursive
        self.f2 = levenshtein_matrix_recursive


class TestDamLev(TestTwoFunctions):
    def setUp(self):
        self.f1 = damerau_levenshtein_recursive
        self.f2 = levenshtein_recursive

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLev)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDamLev))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDamLevDistanse))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLevDistanse))
    unittest.TextTestRunner().run(suite)
    # unittest.main()