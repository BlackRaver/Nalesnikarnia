import time
from nalesnik import Nalesnik
import settings

class NalesnikZSerem:
        def __init__(self):
                self.nalesnik = Nalesnik('Naleśnik z serem i truskawkami w polewie czekoladowej')
                self.progress = settings.Czynnosc.zamowiono
        
        def usmaz(self):
                self.progress = settings.Czynnosc.smazony
                self.nalesnik.usmaz(settings.Rodzaj.francuskie,3)   

        def wypelnijFarszem(self):
                self.progress = settings.Czynnosc.wypelniany
                farsz = 'śmietana, kawałki truskawek'
                farsz_items = (settings.Farsz.śmietana,settings.Farsz.truskawki)
                self.nalesnik.wypelnij(farsz_items,farsz)
                
        def polejSosem(self):
                self.progress = settings.Czynnosc.polewany
                sos = 'Bita śmietana, polewa czekoladowa, wiórki gorzkiej czekolady'
                sos_items = (settings.Sos.bita_śmietana,settings.Sos.sos_czekoladowy,settings.Sos.wiórki_czekolady)
                self.nalesnik.polejSosem(sos_items,sos)
        def dostarcz(self):
                self.progress = settings.Czynnosc.dostarczany  
                print(f'Dostarczanie.') 
                time.sleep(2) 
                self.progress = settings.Czynnosc.gotowy  
                
