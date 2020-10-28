def creeaza_prajitura(id, nume, descriere, pret, calorii, an):
    '''
    creaza un obiect de tipul prajitura
    :param id: id-ul prajiturii
    :param nume: numele prajiturii
    :param descriere: descrierea prajiturii
    :param pret: pretul prajiturii
    :param calorii: nr. de calorii al prajiturii
    :param an: anul introducerii in meniu al prajiturii
    :return: un obiect prajitura
    '''
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "calorii": calorii,
        "an": an,
    }

def get_id(prajitura):
    return prajitura['id']


def get_nume(prajitura):
    return prajitura['nume']


def get_descriere(prajitura):
    return prajitura['descriere']


def get_pret(prajitura):
    return prajitura['pret']


def get_calorii(prajitura):
    return prajitura['calorii']


def get_an(prajitura):
    return prajitura['an']

def to_string(prajitura):
    return "id: {}, nume: {}, descriere: {}, pret: {}, calorii: {}, an: {} ".format(
        get_id(prajitura),
        get_nume(prajitura),
        get_descriere(prajitura),
        get_pret(prajitura),
        get_calorii(prajitura),
        get_an(prajitura)
    )