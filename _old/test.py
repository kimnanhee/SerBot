from pop import Pilot, LiDAR
import time
import math
speed = 20

bot = Pilot.SerBot()
bot.setSpeed(speed)
lidar = LiDAR.Rplidar()
lidar.connect()
lidar.startMotor()

serbot_width = (1 / math.sqrt(3)) * 2 * 1000

def calcAngle(length): 
    radian = math.atan2(serbot_width/2, length)
    angle = radian * 180 / math.pi
    return angle

def collisonDetect(angle):
    vectors = lidar.getVectors()
    detect = []
    
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
            if min(h) < 500: detect.append(True)
            else: detect.append(False)

    return detect

angle = calcAngle(1000)
print("angle :", angle)
collisonDetect(angle)

state = True
mode = 0
while state:
    try:
        vectors = lidar.getVectors()
        scan = []
        
        for v in vectors:
            if v[0] >= (360 - angle) or v[0] <= (0 + angle):
                scan.append(v[1])
        
        if len(scan) > 0:
            if min(scan) < 500:
                print("detected")
                de_list = collisonDetect(angle)
                print(de_list)
                cnt = 0
                for de in de_list:
                    if de == False:
                        break
                    cnt += 1
                mode = cnt
        
        if mode == 8: 
            bot.stop()
            print("detected all")
        else: bot.move(mode*45, speed)
        time.sleep(0.2)
        
    except KeyboardInterrupt:
        state = False

lidar.stopMotor()       
bot.stop()
print("finish")