from Logic.crud import get_nr_apt


def sterge_toate_cheltuielile(nr_apt,lista):
    [cheltuiala for cheltuiala in lista if get_nr_apt(cheltuiala) != nr_apt]

