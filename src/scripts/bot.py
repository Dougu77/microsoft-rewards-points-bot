from time import sleep
from . import console
from .data import *
import pyautogui
import keyboard
import random
import os

def open_edge() -> None:
    try:
        os.startfile(EDGE_PATH)
    except Exception as msg:
        console.exception(msg)

def open_bing_main_page() -> None:
    try:
        pyautogui.click(TOP_SEARCH_BAR_POSITIONS[0], TOP_SEARCH_BAR_POSITIONS[1])
        keyboard.write(random.choice(FOOTBALL_TEAMS))
        sleep(3)
    except Exception as msg:
        console.exception(msg)

def search() -> None:
    try:
        temporary_list = FOOTBALL_TEAMS
        for index in range(30):
            subject = random.choice(temporary_list)
            pyautogui.tripleClick(MAIN_SEARCH_BAR_POSITIONS[0], MAIN_SEARCH_BAR_POSITIONS[1])
            keyboard.press_and_release('backspace')
            keyboard.write(subject)
    except Exception as msg:
        console.exception(msg)
