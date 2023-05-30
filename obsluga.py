from nalesnik_z_serem import NalesnikZSerem
from pancake_klonowy import PancakeKlonowy
from nalesnik_bananowe_szalenstwo import Nalesnik_Bananowe_Szalenstwo
from ziemniaczany_szpinakowy import ZiemniaczanySzpinakowy

class Obsluga:
    def __init__(self):
        self.builder = None

    def przyjmijZamowienie(self,builder):
        self.builder = builder
        steps = (builder.usmaz,
                 builder.wypelnijFarszem,
                 builder.polejSosem,
                 builder.dostarcz)
        [step() for step in steps]

    @property
    def nalesnik(self):
        return self.builder.nalesnik