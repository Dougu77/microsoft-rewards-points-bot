from scripts import bot, console
import threading
import keyboard

# Cria um evento para sinalizar parada
stop_event = threading.Event()

def run_bot() -> None:
    try:
        bot.open_edge()
        bot.open_bing_main_page()
        bot.search(stop_event)
    except Exception as msg:
        console.exception(msg)

def monitor_keyboard() -> None:
    while not stop_event.is_set():
        if keyboard.is_pressed('s'):
            stop_event.set()

if __name__ == '__main__':
    console.start()

    # Thread do bot
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Thread que monitora a tecla 'S'
    keyboard_thread = threading.Thread(target=monitor_keyboard)
    keyboard_thread.start()

    # Aguarda a finalização das threads
    bot_thread.join()
    stop_event.set()  # garante que a thread do teclado pare
    keyboard_thread.join()
    
    bot.close_edge()
    console.end()
