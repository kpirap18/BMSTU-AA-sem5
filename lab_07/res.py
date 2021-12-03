import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('resSS.txt')
print(df)

fig, ax = plt.subplots(2, 1)

speed = list(df['res']) 
speed2 = list(df['res']) 
city = list(df['name'])
N = len(city)

for i in range(N-1):
    for j in range(N-i-1):
        if city[j] > city[j+1]:
            city[j], city[j+1] = city[j+1], city[j]
            speed[j], speed[j+1] = speed[j+1], speed[j]
 

y_pos = np.arange(len(speed)) 

fig.set_figwidth(15)    #  ширина и
fig.set_figheight(4)    #  высота "Figure"
fig.set_facecolor('floralwhite')
ax[0].bar(y_pos, speed, alpha=0.5) 
ax[1].bar(y_pos, speed2, alpha=0.5) 
ax[0].set_facecolor('seashell')
ax[1].set_facecolor('seashell')


plt.show()