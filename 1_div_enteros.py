def clasificar_numeros(lista):
    listaPos = []  
    listaNeg = [] 

    for e in lista:
        if e < 0:
            listaNeg.append(e)
        else:
            listaPos.append(e)

        listaPos.sort()
        listaNeg.sort()
            
    return listaPos, listaNeg


lista = [1, -5, 7, 2, -22, 0]
lista_pos, lista_neg = clasificar_numeros(lista)


print("Lista positivos ordenados: ", lista_pos)
print("Lista negativos ordenados: ", lista_neg)