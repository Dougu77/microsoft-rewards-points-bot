from scripts.bot import Bot
from scripts import console

if __name__ == '__main__':
    bot = Bot()
    try:
        console.start()
        bot.open_edge()
        bot.open_bing_main_page()
        bot.search()
        bot.close_edge()
    except Exception as msg:
        console.exception(msg)
    finally:
        console.end()
