import time
from nalesnik import Nalesnik
import settings

class ZiemniaczanySzpinakowy:
        def __init__(self):
                self.nalesnik = Nalesnik('"Szpinakowa Kura"')
                self.progress = settings.Czynnosc.zamowiono
        
        def usmaz(self):
                self.progress = settings.Czynnosc.smazony
                self.nalesnik.usmaz(settings.Rodzaj.ziemniaczane,3)   

        def wypelnijFarszem(self):
                self.progress = settings.Czynnosc.wypelniany
                farsz = 'smażona cebula, shroma z kurczaka'
                farsz_items = (settings.Farsz.cebula,settings.Farsz.szpinak,settings.Farsz.shroama_kurczak)
                self.nalesnik.wypelnij(farsz_items,farsz)
                
        def polejSosem(self):
                self.progress = settings.Czynnosc.polewany
                sos = None
                sos_items = None
                self.nalesnik.polejSosem(sos_items,sos)
        def dostarcz(self):
                self.progress = settings.Czynnosc.dostarczany  
                print(f'Dostarczanie.') 
                time.sleep(2) 
                self.progress = settings.Czynnosc.gotowy  