import schedule
import time


def hello():
    print("Hello Matteo!")

schedule.every(5).seconds.do(hello)


while True:
    schedule.run_pending()
    time.sleep(1)