import threading
import time
import bot
import server

def is_any_thread_alive(threads):
    return True in [t.is_alive() for t in threads]

def main():
    x1 = threading.Thread(target=bot.startbot, daemon=True)
    x2 = threading.Thread(target=server.startflask, daemon=True)
    x1.start()
    x2.start()
    

    while is_any_thread_alive([x1,x2]):
        time.sleep(0)

if __name__ == '__main__':
    main()