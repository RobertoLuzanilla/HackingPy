import socket

def escaneo_Rapido(ip, puerto):
    print(f"Escaneando IP: {ip} En los puertos: {puerto}")
    with open("escan_Rapido.txt", "a") as archivo:
            archivo.write(f"Escaneo en la IP {ip}\n")#Registra la ip en el archivo

    for i in puerto:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(5)
        result = s.connect_ex((ip,i))

        if result == 0:
            print(f"[+] Puerto {i} esta abierto")
            with open("escan_Rapido.txt", "a") as archivo:
                archivo.write(f"El puerto {i} esta abierto\n")
        
        else:
            print(f"[-] Puerto {i} esta cerrado")
            with open("escan_Rapido.txt", "a") as archivo:
                archivo.write(f"El puerto {i} esta cerrado\n")

        s.close()

    print("Escaneo finalizado\n,\n")


def seleccion_Tipos():
        while True:
            print("\nSelecciona una opcion\n")
            print("1-Escaneo de puertos rapido --Escaneo Rapido, verifica los puertos mas escenciales\n")
            print("2-Escaneo de puertos completo --Escaneo Completo, verifica todos los puertos\n")
            print("-----Mas opciones pronto-----\n")
            print("0-Salir")
            opcion = int(input())

            if opcion == 1:
                print("Escaneo Rapido")
                ip_objetivo = input("Introduce la IP a escanear: ")     
                puertos_a_escanear = [21,22,23,25,53,80,110,143,443,631,3389,3306,5432,5900,8080,9200]
                escaneo_Rapido(ip_objetivo, puertos_a_escanear)
            elif opcion == 2: 
                print("Escaneo Completo")
            elif opcion == 0:
                print("Saliendo...")
                print("Gracias ;)")
                break
            else :
                print("Opcion no valida")


seleccion_Tipos()
