#aqui tenemos que ver cual es el que falta, por ejemplo, del ejemplo 1,5, 10 donde n=20 debemos de verificar primero cuales numeros no se pueden formar por si mismos, 
#podemos validar ordenando una lista y despues de ordenarla ver si son iguales, pues tampoco se pueden repetir elementos, y no dejar que se agreguen a la lista de suma los valores que existen en mayores a n


array=[1,5, 10] 
n = 20

#desde aqui debemos ver cual es el que se pierde, entonces debemos generar las posibles sumas, desde agregando los mismos numeros del array original y despues generando las sumas 
#entoncespara comparar podemos generar una lista con todos los valores de 1 hasta n,

#generacion de 1 a n

array_aux = list(range(1, n+1))
#print(array_aux)

#aqui va el que genera todas las sumas entre ellos, que seria como un ciclo, que el cilco va iterando
list_list_aux=[]
list_aux=[]
i=len(array)
for num in array:
    
    list_aux.append(num)
    #print("lista aux : " + str(list_aux))
    aux_1=0
    while aux_1 <=  i:
        aux_1= aux_1+ 1
        #print(aux_1)


##--------------------------
possible = set([0])
patches = 0 
print("possible: " + str(possible))
for num in array:
    new_sum = set()
    print("num: " + str(num))
    for x in possible:
        suma = x + num
        print("suma=  " + str(x)  +" +" + str(num))
        print("suma flag: " + str(suma))
        if suma <= n:
            new_sum.add(suma)
            
            print("new_sum: " + str(new_sum))
    possible.update(new_sum)
print(possible)

i =1
while i <= n:
    if i not in possible:
        patches += 1
        possible.add(i)
        new_sum = set()
        for x in possible:
            suma = x + i
            if suma <= n:
                new_sum.add(suma)
        possible.update(new_sum)
    i += 1
print("Patches needed: " + str(patches))