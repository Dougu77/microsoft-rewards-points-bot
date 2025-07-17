from scripts import bot, console

if __name__ == '__main__':
    try:
        console.start()
        bot.open_edge()
    except Exception as msg:
        console.exception(msg)
    finally:
        console.end()
