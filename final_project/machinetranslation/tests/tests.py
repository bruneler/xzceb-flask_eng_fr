import unittest

from translator import englishtofrench, frencht


class Test_EnglishToFrench(unittest.TestCase):
    def test_eToF(self):
        self.assertEqual(englishtofrench("hello"), "bonjour")
        self.assertIsNotNone(englishtofrench(None), 'bonjour')


class Test_FrenchToEnglish(unittest.TestCase):
    def test_fToE(self):
        self.assertEqual(frenchtoenglish("bonjour"), "hello")
        self.assertIsNotNone(frenchtoenglish(None), "hello")


if __name__ == '__main__':
    unittest.main()

