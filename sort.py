def insertion_sort( lista ):
    for i in range( 1, len( lista ) ):
        chave = lista[i]
        k = i
        while k > 0 and chave < lista[k - 1]:
            lista[k] = lista[k - 1]
            k -= 1
        lista[k] = chave
    return lista

def selection_sort(lista):
    for i in range(len(lista)):
        mypos = i
        for j in range(i+1, len(lista)):
           if lista[mypos] > lista[j]:
                mypos = j      
                temp = lista[i]
                lista[i] = lista[mypos]
                lista[mypos] = temp
    return lista

def bubble_sort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista
