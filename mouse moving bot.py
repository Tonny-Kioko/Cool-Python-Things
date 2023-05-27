import pyautogui as pag
import random
import time

while True:
    x_coordinates = random.randint(700, 900)
    y_coordinate = random.randint(600, 700)
    pag.moveTo(x_coordinates, y_coordinate, 0.5)
    time.sleep(5)
