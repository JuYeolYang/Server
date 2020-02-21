import threading
import time

def worker(msg):
    """ start 하면서 전달받은 msg 출력, 5초 후에 종료 """
    # 쓰레드 생성시 지정해준 name과 인자로 받은 msg 출력
    print("{} is start : {}".format(threading.currentThread().getName(), msg))
    time.sleep(5)
    print("{} is end". format(threading.currentThread().getName()))

def main():
    for i in range(10):
        '''
        쓰레드는 threading.Thread 메소드를 써서 만들면 된다.
        target에는 쓰레드로 띄울 함수명을 넣어주면 된다.
        name으로 쓰레드의 이름을 지정할 수 있다.
        args로 함수의 인자를 넘겨줄 수 있다.
        이름은 threading.currentThread().getName()로 확인 가능하다.
        '''
        msg = "hello {}".format(i)
        th = threading.Thread(target = worker, name = "[th def {}]".format(i), args = (msg, ))
        th.start() #위에서 생성한 쓰레드를 시작한다.

if __name__ == '__main__':
    main()