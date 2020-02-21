import threading
import time

def worker(msg):
    print("{} is start : {}".format(threading.currentThread().getName(), msg))
    time.sleep(5)
    print("{} is end".format(threading.currentThread.getName()))

def main():
    msg = "hello"
    th = threading.Thread(target = worker, name = "[Demon]", args = (msg,))
    th.setDaemon(True)
    th.start()

    print("Main Thread End")


if __name__ == '__main__':
    main()