def validarList(lista): 
    if (lista is None or not isinstance(lista, list) or len(lista) == 0): raise ValueError("Tem de ser uma lista, não nula e com pelo menos um elemento")

def validarTupla(tupla):
    if (tupla is None or not isinstance(tupla, tuple) or not isinstance(tupla[0], list) or not isinstance(tupla[1], bool)): raise ValueError("Tem de ser passado uma tupla, com uma lista na posição 0 e um boolean na posição 1")

def swap(lista, i, j):
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp
    return lista

def quickSort(lista, left, right):
    if (left < right):
        pivot = partition(lista, left, right)
        quickSort(lista, left, pivot - 1)
        quickSort(lista, pivot + 1, right)
    return lista

def partition(lista, left, right):
    i = left
    pivot = lista[left]
    for j in range(left + 1, right + 1):
        if (lista[j] <= pivot):
            i += 1
            swap(lista, i, j)
    swap(lista, left, i)
    return i

"""
Intersect espera duas tuplas, cada uma com 2 itens: 
posição 0: Lista
Posição 1: Boolean

O boolean serve para indicar se a lista já está ordenada ou se precisa ser ordenada. A lista deve ter pelo menos um elemento.
"""
def intersect(tupla1, tupla2):

    validarTupla(tupla1)

    validarTupla(tupla2)

    lista1 = tupla1[0]

    validarList(lista1)

    lista2 = tupla2[0]

    validarList(lista2)

    if (not tupla1[1] and len(lista1) > 1): quickSort(lista1, 0, len(lista1) - 1)

    if (not tupla2[1] and len(lista2) > 1): quickSort(lista2, 0, len(lista2) - 1)

    if (len(lista1) > 1): eliminarRepeticoes(lista1, 0)

    if (len(lista2) > 1): eliminarRepeticoes(lista2, 0)

    if (len(lista1) <= len(lista2)):
        return intersectLogica(lista1, lista2)
    else:
        return intersectLogica(lista2, lista1)

def intersectLogica(lista1, lista2):
    i = 0
    j = 0
    while (len(lista1) - 1 >= i and len(lista2) - 1 >= j):
        if (lista1[i] == lista2[j]):
            i += 1
            j += 1
        elif (lista1[i] > lista2[j]):
            if (len(lista2) - 1 == j):
                return removerItens(lista1, i)
            j += 1
        else:
            lista1.remove(lista1[i])
    return lista1
    
def removerItens(lista, i):
    if (len(lista) - 1 < i): return lista
    else:
        lista.remove(lista[i])
        return removerItens(lista, i)
    
def eliminarRepeticoes(lista, i):
    if (len(lista) - 1 < i or i < 1): return lista
    else:
        if (lista[i - 1] == lista[i]): 
            lista.remove(lista[i])
            return eliminarRepeticoes(lista, i)
        else:
            return eliminarRepeticoes(lista, i + 1)

#Exemplo:
print(intersect(([4, 3, 2, 1001, 33, 4, 6, 63, 70, 1], False), ([ 1, 2, 3, 5, 7, 8, 11, 70, 102],True)))
