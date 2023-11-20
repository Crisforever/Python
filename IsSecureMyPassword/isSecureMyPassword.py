import re
import time

def display_ascii_art(text, color):
    print(f"\033[{color}m{text}\033[0m")

display_ascii_art("""
    .oooooo.             o8o            .o88o.
   d8P'  `Y8b            `"'            888 `"
  888          oooo d8b oooo   .oooo.o o888oo   .ooooo.  oooo d8b  .ooooo.  oooo    ooo  .ooooo.  oooo d8b
  888          `888""8P `888  d88(  "8  888    d88' `88b `888""8P d88' `88b  `88.  .8'  d88' `88b `888""8P
  888           888      888  `"Y88b.   888    888   888  888     888ooo888   `88..8'   888ooo888  888
  `88b    ooo   888      888  o.  )88b  888    888   888  888     888    .o    `888'    888    .o  888
   `Y8bood8P'  d888b    o888o 8""888P' o888o   `Y8bod8P' d888b    `Y8bod8P'     `8'     `Y8bod8P' d888b
""", "32")


display_ascii_art("Github: https://github.com/Crisforever", "35")
time.sleep(2)
print()
display_ascii_art("> Spanish version <", "34")
print()

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return 'La contraseña debe contener un mínimo de 8 caracteres.'
    
    elif not re.search(r'[a-z]', contraseña):
        return 'La contraseña debe tener al menos una letra en minúscula.'
    
    elif not re.search(r'[A-Z]', contraseña):
        return 'La contraseña debe tener al menos una letra en mayúscula.'
    elif not re.search(r'\d', contraseña):
        return 'La contraseña debe tener al menos un número.'
    elif not re.search(r'\W', contraseña):
        return 'La contraseña debe tener al menos un carácter no alfanumérico.'
    elif ' ' in contraseña:
        return 'La contraseña no debe tener espacios en blanco.'
    else:
        print()
        return 'Contraseña segura.'
print()
display_ascii_art("Inserta tu contraseña:", "34")
print()
contraseña = input()

resultContraseña = validar_contraseña(contraseña)
display_ascii_art(resultContraseña, "34")

