#  두시간 마다 물 마시라고 알려주기
import schedule
import time
import datetime

my_money = 0

def drink_water():
    now = datetime.datetime.now()
    print(now, "물 마실 시간입니다!")
    

schedule.every(2).minutes.do(drink_water)


while True:
    schedule.run_pending()
    time.sleep(1)