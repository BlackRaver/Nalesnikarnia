from enum import Enum


def init():
    global Czynnosc
    global Rodzaj
    global Farsz
    global Sos
    Czynnosc = Enum('Czynnosc','zamowiono smazony wypelniany polewany dostarczany gotowy')
    Rodzaj = Enum('Rodzaj','francuskie pancake ziemniaczane')
    Farsz = Enum('Farsz','śmietana szarpana_wołowina truskawki szpinak shroama_kurczak cebula kukurydza ser_żółty')
    Sos = Enum('Sos','bita_śmietana orzechy_laskowe nutella dzem_wisniowy cukier_puder wiórki_kokosowe sos_czekoladowy wiórki_czekolady syrop_klonowy plastry_banana')

