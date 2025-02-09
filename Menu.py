# Autor: Roberto Luzanilla
def menu():            
    while True:
        print("\n1- Escaneo de puertos\n")
        print("-----Más opciones pronto-----\n")
        print("0- Salir\n")
        print("Versión 1.0")
        
        opcion = int(input("Introduce una opción: "))
        
        if opcion == 1:
            import Escaneo
            Escaneo.seleccion_Tipos()
        elif opcion == 0:
            print("Gracias por usar mis herramientas")
            break  
        else:
            print("Opción no válida, por favor ingresa una opción válida.")

print("Hola, bienvenido a mi paquete de herramientas. Aquí podrás encontrar varias herramientas")
print("que he creado para mi aprendizaje. Espero que te sirvan estas herramientas.\nSi tienes alguna sugerencia o mejora, no dudes en decírmelo.")
menu()
