def maximo(v):
    n=len(v)
    r=v[0]
    p=0
    for i in range(1,n):
        if v[i]>r:
            r=v[i]
            p=i
    return p
#def maximo-->La estrategia consiste en iniciar la variable de salida r,con
#el primer elemento del vector.mediante un ciclo se compara cada uno de los otros
#elementos con el valor asignado a r.En cada comparacion si el elemento tiene un
#valor mayor que r,se actualiza r a ese valor y tambien se actualiza la posicion
#o indice de este elemento.


#TAREA 3
def desplazamiento(unidades_a_desplazar,lista_de_elementos):
    if unidades_a_desplazar<=len(lista_de_elementos):
        i=len(lista_de_elementos)-unidades_a_desplazar
        s=lista_de_elementos[i:len(lista_de_elementos)]+lista_de_elementos[0:i]
    return s





#Localizar el valor maximo de la lista y su indice.Una vez localizado mover el
#valor maximo a la ultima posicion de la lista deplazando todos los elementos
#las posiciones que sean necesarias.

lista1=[6,3,4,7,13,2,5,1]#lista a ordenar.
lista_ordenada=[]

i=True
while i:
    valor_maximo=maximo(lista1)
    unidades_a_desplazar=(len(lista1)-1)-valor_maximo
    lista_modificada=desplazamiento(unidades_a_desplazar,lista1)
    lista_ordenada=[lista_modificada[-1]]+lista_ordenada
    lista1=lista_modificada[0:(len(lista_modificada)-1)]
    if len(lista1)==1:
        i=False
print(lista_ordenada)









