#UNIVERIDAD DE SANTIAGO DE CHILE
#Carrera:  Licenciatura en Ciencias de la Computación.
#Asignatura:  Lenguaje y Técnicas de Programación.
#Profesor:  Igor Caracci.
#Ayudante:  Andrés Caro Q.
#Autor del Programa:  Alejandro Alberto Sánchez Iturriaga.
#Problema 06 - Craps:

#Libreria para función random:
from random import choice    #Libreria que sirve para elegir un elemento al azar de una lista o tupla.
from random import sample    #Libreria que sirve para elegir uno o varios elementos al azar de una lista, tupla o conjunto.

#Función que genera las combinaciones de suma de los 2 dados.
def creacion_dados():
    numeros = (1, 2, 3, 4, 5, 6)    #Tupla que posee los numeros de los dados.
    lista_36tuplas = list()    #Se declara una lista vacia, para guardar todas las combinaciones de tuplas.
    for elemento in numeros:    #Ciclos que generan las 36 combinaciones posibles de dados.
        for elemento_2 in numeros:
            tupla = (elemento, elemento_2)    #Se agregan los elementos a la tupla formando las conbinaciones.
            lista_36tuplas.append(tupla)    #Se agregan las tuplas con las combinaciones a la lista.
    dado = list()    #Se declara una lista vacia, para guardar todos los conjuntos de sumas de dados.
    suma = 0    #Se declara un contador en cero.
    while(suma < 13):    #Mientras el contador "suma" sea menor que 13. 
        conjunto_suma = set()    #Se declara un conjunto vacio, para ingresar las tuplas con las mismas sumas.
        for tupla in lista_36tuplas:
            if((tupla[0] + tupla[1]) == suma):    #Si la suma de la tupla es igual a la del contador, la tupla ingresa al conjunto.
                conjunto_suma.add(tupla)
        dado.append(conjunto_suma)    #Se agregan los conjuntos de suma de dados a la lista dado.
        suma = suma + 1    #Aumenta en 1 el contador "suma"
    return dado

#Función que genera de forma aleatoria el lanzamientos de dados, y define si el juego termina ganando, perdiendo, o continúa.
def craps(dado):
    pierdes = dado[2] | dado[3] | dado[12]    #Conjunto que posee las combinaciones de suma de dados cuando uno pierde.
    ganas = dado[7] | dado[11]    #Conjunto que posee las combinaciones de suma de dados cuando uno gana.
    enter = input("\n\nPresione la tecla ENTER para lanzar los dos dados...  ")    #Variable "enter" es para crear el efecto de lanzamiento.
    suma_dado = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)    #Tupla que posee todas las posibles sumas de los 2 dados.
    s = choice(suma_dado)    #Función random.choice(), elije un numero al azar, para usarlo como la suma de los 2 dados.
    lanzamiento = sample(dado[s], 1)    #Función random.sample(), elije un tupla al azar del conjunto "dado[s]" y la retorna como lista.
    print("\n\nTu lanzamiento de dados fue:\t",lanzamiento)
    if lanzamiento[0] in pierdes:    #Si la tupla (lanzamiento) esta en el conjunto "pierdes".
        print("\n¡Perdiste!\nEl juego termino...")
    elif lanzamiento[0] in ganas:    #Si la tupla (lanzamiento) esta en el conjunto "ganas".
        print("\n¡Ganaste!\nEl juego termino...")
    else:
        print("\nEl juego continua...")
        termino = 0    #Variable utilizada para salir del (while), si "termino = 1" sale del (while).
        while(termino != 1):    #Bucle que termina cuando se gana o pierde.
            punto = s    #Se guarda la suma de dados para establecer un punto.
            enter = input("\n\nPresione la tecla ENTER para lanzar los dos dados...  ")    #Variable para el efecto de lanzamiento.
            suma_dado = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)    #Tupla que posee todas las posibles sumas de los 2 dados.
            s = choice(suma_dado)    #Función random.choice(), elije un numero al azar, para usarlo como la suma de los 2 dados.
            lanzamiento = sample(dado[s], 1)    #Función random.sample(), elije un tupla al azar del conjunto "dado[s]".
            print("\n\nTu lanzamiento de dados fue:\t",lanzamiento)
            if lanzamiento[0] in dado[punto]:    #Si la tupla (lanzamiento) esta en el conjunto "dado[punto]".
                print("\n¡Ganaste!\nEl juego termino...")
                termino = 1    #La variable se iguala a 1 para salir del bucle.
            elif lanzamiento[0] in dado[7]:    #Si la tupla (lanzamiento) esta en el conjunto "dado[7]".
                print("\n¡Perdiste!\nEl juego termino...")
                termino = 1    #La variable se iguala a 1 para salir del bucle.
            else:
                print("\nEl juego continua...")


print("\n###############  JUEGO DE AZAR - CRAPS  ###############")
dado = creacion_dados()
craps(dado)

