import socket

def escaneo(ip, puerto):
    
    print(f"Escaneando IP: {ip} En los puertos: {puerto}")
    for i in puerto:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(5)
        result = s.connect_ex((ip,i))

        if result == 0:
            print(f"[+] Puerto {i} esta abierto")
        else:
            print(f"[-] Puerto {i} esta cerrado")

        s.close()

ip_objetivo = input("Introduce la IP a escanear: ")
puertos_a_escanear = [21,22,80,443,8080]

escaneo(ip_objetivo, puertos_a_escanear)