from pop import Pilot
from nh import Serbot
import random, math

speed = 30 # 속도

ser = Serbot(32)
bot = Pilot.SerBot()
bot.setSpeed(speed)

state = True
mode = 0 # 주행 방향
bot.move(mode * (360/ser.degree_num), speed)
while state:
    try:
        if ser.collisonDetect(300)[mode]:
            bot.stop()
            continue

        de_list = ser.collisonDetect(800)
        # print(mode, de_list)
        
        if sum(de_list) == ser.degree_num:
            bot.stop()
            print("detected all")
            continue
        if de_list[mode] == True:
            de_false_list = [i for i, val in enumerate(de_list) if not val]
            mode = random.choice(de_false_list)
        bot.move(mode * (360/ser.degree_num), speed)
        
    except KeyboardInterrupt:
        state = False

ser.stop()
bot.stop()
print("finish")