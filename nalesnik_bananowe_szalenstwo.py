import time
from nalesnik import Nalesnik
import settings

class Nalesnik_Bananowe_Szalenstwo:
        def __init__(self):
                self.nalesnik = Nalesnik('Naleśnik z nutellą i bananami z wiórkami gorzkiej czekolady')
                self.progress = settings.Czynnosc.zamowiono
        
        def usmaz(self):
                self.progress = settings.Czynnosc.smazony
                self.nalesnik.usmaz(settings.Rodzaj.pancake,5)   

        def wypelnijFarszem(self):
                self.progress = settings.Czynnosc.wypelniany
                farsz = None
                farsz_items = None
                self.nalesnik.wypelnij(farsz_items,farsz)
                
        def polejSosem(self):
                self.progress = settings.Czynnosc.polewany
                sos = 'Czekolada "Nutella", plastry banana, wiórki gorzkiej czekolady'
                sos_items = (settings.Sos.nutella, settings.Sos.plastry_banana, settings.Sos.wiórki_czekolady)
                self.nalesnik.polejSosem(sos_items,sos)

        def dostarcz(self):
                self.progress = settings.Czynnosc.dostarczany  
                print(f'Dostarczanie.') 
                time.sleep(2) 
                self.progress = settings.Czynnosc.gotowy  