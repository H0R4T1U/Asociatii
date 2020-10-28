from Domain.cheltuiala import  get_id, creeaza_cheltuiala,get_nr_apt, get_suma, get_tip, get_data
from datetime import  datetime
def get_by_id(lista_cheltuieli,id):
    '''
    Gaseste cheltuiala dupa nr apartament
    :param lista_cheltuieli:
    :param id: nr apartament
    :return:
    '''
    for cheltuiala in lista_cheltuieli:
        if(get_id(cheltuiala) == id):
            return cheltuiala
    return None


def adauga_cheltuiala(id, nr_apt, suma, data, tip, lista):
    '''

    :param id:
    :param suma:
    :param data:
    :param tip:
    :return:
    '''
    cheltuiala = creeaza_cheltuiala(id, nr_apt, suma, data, tip)
    return lista + [cheltuiala]


def modificare_cheltuiala(id,nr_apt,suma,data,tip,lista):

    lista_modificata = []
    for cheltuiala in lista:
        if(get_id(cheltuiala) == id and get_nr_apt(cheltuiala) == nr_apt):
            cheltuiala_noua = creeaza_cheltuiala(
                id,
                nr_apt,
                suma if suma != 0 else get_suma(cheltuiala),
                datetime.strptime(data, "%d/%m/%Y")  if data != "" else get_data(cheltuiala),
                tip if tip != "" else get_tip(cheltuiala)
            )
            lista_modificata.append(cheltuiala_noua)
        else:
            lista_modificata.append(cheltuiala)
    return lista_modificata


def stergere_cheltuiala(id,nr_apt,lista):
    '''

    :param id:
    :param nr_apt:
    :param lista:
    :return:
    '''
    return [cheltuiala for cheltuiala in lista if get_id(cheltuiala) != id and get_nr_apt(cheltuiala) != nr_apt]