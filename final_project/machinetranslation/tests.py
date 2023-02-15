import unittest

from translator import englishToFrench, frenchToEnglish


class Test_EnglishToFrench(unittest.TestCase):
    def test_eToF(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)


class Test_FrenchToEnglish(unittest.TestCase):
    def test_fToE(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("None"), "")
        self.assertNotEqual(frenchToEnglish(0), 0)

if __name__ == '__main__':
    unittest.main()

