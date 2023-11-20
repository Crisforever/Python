import re;
from colorama import init, Fore
import time

init()

def display_ascii_art(text, color):
    print(color + text)

print(Fore.GREEN)
display_ascii_art("""


    .oooooo.             o8o            .o88o.
   d8P'  `Y8b            `"'            888 `"
  888          oooo d8b oooo   .oooo.o o888oo   .ooooo.  oooo d8b  .ooooo.  oooo    ooo  .ooooo.  oooo d8b
  888          `888""8P `888  d88(  "8  888    d88' `88b `888""8P d88' `88b  `88.  .8'  d88' `88b `888""8P
  888           888      888  `"Y88b.   888    888   888  888     888ooo888   `88..8'   888ooo888  888
  `88b    ooo   888      888  o.  )88b  888    888   888  888     888    .o    `888'    888    .o  888
   `Y8bood8P'  d888b    o888o 8""888P' o888o   `Y8bod8P' d888b    `Y8bod8P'     `8'     `Y8bod8P' d888b
 
""", Fore.GREEN)

print(Fore.MAGENTA + "Github: https://github.com/Crisforever")
time.sleep(2)
print()
print("> Spanish version <")

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return 'La contraseña debe contener un mínimo de 8 caracteres.'
    
    elif not re.search(r'[a-z]',contraseña):
        return 'La contraseña debe tener minimo una letra en minuscula'
    
    elif not re.search(r'[A-Z]',contraseña):
        return 'La contraseña debe tener minimo una letra en mayuscula'
    elif not re.search(r'\d',contraseña):
        return 'La contraseña debe tener minimo un numero'
    elif not re.search(r'\W',contraseña):
        return 'La contraseña debe tener a el menos un caracter no alfanumerico'
    elif ' ' in contraseña:
        return 'La contraseña no debe tener espacios en blanco'
    else:
        return 'Contraseña segura'
    
print(Fore.BLUE+('Inserta tu contraseña:'))
print()
contraseña = input()

resultContraseña = validar_contraseña(contraseña)
print(resultContraseña)
