#no ejecutar sin saber este codigo
#se debe conocer la ruta de la maquina victima

import subprocess

def ejecutar_bat():
    try:
        # Ruta completa del archivo .bat
        ruta_bat = r"C:\Users\crist\Desktop\Python\Trojan spamer\repeater.bat"
        subprocess.run([ruta_bat], shell=True)
    except FileNotFoundError:
        print("Error: El archivo .bat no fue encontrado.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    ejecutar_bat()
