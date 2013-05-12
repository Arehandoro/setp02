#UNIVERIDAD DE SANTIAGO DE CHILE
#Carrera:  Licenciatura en Ciencias de la Computación.
#Asignatura:  Lenguaje y Técnicas de Programación.
#Profesor:  Igor Caracci.
#Ayudante:  Andrés Caro Q.
#Autor del Programa:  Alejandro Alberto Sánchez Iturriaga.
#Problema 05 - Ca-chi-pún:

import os    #Se declara para usar clear y asi limpiar la pantalla.
from random import choice    #Libreria para función random, que sirve para elegir un elemento al azar de una lista o tupla.

def ganador_cachipun(game, contador):    #Función que evalua las jugadas de cachipum y retorna al ganador en pantalla.
    if( (game[0][1]=="R" or game[0][1]=="P" or game[0][1]=="T") and (game[1][1]=="R" or game[1][1]=="P" or game[1][1]=="T") ):    #Evalua las jugadas posibles, osea validas.
        print("Partida Nº",contador,"\t",game,"\n")
        if( (game[0][1]=="R" and game[1][1]=="T") or (game[0][1]=="P" and game[1][1]=="R") or (game[0][1]=="T" and game[1][1]=="P") ):
            print("¡Ganador! ",game[0])    #Si el primer jugador gana, lo retorna en pantalla.
        elif( (game[1][1]=="R" and game[0][1]=="T") or (game[1][1]=="P" and game[0][1]=="R") or (game[1][1]=="T" and game[0][1]=="P") ):
            print("¡Ganador! ",game[1])    #Si el segundo jugador gana, lo retorna en pantalla.
        else:
            print("¡Empate por lo tanto Ganador! ",game[0])    ##Si ocurre empate, gana primer jugador y lo retorna en pantalla.
    else:
        raise Exception("\n\n¡Jugada no válida!")    #Si se ingresa una jugada incorrecta, levanta la excepción.

print("###############  CA-CHI-PÚN  ###############\n\n")
print("Presione (1):  1 Jugador.\nPresione (2):  2 Jugadores.\n")
opcion = input("Ingrese el modo de juego... ")    #Lee la opción de jugadores ingresada por el usuario.
os.system("clear")    #Limpia la pantalla.

if(opcion == "1"):    #Si se juega a 1 jugador.
    nombre = input("Jugador:\nIngrese un Nombre:  ")    #Lee el nombre del jugador y lo guarda en la variable.
    num_game = int(input("\n\n\nIngrese el numero de partidas que desea jugar:  "))    #Lee el numero de jugadas y lo guarda en la variable.
    os.system("clear")    #Limpia la pantalla.
    contador = 1    #Se inicia un contador en 1.
    while(num_game >= contador):    #Mientras el contador sea menor o igual al numero de juegos.
        print("Jugadas:\t(R = Roca, P = Papel, T = Tijera)\n\n",nombre)
        play_1 = input("Ingrese su jugada:  ")    #Lee la jugada del jugador y la guarda en la variable.
        play_1 = play_1.upper()    #Si la letra de la jugada es ingresada en minuscula, la convierte en mayuscula.
        jugador_1 = [nombre, play_1]    #Crea una lista con el nombre y jugada del jugador.
        os.system("clear")    #Limpia la pantalla.
        jugadas = ["R","P","T"]    #Lista definidas para las posibles jugadas del computador.
        play_2 = choice(jugadas)    #Elije una jugada (letra) al azar de la lista y la guarda en la variable.
        jugador_2 = ["COMPUTADOR", play_2]    #Crea una lista anidada con las listas de ambos jugadores.
        os.system("clear")    #Limpia la pantalla.
        game = [jugador_1, jugador_2]    #Crea una lista anidada con las listas de ambos jugadores.
        ganador_cachipun(game, contador)    #Llama a la función, y envia la lista anidada y al contador como parámetros.
        contador = contador+1    #Aumenta 1 el contador.
        pause = input("\n\n\nPulsa la tecla ENTER para continuar... ")
        os.system("clear")    #Limpia la pantalla.
        
elif(opcion == "2"):    #Si se juega a 2 jugadores.
    nombre_1 = input("Jugador Nº1:\nIngrese un Nombre:  ")    #Lee el nombre del jugador y lo guarda en la variable.
    print("\n\n")
    nombre_2 = input("Jugador Nº2:\nIngrese un Nombre:  ")    #Lee el nombre del jugador y lo guarda en la variable.
    num_game = int(input("\n\n\nIngresen el numero de partidas que desean jugar:  "))    #Lee el numero de jugadas y lo guarda en la variable.
    os.system("clear")    #Limpia la pantalla.
    contador = 1    #Se inicia un contador en 1.
    while(num_game >= contador):    #Mientras el contador sea menor o igual al numero de juegos.
        print("Jugadas:\t(R = Roca, P = Papel, T = Tijera)\n\n",nombre_1)
        play_1 = input("Ingrese su jugada:  ")    #Lee la jugada del jugador y la guarda en la variable.
        play_1 = play_1.upper()    #Si la letra de la jugada es ingresada en minuscula, la convierte en mayuscula.
        jugador_1 = [nombre_1, play_1]    #Crea una lista con el nombre y jugada del primer jugador.
        os.system("clear")    #Limpia la pantalla.
        print("Jugadas:\t(R = Roca, P = Papel, T = Tijera)\n\n",nombre_2)
        play_2 = input("Ingrese su jugada:  ")    #Lee la jugada del jugador y la guarda en la variable.
        play_2 = play_2.upper()    #Si la letra de la jugada es ingresada en minuscula, la convierte en mayuscula.
        jugador_2 = [nombre_2, play_2]    #Crea una lista con el nombre y jugada del segundo jugador.
        os.system("clear")    #Limpia la pantalla.
        game = [jugador_1, jugador_2]    #Crea una lista anidada con las listas de ambos jugadores.
        ganador_cachipun(game, contador)    #Llama a la función, y envia la lista anidada y al contador como parámetros.
        contador = contador+1    #Aumenta 1 el contador.
        pause = input("\n\n\nPulsa la tecla ENTER para continuar... ")
        os.system("clear")    #Limpia la pantalla.

else:    #Si el número de jugadores no es igual a 1 o 2, levanta la excepción.
    raise Exception("\n\n¡Número incorrecto de jugadores! (Solo se puede 1 o 2 Jugadores).")

