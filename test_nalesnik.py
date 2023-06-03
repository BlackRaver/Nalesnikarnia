import unittest
import settings
from nalesnik_z_serem import NalesnikZSerem
from pancake_klonowy import PancakeKlonowy
from nalesnik import Nalesnik
from obsluga import Obsluga 

class TestNalesnik(unittest.TestCase):
    settings.init()

    #@unittest.skip('take to much time')
    def test_nalesnik1(self):

        print("TEST 1")
        placek = Nalesnik("testowy normalny")
        self.assertEqual(placek.nazwa,"testowy normalny")

        placek.usmaz(settings.Rodzaj.francuskie,1)
        self.assertEqual(placek.placek,settings.Rodzaj.francuskie)
        
        farsz_test=[settings.Farsz.śmietana,settings.Farsz.borowka_amerykanska]
        placek.wypelnij(farsz_test,"śmietana, borówki amerykańskie")
        self.assertEqual(placek.farsz,[farsz_test]) 

        #Test jednostkowy spełnił swoją role, i wykrył błąd w kodzie który został już poprawiony
        polewa_test=[settings.Sos.bita_śmietana,settings.Sos.nutella,settings.Sos.sos_czekoladowy]
        placek.polejSosem(polewa_test,"bita śmietana, nutella, sos czekoladowy")
        self.assertEqual(placek.polewa,[polewa_test]) 
    
    #@unittest.skip('take to much time')
    def test_nalesnik2(self):
        
        print("TEST 2")
        placek = Nalesnik("testowy pusty")
        self.assertEqual(placek.nazwa,"testowy pusty")

        placek.usmaz(settings.Rodzaj.ziemniaczane,0.5)
        self.assertEqual(placek.placek,settings.Rodzaj.ziemniaczane)
        
        farsz_test=[]
        placek.wypelnij(farsz_test,"")
        self.assertEqual(placek.farsz,[farsz_test]) 

        polewa_test=[]
        placek.polejSosem(polewa_test,"")
        self.assertEqual(placek.polewa,[polewa_test]) 

    
    def test_nalesnik_z_serem(self):

        print("TEST 3")
        kelner_test = Obsluga()
        kelner_test.przyjmijZamowienie(NalesnikZSerem())
        self.assertIsInstance(kelner_test.builder,NalesnikZSerem)
        
        placek = Nalesnik('Naleśnik z serem i truskawkami w polewie czekoladowej')
        placek.placek = settings.Rodzaj.francuskie
        placek.farsz =  [settings.Farsz.śmietana,settings.Farsz.truskawki]
        placek.polewa = [settings.Sos.bita_śmietana,settings.Sos.sos_czekoladowy,settings.Sos.wiórki_czekolady]

        self.assertEqual(kelner_test.builder.nalesnik.nazwa,placek.nazwa)
        self.assertEqual(kelner_test.builder.nalesnik.placek,placek.placek)
        self.assertEqual(kelner_test.builder.nalesnik.farsz,[placek.farsz])
        self.assertEqual(kelner_test.builder.nalesnik.polewa,[placek.polewa])
        

    def test_pancake_klonowy(self):

        print("TEST 4")
        kelner_test = Obsluga()
        kelner_test.przyjmijZamowienie(PancakeKlonowy())
        self.assertIsInstance(kelner_test.builder,PancakeKlonowy)
        
        placek = Nalesnik('Pancake Amerykański z syropem klonowym i wiśniowym dżemem')
        placek.placek = settings.Rodzaj.pancake
        placek.farsz =  []
        placek.polewa = [settings.Sos.syrop_klonowy,settings.Sos.dzem_wisniowy]

        self.assertEqual(kelner_test.builder.nalesnik.nazwa,placek.nazwa)
        self.assertEqual(kelner_test.builder.nalesnik.placek,placek.placek)
        self.assertEqual(kelner_test.builder.nalesnik.farsz,placek.farsz)
        self.assertEqual(kelner_test.builder.nalesnik.polewa,[placek.polewa])

if __name__ == '__main__':
    unittest.main()


