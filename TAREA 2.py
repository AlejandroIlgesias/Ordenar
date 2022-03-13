def ordenaR(l):
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
