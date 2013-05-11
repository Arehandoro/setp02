#UNIVERIDAD DE SANTIAGO DE CHILE
#Carrera:  Licenciatura en Ciencias de la Computación.
#Asignatura:  Lenguaje y Técnicas de Programación.
#Profesor:  Igor Caracci.
#Ayudante:  Andrés Caro Q.
#Autor del Programa:  Alejandro Alberto Sánchez Iturriaga.
#Problema 03 - Funes el Memorioso:

from operator import itemgetter    #Se declara al operador para ordenar el diccionario en una lista de tuplas de la segunda clave.

def ordena_ingresa(cadena):
    cadena_mayus = cadena.upper()    #Convierte todas las letras minusculas del string en mayusculas y guarda el string resultante.
    lista = cadena_mayus.split()    #La función split() retorna una lista conteniendo las subcadenas en las que se divide nuestra cadena al dividirlas por los espacios en blancos y salto de lineas.
    diccionario = dict()    #Se declara un diccionario vacio.
    for palabra in lista:    #Recorre la lista palabra por palabra.
        frecuencia = lista.count(palabra)    #La función count() retorna el número de veces que se encuentra la palabra en la lista.
        diccionario[palabra] = frecuencia    #Ingresa la palabra con su frecuencia al diccionario. (llave=palabra, valor=frecuencia)
    return sorted(diccionario.items(), key=itemgetter(1), reverse=True)    #Retorna una lista de los pares (llave, valor), ordenados por el valor de mayor a menor.

f = open('funes.txt', encoding='utf-8')    #Abre el archivo y lo guarda en la variable "f".
cadena = f.read()    #Guarda todo el contenido del archivo retornado en string en cadena.
f.close()    #Cierra el archivo.
print("Diccionario (Palabra, Frecuencia) Ordenado Mayor a Menor según frecuencia:\n\n",ordena_ingresa(cadena))    #Llama a la función que ingresa las palabras y frecuencias al diccionario, y las imprime ordenadas.
