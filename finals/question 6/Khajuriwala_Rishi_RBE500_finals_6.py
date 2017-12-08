import numpy as np
import glob
import csv
import matplotlib.pyplot as plt
import pylab as pltt
import math

reading_1 = []
for x in sorted(glob.glob('Lidar_1_*.csv')):
    with open(x) as csvfile:
        readings =csv.reader(csvfile)
        list1 = [float(''.join(row[0])) for row in readings]
        reading_1.append(list1)
# print(reading_1)

mean_1 =[]
for i in reading_1:
    mean_1.append(np.mean(i))
# print(mean_11)
reading_2 = []
for y in sorted(glob.glob('Lidar_2_*.csv')):
    with open(y) as csvfile:
        readings2 =csv.reader(csvfile)
        list1 = [float(''.join(row[0])) for row in readings2]
        reading_2.append(list1)
# print(reading_1)
mean_2 = []
for i in reading_2:
    mean_2.append(np.mean(i))
# print(mean_2)

q1 = 0.0
q_1 =[]
for j in mean_1[0:len(mean_1)]:
    q_1.append(q1)
    q1 += math.radians(45.0)

q2 = 0.0
q_2 =[]
for z in mean_2[0:len(mean_2)]:
    q_2.append(q2)
    q2 += math.radians(45.0)
# print(q_2)
# print(q_1)
fig = plt.figure()
ax = pltt.axes(polar=True)
ax.plot(q_1,mean_1,'ob')
plt.show()

fig2 = plt.figure()
ax = pltt.axes(polar=True)
ax.plot(q_2,mean_2,'or')
plt.show()
