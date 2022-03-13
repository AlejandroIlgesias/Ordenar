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
