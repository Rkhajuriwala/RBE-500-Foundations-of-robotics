import numpy as np
import glob
import matplotlib.pyplot as plt
import csv
import pylab as pltt


mean = []
std = []
for x in sorted(glob.glob('LIDAR_100ms_Degrees*.csv')):
    with open(x) as csvfile:
        readings = csv.reader(csvfile)
        list1 = [float(''.join(row[0])) for row in readings ]
        mean.append(np.mean(list1))
        std.append(np.std(list1))

#print (mean)
#print (std)

plt.plot(mean,std,'bo')
plt.title('Question 1(a)')
plt.xlabel('Mean')
plt.ylabel('Standard')
plt.show()

fig = plt.figure()
ax = pltt.axes(polar=True)
s= np.array(mean)
t = 2*np.pi/360 * np.array(list(range(0,360,10)))
ax.plot(t,s,'b')
plt.show()
