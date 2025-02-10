# Escaneo de Puertos

Este proyecto contiene herramientas para realizar escaneos de puertos en una dirección IP específica, lo que es útil para detectar puertos abiertos o cerrados en un sistema remoto.

## Requisitos

- Python 3.x
- Librerías requeridas:
    - socket (viene por defecto con Python, no es necesario instalarla)
    - ping3 (instalable con pip)

## Instalación

1. Clona este repositorio o descarga los archivos.

    ```bash
    git clone <URL del repositorio>
    ```

2. Navega al directorio donde descargaste o clonaste el repositorio.

    ```bash
    cd <directorio_del_repositorio>
    ```

3. Instala las librerías requeridas.

    ```bash
    pip install ping3
    ```

## Uso
    
1. Ejecuta el script principal `Menu.py` con Python:

    ```bash
    python Menu.py
    ```

2. El script proporcionará un menú donde podrás seleccionar diferentes herramientas de escaneo de puertos.

### Escaneo Rápido

El script [Escaneo.py] realiza un escaneo rápido de los puertos más esenciales en una dirección IP específica. Los puertos a escanear están predefinidos en el código.

Los resultados del escaneo se guardan en un archivo llamado [escan_Rapido.txt]. En este archivo, podrás ver los puertos abiertos y cerrados de la IP escaneada.

### Escaneo Completo (Próximamente)

Estamos trabajando en una versión completa de escaneo que incluirá la posibilidad de escanear todos los puertos (1-65535). Mantente al tanto para futuras actualizaciones.

## Autor

Roberto Luzanilla  
Desarrollador y aprendiz de ciberseguridad.

## Contribuciones

Si tienes alguna sugerencia o mejora, no dudes en abrir un issue o enviar un pull request.