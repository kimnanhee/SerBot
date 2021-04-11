from pop import Pilot
from nh import degree_num, collisonDetect, lidar
import random, math

speed = 30 # 속도

bot = Pilot.SerBot()
bot.setSpeed(speed)

state = True
mode = 0 # 주행 방향
bot.move(mode * (360/degree_num), speed)
while state:
    try:
        if collisonDetect(300)[mode]:
            bot.stop()
            continue

        de_list = collisonDetect(800)
        print(mode, de_list)
        
        if sum(de_list) == degree_num:
            bot.stop()
            print("detected all")
            continue
        if de_list[mode] == True:
            de_false_list = [i for i, val in enumerate(de_list) if not val]
            mode = random.choice(de_false_list)
        bot.move(mode * (360/degree_num), speed)
        
    except KeyboardInterrupt:
        state = False

lidar.stopMotor()
bot.stop()
print("finish")