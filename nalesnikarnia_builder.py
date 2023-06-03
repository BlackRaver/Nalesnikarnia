from nalesnik import Nalesnik
from nalesnik_bananowe_szalenstwo import Nalesnik_Bananowe_Szalenstwo
from nalesnik_z_serem import NalesnikZSerem
from pancake_klonowy import PancakeKlonowy
from ziemniaczany_szpinakowy import ZiemniaczanySzpinakowy
from obsluga import Obsluga
import settings

builder = "definiowanie"

def sprawdzDostepnosc(builders):
    
    result = False
    try:
        wiadomosc = 'Podawane dziś naleśniki to:\n [s]Francuski z serem,\n [p]Pancake z syropem klonowym,\n [pb]Pancake Bananowe szaleństwo,\n [zsz] Ziemniaczany "Szpinakowa Kura"\n\n:'
        wybranyNalesnik = input(wiadomosc)
        global builder 
        builder = builders[wybranyNalesnik]()
        for menu in builders:
            if wybranyNalesnik == menu:
                result = True
    except KeyError:
        error_msg =  'Przykro mi ale nie ma takiego (key m)'
    return (result,builder)

def main():
    settings.init()
    while True:
        
        builders = dict(s=PancakeKlonowy, p=PancakeKlonowy, pb=Nalesnik_Bananowe_Szalenstwo, zsz=ZiemniaczanySzpinakowy)
        czyMamyWKarcie = False
        print('______________________________________________________')
        print(f'Witam! Czy moge przyjąć zamówienie?')
        while not czyMamyWKarcie:
            czyMamyWKarcie, builder = sprawdzDostepnosc(builders)
            if(not czyMamyWKarcie):
                print( "Przykro mi ale nie ma takiego naleśnika")

        print("\n")
        kelner = Obsluga()
        kelner.przyjmijZamowienie(builder)
        nalesnik = kelner.nalesnik

        print("\n")

        print(f'Oto zamówiony {nalesnik}!\nSMACZNEGO\n######################################################\n\n')

if __name__ == '__main__':
    main()