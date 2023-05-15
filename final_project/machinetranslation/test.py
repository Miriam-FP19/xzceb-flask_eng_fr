import unittest
from translator import english_to_french as en_fr
from translator import french_to_english as fr_en

class EnglishToFrench(unittest.TestCase):
    """Test English to French""" 
    def test1(self): 
        self.assertEqual(en_fr('Hello.'),'Bonjour.') 
        self.assertNotEqual(en_fr('Hello.'),'Merci.') 
        self.assertEqual(en_fr('Thank you.'),'Je vous remercie.')

class FrenchToEnglish(unittest.TestCase): 
    """Test French to English"""
    def test2(self): 
        self.assertEqual(fr_en('Bonjour.'),'Hello.') 
        self.assertNotEqual(fr_en('Bonjour.'),'Thank you.') 
        self.assertEqual(fr_en('Je vous remercie.'),'Thank you.') 

unittest.main()