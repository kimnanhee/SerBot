from pop import Pilot, LiDAR
import random
import math
speed = 30

bot = Pilot.SerBot()
bot.setSpeed(speed)
lidar = LiDAR.Rplidar()
lidar.connect()
lidar.startMotor()

serbot_width = (1 / math.sqrt(3)) * 2 * 100
serbot_width = 500

def calcAngle(length): 
    radian = math.atan((serbot_width/2) / length)
    angle = radian * (180 / math.pi)
    return angle

def collisonDetect(length):
    vectors = lidar.getVectors()
    angle = calcAngle(length)
    detect = [False] * 8
    
    for i in range(8):
        h = []
        an_a = i*45 - angle
        an_b = i*45 + angle
        if an_a < 0:   an_a = 360 + an_a
        if an_a > 360: an_a = an_a - 360
        if an_b < 0:   an_b = 360 + an_b
        if an_b > 360: an_b = an_b - 360
        
        for v in vectors:
            if an_a < an_b:
                if(v[0] >= an_a and v[0] <= an_b):
                    h.append(v[1])
            else:
                if(v[0] >= an_a or v[0] <= an_b):
                    h.append(v[1])
                    
        if len(h) > 0:
            if min(h) < length: detect[i] = True
            else: detect[i] = False
    return detect

state = True
mode = 0
bot.move(mode * 45, speed)
while state:
    try:
        if collisonDetect(300)[mode]:
            bot.stop()
            continue

        de_list = collisonDetect(800)
        print(mode, de_list)
        
        if sum(de_list) == 8:
            bot.stop()
            print("detected all")
            continue

        if de_list[mode] == True:            
            while True:
                i = random.randint(0, 7)
                if de_list[i] == False:
                    break
            mode = i    
        bot.move(mode * 45, speed)
        
    except KeyboardInterrupt:
        state = False

lidar.stopMotor()       
bot.stop()
print("finish")