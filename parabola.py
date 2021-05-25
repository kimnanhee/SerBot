# https://lhh3520.tistory.com/41
import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.8 # 중력가속도
seta = 30 # 각도
Vo = 60 # 속도
t = 0

x_list = []
y_list = []

while True:
    t += 0.01

    x = Vo * math.cos(math.radians(seta)) * t # Vo cosθ t
    y = Vo * math.sin(math.radians(seta)) * t - 0.5 * g * t * t # Vo sinθ t - 0.5 g t^2

    x_list.append(x)
    y_list.append(y)
    if(y < 0):
        break

plt.plot(x_list, y_list)
plt.show()