import csv
from math import sqrt
import matplotlib.pyplot as plt

readings=[]

with open('LIDAR_100ms_Wander.csv','rb') as csvfile:
		reader1= csv.reader(csvfile)
		my_list = list(reader1)

#print my_list
for b in my_list:
    #print b
    str1 = ''.join(b)
    some=int(str1)
    readings.append(some)
i = 0
list_size = float(len(my_list))
list_format = len(my_list)


for n in range(0,list_format):
    if readings[n]>4000:
        i = i+1

ans_a= float(i/list_size)
print 'Answer_a :',ans_a

s = 0
for g in range(0,list_format):
    if readings[g]<5:
        s = s+1


ans_b = float(s/list_size)
print 'Answer_b:',ans_b

readingstemp = list(readings)
readingsrange=[]
c = []
cr = []

for x in range(0,len(readingstemp)):
    if (readingstemp[x]<3500 and readingstemp[x]>3000):
        readingsrange.append(readingstemp[x])
#plt.plot(readingsrange)
#plt.show()


def mean(list):
    """calculates mean"""
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return (sum / len(list))
print 'Answer_c Mean:',mean(readingsrange)

def stddev(list):
    """calculates standard deviation"""
    sum = 0
    m = mean(list)
    for i in range(len(list)):
        sum += pow((list[i]-m),2)
    return sqrt(sum/len(list)-1)

print 'Answer_c Standard Deviation:',stddev(readingsrange)

c = list(readings)
for x in range(0,(len(readings)-1)):
    if (c[x]<3000 and c[x]>=5):
        cr.append(c[x])        

cr.insert(0,0)
count_object = 0
for x in range(0,(len(cr)-1)):
    if ((cr[x] - cr[x+1]) > 200):
        count_object = count_object+1  

print'The number of objects detected by observing the pattern',count_object
print'but by observing the plot we can see that there are only 6 objects'
velo_temp = []
t = []

for y in range(0,len(cr)):
    t.append(y)
ti = [float(i)/10 for i in range(1699)]  
ti_update = []
for x in range(len(readings)):
    if readings[x]>400 and readings[x]<1900 and ti[x]>10 and ti[x]<148:
        velo_temp.append(readings[x])
        ti_update.append(ti[x])
        
        

plt.plot(ti,readings,".")
plt.show()
plt.plot(ti_update,velo_temp,".b")
plt.title("The blue lines indicate presence of the 6 objects")
plt.show()
tem_velocity = []
for x in range(len(velo_temp)):
    if x != 0:
        if(ti_update[x]-ti_update[x-1] < 0.4):
           tem_velocity.append(abs(float(float(velo_temp[x]-velo_temp[x-1]) / 0.1)*0.01))
print 'max velocity is in object:',max(tem_velocity) 

print 'Probability that the reading is object and not wall is: ',(float(len(ti_update))/len(ti))