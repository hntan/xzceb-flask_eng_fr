import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    def englishToFrench(self):
        self.assertEqual(englishToFrench(''), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(''), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


unittest.main()
