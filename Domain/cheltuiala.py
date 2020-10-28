def creeaza_cheltuiala(id,nr_apt,suma,data,tip):
    '''
    Creaza un obiect de tipul cheltuiala
    :param id: nr apartament
    :param suma: suma cheltuala
    :param data: data cheltuieli
    :param tip: tipul cheltuieli
    :return:
    '''
    return{
        "id":id,
        "nr_apt":nr_apt,
        "suma":suma,
        "data":data,
        "tip":tip
    }

def get_id(cheltuiala):
    return cheltuiala['id']


def get_nr_apt(cheltuiala):
    return cheltuiala["nr_apt"]


def get_suma(cheltuiala):
    return cheltuiala['suma']


def get_data(cheltuiala):
    return cheltuiala['data']


def get_tip(cheltuiala):
    return cheltuiala['tip']





def to_string(cheltuiala):

    return "id: {},Nr. apartament: {}, suma: {}, data: {}, tip: {} ".format(
        get_id(cheltuiala),
        get_nr_apt(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala),
    )