from . import console
from .data import *
import pyautogui
import keyboard
import os

def open_edge() -> None:
    try:
        os.startfile(EDGE_PATH)
    except Exception as msg:
        console.exception(msg)
