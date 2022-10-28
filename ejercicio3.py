
def ordenar(lista, nombre):
    l_o = []
    for i in lista:
        l_o.append(i[nombre])
    print(l_o)
    if nombre == 'name':
        l_o.sort()
    else:
        l_o.sort(reverse=True)
    return l_o
    