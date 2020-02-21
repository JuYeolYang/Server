import threading
import time

class Worker(threading.Thread):
    ''' 클래스 생성시 threading.Thread를 상속받아 만들면 된다.'''

    def __init__(self, args, name = ""):
        """ __init__ 메소드 안에서 threading.Thread를 init한다."""
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
    
    def run(self):
        """start()시 실제로 실행되는 부분이다."""
        print("{} is start : {}".format(threading.currentThread().getName(), self.args[0]))
        time.sleep(5)
        print("{} is end".format(threading.currentThread().getName()))


def main():
    for i in range(10):
        #threading.Thread 대신, 클래스명으로 쓰레드 객체를 생성하면 된다.
        msg = "hello"
        th = Worker(name = "[th cls {}]".format(i), args = (msg, ))
        th.start() #run()에 구현한 부분이 실행된다.

if __name__ == "__main__":
    main()