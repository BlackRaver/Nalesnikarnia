import time
from nalesnik import Nalesnik
import settings

class PancakeKlonowy:
        def __init__(self):
                self.nalesnik = Nalesnik('Pancake Amerykański z syropem klonowym i wiśniowym dżemem')
                self.progress = settings.Czynnosc.zamowiono
        
        def usmaz(self):
                self.progress = settings.Czynnosc.smazony
                self.nalesnik.usmaz(settings.Rodzaj.pancake,4)   

        def wypelnijFarszem(self):#to do
                self.progress = settings.Czynnosc.wypelniany
                farsz = None
                farsz_items = None
                self.nalesnik.wypelnij(farsz_items,farsz)
                
        def polejSosem(self):
                self.progress = settings.Czynnosc.polewany
                sos = 'Syrop klonowy, dżem wiśniowy'
                sos_items = (settings.Sos.syrop_klonowy,settings.Sos.dzem_wisniowy)
                self.nalesnik.polejSosem(sos_items,sos)
        def dostarcz(self):
                self.progress = settings.Czynnosc.dostarczany  
                print(f'Dostarczanie.') 
                time.sleep(2) 
                self.progress = settings.Czynnosc.gotowy  