# https://www.delftstack.com/ko/howto/matplotlib/how-to-automate-plot-updates-in-matplotlib/
import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.8 # 중력가속도
seta = 30 # 각도
Vo = 60 # 속도
t = 0
t_period = 0.5

fig = plt.figure()
x_list = [0]
y_list = [0]

while True:
    t += t_period

    x = Vo * math.cos(math.radians(seta)) * t # Vo cosθ t
    y = Vo * math.sin(math.radians(seta)) * t - 0.5 * g * t * t # Vo sinθ t - 0.5 g t^2

    x_list.append(x)
    y_list.append(y)
    if(y < 0):
        break

    plt.plot(x_list, y_list)
    plt.draw()
    plt.pause(0.001)
    fig.clear()

plt.plot(x_list, y_list)
plt.show()