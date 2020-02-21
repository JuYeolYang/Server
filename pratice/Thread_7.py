import threading #threading 모듈 import

class myThread (threading.Thread): #threading.Thread 상속받음

    def __init__(self, threadID): #초기화 작업
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self): #.start()를 했을때 실행될 내용
        print("Starting " + str(self.threadID))
        for i in range(1,101):
            print("{0} {1}".format(self.threadID,i))
        print("Exiting " + str(self.threadID))


myThread(1).start()
myThread(2).start()


'''
thread1 = myThread(1) #thread1생성
thread2 = myThread(2) #thread2생성

thread1.start() #thread1실행
thread2.start() #thread2실행
'''