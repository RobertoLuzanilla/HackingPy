import socket
import ping3
import time
import ipaddress

def escribir_Log(mensaje, archivo): #Funcion para escribir en un archivo de texto
    with open(archivo, "a") as archivo:
        archivo.write(mensaje)

def verificar_IP(ip): #Verifica si la ip que se introduce es valida
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def ping_Detallado(ip): #Lanza un ping a la ip que se introduce
    for i in range(4):
        time.sleep(3) #Hace que espere 3 segundos antes de hacer el siguiente ping
        mensaje = f"{i}- Haciendo ping a la IP {ip}\n" #Mensaje que se guardara en el archivo de texto
        escribir_Log(mensaje, "ping_Detallado.txt")
        try: 
            ping = ping3.ping(ip) * 1000  # Multiplicamos por 1000 para obtener el tiempo en milisegundos
            if ping is None:
                print(f"{i}- No se pudo obtener el ping a la IP {ip}")
                mensaje = f"{i}- No se pudo obtener el ping a la IP {ip}\n" #Mensaje que se guardara en el archivo de texto
                escribir_Log(mensaje, "ping_Detallado.txt")
            else:
                print(f"{i}- El ping a la IP {ip} es de: {ping:.2f} ms")
                mensaje = f"{i}- El ping a la IP {ip} es de: {ping:.2f} ms\n" #Mensaje que se guardara en el archivo de texto
                escribir_Log(mensaje, "ping_Detallado.txt")

        except Exception as e:
            print(f"{i}- Error al hacer ping a la IP {ip}: {e}")
            mensaje = f"{i}- Error al hacer ping a la IP {ip}: {e}\n" #Mensaje que se guardara en el archivo de texto
            escribir_Log(mensaje, "ping_Detallado.txt")

def escaneo_Rapido(ip, puerto):#Un escaneo a los puertos mas comunes
    print(f"Escaneando IP: {ip} En los puertos: {puerto}")
    mensaje = f"Escaneando IP: {ip} En los puertos: {puerto}\n" #Mensaje que se guardara en el archivo de texto
    escribir_Log(mensaje, "escan_Rapido.txt")

    for i in puerto:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(5)
        result = s.connect_ex((ip,i))

        if result == 0:
            print(f"[+] Puerto {i} esta abierto")
            mensaje = f"El puerto {i} esta abierto\n" #Mensaje que se guardara en el archivo de texto
            escribir_Log(mensaje, "escan_Rapido.txt")
        
        else:
            print(f"[-] Puerto {i} esta cerrado")
            mensaje = f"El puerto {i} esta cerrado\n" #Mensaje que se guardara en el archivo de texto
            escribir_Log(mensaje, "escan_Rapido.txt")

        s.close()

    print("Escaneo finalizado\n,\n")


def seleccion_Tipos(): #Menu de la clase Escaneo
        while True:
            print("\nSelecciona una opcion\n")
            print("1-Ping --Verifica si hay conexion activa a la IP\n") #Verifica si hay conexion
            print("2-Escaneo de puertos rapido --Escaneo Rapido, verifica los puertos mas escenciales\n") #Escaneo de puertos
            print("3-Escaneo de puertos completo --Escaneo Completo, verifica todos los puertos\n")#Escaneo de puertos PRONTO
            print("-----Mas opciones pronto-----\n")
            print("0-Salir")
            try:
                opcion = int(input("Introduce una opción: "))
            except ValueError:
                print("Por favor, introduce un número entero.")
            continue

            if opcion == 1:
                print("Ping")
                ip_objetivo = input("Introduce la IP a escanear:")
                if verificar_IP(ip_objetivo):
                    ping_Detallado(ip_objetivo)
                else:
                    print("La IP no es valida")
            elif opcion == 2: 
                print("Escaneo Rapido")
                ip_objetivo = input("Introduce la IP a escanear: ")   
                if  verificar_IP(ip_objetivo):
                        puertos_a_escanear = [21,22,23,25,53,80,110,143,443,631,3389,3306,5432,5900,8080,9200]#Puertos comunes a escanear
                        escaneo_Rapido(ip_objetivo, puertos_a_escanear)
                else:
                    print("La IP no es valida") 
            elif opcion == 3:
                print("Escaneo Completo")
                print("----Pronto----")
            elif opcion == 0:
                print("Saliendo...")
                print("Gracias ;)")
                break
            else :
                print("Opcion no valida")

if __name__ == "__main__": #Para que se ejecute el menu
    seleccion_Tipos()
