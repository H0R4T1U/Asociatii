from Domain.cheltuiala import to_string
from Logic.crud import adauga_cheltuiala, modificare_cheltuiala, stergere_cheltuiala
from Logic.functionalitati import  sterge_toate_cheltuielile
from datetime import datetime


def UI_sterge_toate_cheltuielile(lista):
    nr_apt = int(input("Itroduceti numarul apartamentului: "))
    sterge_toate_cheltuielile(nr_apt,lista)


def UI_adauga_cheltuiala(lista):
    id = int(input("Introduceti id-ul: "))
    nr_apt = int(input("Itroduceti numarul apartamentului: "))
    suma =  int(input("Introduceti suma cheltuielii:"))
    data = datetime.strptime(input("Introduceti data cheltuielii(format zi/luna/an): "), "%d/%m/%Y")
    tip = input("Introduceti tip-ul cheltuielii: ")
    return adauga_cheltuiala(id, nr_apt, suma, data, tip, lista)


def UI_sterge_cheltuiala(lista):
    id = int(input("Introduceti id-ul:"))
    nr_apt = int(input("Introduceti numarul apartamentului: "))
    return stergere_cheltuiala(id,nr_apt,lista)


def UI_modifica_cheltuiala(lista):

    id = int(input("Introduceti id-ul:"))
    nr_apt = int(input("Introduceti numarul apartamentului: "))
    suma = int(input("Introduceti suma cheltuielii, introdu 00 ca sa nu schimbati:"))
    data = input("Introduceti data cheltuielii(format zi/luna/an): ")
    tip = input("Introduceti tip-ul cheltuielii: ")
    return modificare_cheltuiala(id,nr_apt,suma,data,tip,lista)


def ui_afisare_cheltuieli(lista):
    if lista:
        for cheltuiala in lista:
            print(to_string(cheltuiala))
    else:
        print("Nu mai exista nici o cheltuiala")


def print_options():
    print("1. Adaugare")
    print("2. Stergere")
    print("3. Modificare")
    print("--------------------------------------")
    print("4. Sterge toate cheltuielile apartament")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def run_menu(lista):
    while True:
        print_options()
        option = input("Cititi optiunea: ")
        if option =="1":
            lista = UI_adauga_cheltuiala(lista)
        if option =="2":
            lista = UI_sterge_cheltuiala(lista)
        if option =="3":
            lista = UI_modifica_cheltuiala(lista)
        if option == "4":
            lista = UI_sterge_toate_cheltuielile(lista)
        if option =="a":
            ui_afisare_cheltuieli(lista)
