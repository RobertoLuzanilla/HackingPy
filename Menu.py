# Autor: Roberto Luzanilla
import Escaneo

def menu():            
    while True: #En este bucle se ejecutará el menú, donde escogeremos la opcion que deseamos
        print("\n1- Escaneo de puertos\n") #Manda a otro archivo con mas opciones
        print("-----Más opciones pronto-----\n") #Agregar un encriptador de contraseas
        print("0- Salir\n")
        print("Versión 1.1")
        try:
            opcion = int(input("Introduce una opción: "))
        except ValueError:
            print("Por favor, introduce un número entero.")
            continue
        if opcion == 1:
            Escaneo.seleccion_Tipos()
        elif opcion == 0:
            print("Gracias por usar mis herramientas")
            break  
        else:
            print("Opción no válida, por favor ingresa una opción válida.")

#Este es un mensaje de bienvenida
print("\nHola, bienvenido a mi paquete de herramientas. Aquí podrás encontrar varias herramientas")
print("que he creado para mi aprendizaje. Espero que te sirvan estas herramientas.\nSi tienes alguna sugerencia o mejora, no dudes en decírmelo.")
menu()
