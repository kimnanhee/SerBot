from pop import LiDAR
import math

lidar = LiDAR.Rplidar()
lidar.connect()
lidar.startMotor()

degree_num = 36 # 장애물을 측정하는 각도의 개수
degree = [i for i in range(0, 360, 360//degree_num)]

serbot_width = (1 / math.sqrt(3)) * 2 * 100
serbot_width = 500

# 거리에 따른 측정 각도를 반환하는 함수
def calcAngle(length): 
    radian = math.atan((serbot_width/2) / length)
    angle = radian * (180 / math.pi)
    return angle

# 거리에 따른 장애물을 측정하는 함수
def collisonDetect(length):
    vectors = lidar.getVectors()
    angle = calcAngle(length)
    detect = [False] * degree_num # 장애물이 없으면 False, 있으면 True
    
    for i in range(degree_num):
        h = []
        an_a = i*(360/degree_num) - angle
        an_b = i*(360/degree_num) + angle
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
            if min(h) < length: detect[i] = True # 장애물이 있다.
            else: detect[i] = False
    return detect

if __name__ == "__main__":
    while True:
        de_list = collisonDetect(800)
        print(de_list)