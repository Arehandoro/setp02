#UNIVERIDAD DE SANTIAGO DE CHILE
#Carrera:  Licenciatura en Ciencias de la Computación.
#Asignatura:  Lenguaje y Técnicas de Programación.
#Profesor:  Igor Caracci.
#Ayudante:  Andrés Caro Q.
#Autor del Programa:  Alejandro Alberto Sánchez Iturriaga.
#Problema 02 - Palíndroma:

def es_palindroma(cadena):    #Función que retorna un (true o false) si el string es palindroma.
    lista = list(cadena)    #Guarda el string en una lista.
    aux = list(cadena)    #Guarda el string en una lista auxiliar para cambiar la lista al revés.
    aux.reverse()    #Da vuelta la lista.
    if lista == aux:    #Si la lista original y la lista al revés son iguales retorna un true, sino un false.
        return True
    else:
        return False

cadena = input("Ingrese un string: ")    #Lee el string ingresado por el usuario y lo guarda en la variable "cadena".
if es_palindroma(cadena):    #Llama a la función si "es_palindroma" y verifica si lo es.
    print("\nEl string es palindroma.")
else:
    print("\nEl string no es palindroma.")

