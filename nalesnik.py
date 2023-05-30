import time

class Nalesnik:
    def __init__(self,name):
        self.nazwa = name
        self.placek = None
        self.polewa =  []
        self.farsz = []

    def __str__(self):
        return self.nazwa

    def usmaz(self,rodzajCiasta,pieczenie):
        self.placek = rodzajCiasta

        print(f'Smażenie ciasta typu: {self.placek.name}')
        time.sleep(pieczenie)
        print(f'Ciasto typu: {self.placek.name} usmażone')

    def wypelnij(self,skladniki,skladnikiOpis = None,):
        if skladnikiOpis is not None:
            print(f'Dodawanie skladników: ({skladnikiOpis})')
            self.farsz.append([t for t in skladniki])
            time.sleep(2)
            print(f'Naleśnik wypełniony i złożony')  

    def polejSosem(self,polewa,polewaOpis = None):
        if polewaOpis is not None:
            print(f'Dekorowanie składnikami: ({polewaOpis})')
            self.farsz.append([t for t in polewa])
            time.sleep(3)
            print(f'Naleśnik wypełniony i złożony') 

    