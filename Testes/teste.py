
palavra = ["abcd", "d"]

def teste(palavra):
    if (len(palavra) - 1 != 2):
        for letra in palavra: print(ord(letra))
    print("passou")

def maiorLen(lista):
    if (len(lista) -1 == 0): return 0
    temp = len(lista[0])
    lista.remove(lista[0])
    if (temp >= maiorLen(lista)): return temp

print(ord("a"), ord("A"))
