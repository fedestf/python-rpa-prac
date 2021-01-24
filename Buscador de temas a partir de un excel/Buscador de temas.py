import pyautogui as robot
import time
from openpyxl import *

FILE_PATH = "Temas.xlsx"
SHEET = "Hoja1"

workbook = load_workbook(FILE_PATH)
sheet = workbook[SHEET]

minimizar = 1919, 1064
google = 239, 335
direc = 210, 51
buscar = 681, 130
cancion = 697, 313
cerrar = 1893, 15
duracionCancion = 10

lista_canciones = []

for row in sheet.iter_rows():
    lista_canciones.append(row[0].value)


def abrir(pos, click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)


time.sleep(2)

abrir(minimizar)
time.sleep(1)

abrir(google, click=2)
time.sleep(2)

robot.hotkey("alt", "space")
time.sleep(0.5)
robot.typewrite("x")

time.sleep(1)
abrir(direc)

robot.typewrite("www.youtube.com")
robot.hotkey("enter")
time.sleep(3)

for i in range((len(lista_canciones))):
    abrir(buscar, click=3)
    robot.typewrite(lista_canciones[i])
    robot.hotkey("enter")
    time.sleep(2)
    abrir(cancion)
    time.sleep(duracionCancion)

abrir(cerrar)
