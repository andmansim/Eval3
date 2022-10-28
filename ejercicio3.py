
def ordenar(lista, nombre):
    for i in lista:
        l_o = []
        l_o.append(i[nombre])
        if nombre == 'name':
            l_o.sort()
        else:
            l_o.sort(reverse=True)
    return l_o
    