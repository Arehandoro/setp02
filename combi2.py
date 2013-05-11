#UNIVERIDAD DE SANTIAGO DE CHILE
#Carrera:  Licenciatura en Ciencias de la Computación.
#Asignatura:  Lenguaje y Técnicas de Programación.
#Profesor:  Igor Caracci.
#Ayudante:  Andrés Caro Q.
#Autor del Programa:  Alejandro Alberto Sánchez Iturriaga.
#Problema 04 - Coeficiente del demonio 2.0:

from itertools import combinations    #Se declara función que calcula la combinatoria y crea las combinaciones posibles.

def combinatoria_2(conjunto, K):    #Función que calcula las combinaciones de elementos en tuplas en el conjunto.
    aux = combinations(conjunto, K)    #Crea las combinaciones de tuplas del conjunto, y las guarda en un dirección de memoria en (aux).
    combinaciones = list()    #Se declara una lista vacia para las combinaciones.
    for elemento in aux:    #Recorre los elementos de la dirección de memoria de (aux) y los guarda en la lista (combinaciones).
        combinaciones.append(elemento)    #Agrega los elementos a la lista.
    return combinaciones    #Retorna una lista con las tuplas.

N = int(input("Ingrese la cantidad (N) elementos del Conjunto:  "))    #Lee los numeros (N, K) ingresados por el usuario como enteros.
K = int(input("Ingrese la cantidad (K) elementos de las Tuplas:  "))
if(N > 0 and K >= 0 and K <= N):    #Si el Numero (N) mayor que cero, y un Numero (k) mayor o igual a cero y menor que (N).
    conjunto = set()    #Se declara conjunto vacio.
    print("\n\nConjunto:\n")
    while(N != 0):    #Mientras (N) sea distinto de cero, pide al usuario que ingrese un elemento al conjunto.
        elemento = input("Ingrese un elemento:  ")
        conjunto.add(elemento)    #Se agrega un elemento al conjunto.
        N = N-1    #El valor (N) disminuye 1 en cada ciclo.
    print("\nLas Combinaciones de Tuplas que se pueden formar con el Conjunto son:\n\n",combinatoria_2(conjunto, K))    #Llama a la función que retorna la lista con las combinaciones y las imprime. 
else:
    print("\n¡¡Error!!\nIngrese un Numero (N) mayor que cero, y un Numero (k) mayor o igual a cero y menor que (N).")


