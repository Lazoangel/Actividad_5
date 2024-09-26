print ("Lazo Jimenez Angel Jesus 3W")
import random #Esta linea es para importar un numero al azar

numero_secreto = random.randint(1, 100) # Generar un número aleatorio entre 1 y 100
intentos = 0 

print("¡Bienvenido al juego de adivinar el número!") #Bienvenida al usuario
print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!") #indica al usuario elegir un numero del 1 al 100

while True: #indica el bucle que se hara hasta que se adivine el numero

    try: # Solicitar al usuario que adivine el número
        adivinanza = int(input("Introduce tu adivinanza: ")) #pide al usuario ingresar un numero
        intentos += 1 #Sube el contador de intentos
        
        if adivinanza < numero_secreto: #Compara el numero ingresado con el que se tiene que adivinar
            print("Demasiado bajo. Intenta de nuevo.") #Indica al usuario que su numero elegido es muy bajo
        elif adivinanza > numero_secreto: 
            print("Demasiado alto. Intenta de nuevo.") #Indica al usuario que su numero elegido es muy alto
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.") #Informa al usuario que a adivinado el numero y lo felicita
            #Sale del bucle
            break
    except ValueError:
        print("Por favor, introduce un número válido.") #Informa si el usuario ingresa un numero no valido