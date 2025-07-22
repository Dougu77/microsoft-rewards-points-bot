from datetime import datetime
from .constants import *
from . import console
import threading
import pyautogui
import keyboard
import random
import time
import os

def open_edge() -> None:
    '''summary_ Abre o navegador
    '''
    os.startfile(EDGE_PATH)
    console.opening_edge()
    time.sleep(WAIT_TIME)

def open_bing_main_page() -> None:
    '''summary_ Faz a primeira pesquisa, que faz entrar na tela principal do Bing
    '''
    keyboard.press_and_release('ctrl+t')
    pyautogui.click(TOP_SEARCH_BAR_POSITIONS[0], TOP_SEARCH_BAR_POSITIONS[1])
    keyboard.write(random.choice(COUNTRIES))
    keyboard.press_and_release('enter')
    time.sleep(WAIT_TIME)

def search(stop_event:threading.Event) -> None:
    '''summary_ Pesquisa nomes de países 30 vezes

    Args:
        stop_event (threading.Event): Evento de quando é pressionada a tecla "S", indicando que é para parar
    '''
    temporary_list = COUNTRIES.copy()
    for _ in range(30):
        if stop_event.is_set():
            console.stop_search()
            break

        subject = random.choice(temporary_list)
        pyautogui.tripleClick(MAIN_SEARCH_BAR_POSITIONS[0], MAIN_SEARCH_BAR_POSITIONS[1])
        keyboard.press_and_release('backspace')
        keyboard.write(subject)
        keyboard.press_and_release('enter')
        console.register_subject(subject, datetime.now())
        temporary_list.remove(subject)
        time.sleep(WAIT_TIME)

def close_edge() -> None:
    '''summary_ Fecha a aba utilizado pelo bot
    '''
    keyboard.press_and_release('ctrl+w')
    console.closing_edge()
