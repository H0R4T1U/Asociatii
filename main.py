from UI.console import run_menu
from Logic.crud import adauga_cheltuiala

def main():
    lista = []
    lista = adauga_cheltuiala(1, 1, 500, "25/10/2020","intretinere", lista)
    lista = adauga_cheltuiala(2, 1, 1000, "14/9/1979", "canal", lista)
    run_menu(lista)

main()