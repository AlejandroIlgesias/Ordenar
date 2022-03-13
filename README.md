Mi repositorio es:https://github.com/AlejandroIlgesias/Ordenar.git
El codigo de cada programa consiste en lo siguiente:
El funcionamiento basico de la funcion consiste en desplazar todos los elementos de la lista el mismo numero de posiciones.Los parametros:unidades:a_desplazar->es el numero de unidades que se desplaza cada elemento y lista_de_elementos es la lista de los elementos que vamos a desplazar.La funcion desplazamiento funciona de la siguiente manera:Lo primero que hace es comprobar que el numero de unidades que quiero desplazar los elementos de la lista es menor o igual a la longitud de la lista.De ser así ejecuta el cuerpo de instrucciones que se encargaran del desplazamiento.De lo contrario no hace nada y no se ejecuta el desplazamiento.Las instrucciones que ejecutan el desplazamiento se basan en el siguiente hecho:Si desplazamos todos los elementos de la lista n unidades,los n primeros elementos empezando por el final de la lista(por la posicion len(lista)-1)se colocan al principio en el mismo orden en que aparecen en la lista original.Así la variable i almacena los n elementos que voy a poner al principio de la lista.La lista s se trata de una lista formada por los cortes de la lista original que he metido como parametro,de tal forma que los n ultimos elementos de la lista original empezando por el final de la lista ,por la posicion -1 y yendo de derecha a izquierda y en el orden en el que se encuentran ,los coloco al principio de la lista s usando la sintaxis de acceso a un rango de elementos de una lista de python y por ultimo añado los restantes elementos de la lista original en el orden en el que aparecen al final de la lista s.Al final la funcion me devuelve la lista s con todos los elementos desplazados n posiciones.



TAREA 1
El programa compara cada elemento de la lista con todos los elementos que se encuentran en posiciones posteriores.Cada vez que se encuentra un elemento con menor valor,se intercambian estos elementos,de tal manera que el menor valor siempre irá quedando a la izquierda.
TAREA 2
El programa consiste en dos bucles.El bucle interno compara cada elemento de la lista a ordenar con todos los elementos de la propia lista,y en caso de que el elemento que esta comparando sea mayor que otro intercambia sus posiciones.Una vez hecho esto el bucle externo vuelve a ejecutar el bucle interno de nuevo.Las veces que se repite el bucle interno son la mismas sea cual sea la longitud de la lista.He añadidio una estructura try-except para controlar que cuando el indice i+1 exceda el numero de indices de la lista se capture el error y se solucione de tal forma que el programa no deje de funcionar.

TAREA 3
El programa trabaja de la siguiente manera.Primero localiza el mayor valor de toda la lista usando la funcion maximo.Despues calcula el numero de unidades que se tiene que mover para quedar al final de la lista.Utiliza la funcion desplazamiento para mover todos los elementos de la lista ese mismo numero de unidades.Una vez dicho elemento queda
de ultimo,corta la lista utilizando el rango por indices para obtener la sublista con todos los elementos menos el ultimo elemento.Repite este proceso hasta que la subilista que obtiene es una lista de un elemento,el cual es el elemento mas pequeño de todos los de la lista original.

///
#TAREA 1
def orden(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[j]<x[i]:
                a=x[j]
                x[j]=x[i]
                x[i]=a
    return x
#def orden-->cada elemento de la lista x es comparado con los restantes
#elementos.cada vez que se encuentra un elemento con menor valor,se inter-
#cambian estos elementos,de tal manera que el menor valor siempre irá quedando
#a la izquierda.

#<---------------------------------------------------------------------------------------->

#TAREA 2
def ordena(l):
    n=len(l)#longitud de la lista
    o=0#indice para romper el bucle while
    while True:
        for i in range(n): # numero de elementos de la lista
        
            try:
                if l[i]>l[i+1]: #si el elemento de la lista es mayor que su siguiente
            
                    a=l[i+1]   #almaceno el valor del elemento siguiente en a
                    l[i+1]=l[i]  #al elemento siguiente le asigno el valor de su anterior elemento
                    l[i]=a #al enterior elemento le asigno el valor de su siguiente elemento
                    
                    if i+1<n:#numero de elementos de la lista
                        break#para cuando llega al ultimo elemento
            except IndexError:
                i+1==n-1
                break
        
        
        o=o+1#para romper el bucle
        
        if o==2*n:
            return l





#<------------------------------------------------------------------------------------------------------->
#TAREA 3
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
print(lista_ordenada)///


