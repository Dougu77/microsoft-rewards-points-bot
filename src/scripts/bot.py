from . import console
from .data import *
import pyautogui
import keyboard
import random
import time
import os

class Bot():
    
    def __init__(self):
        self.edge_was_already_open = False

    def open_edge(self) -> None:
        os.startfile(EDGE_PATH)
        console.opening_edge()
        time.sleep(3)

    def open_bing_main_page(self) -> None:
        keyboard.press_and_release('ctrl+t')
        pyautogui.click(TOP_SEARCH_BAR_POSITIONS[0], TOP_SEARCH_BAR_POSITIONS[1])
        keyboard.write(random.choice(FOOTBALL_TEAMS))
        keyboard.press_and_release('enter')
        time.sleep(3)

    def search(self) -> None:
        temporary_list = FOOTBALL_TEAMS.copy()
        for _ in range(30):
            subject = random.choice(temporary_list)
            pyautogui.tripleClick(MAIN_SEARCH_BAR_POSITIONS[0], MAIN_SEARCH_BAR_POSITIONS[1])
            keyboard.press_and_release('backspace')
            keyboard.write(subject)
            keyboard.press_and_release('enter')
            temporary_list.remove(subject)
            time.sleep(3)

    def close_edge(self) -> None:
        keyboard.press_and_release('ctrl+w')
        console.closing_edge()
