import csv
import numpy as np 


readings_1_m_lidar=[]
readings_1_m_ultra=[]
readings_2_m_lidar=[]
readings_2_m_ultra=[]

with open('Midterm_F17_LIDAR_Ultrasound_100ms_1m_000_soft.csv','rb') as csvfile:
		reader_1= csv.reader(csvfile)
		my_list1 = list(reader_1)
sensor_1_goal = 100
for b in my_list1:
    x =int(b[0])
    y =int(b[1])
    readings_1_m_lidar.append(x)
    readings_1_m_ultra.append(y) 

lidar_1_m_mean = np.mean(readings_1_m_lidar)
ultra_1_m_mean = np.mean(readings_1_m_ultra)
lidar_1_m_stddev= np.std(readings_1_m_lidar,ddof = 1)
ultra_1_m_stddev = np.std(readings_1_m_ultra,ddof =1)

bias_1_m_lidar=(lidar_1_m_mean- sensor_1_goal)
bias_1_m_ultra= (ultra_1_m_mean-sensor_1_goal)


Adjust_1_m=[]
lidar_var = np.var(readings_1_m_lidar,ddof=1)
ultra_var = np.var(readings_1_m_ultra,ddof =1)
w1 = lidar_var/float(lidar_var+ultra_var)
w2 = ultra_var/float(lidar_var+ultra_var)

for x in my_list1:
	w1z1 = w1*(int(x[0])-bias_1_m_lidar)
	w2z2 = w2*(int(x[1])-bias_1_m_ultra)
	s= w1z1+w2z2
	Adjust_1_m.append(s)

with open('Midterm_F17_LIDAR_Ultrasound_100ms_2m_000_soft.csv','rb') as csvfile:
		reader_2= csv.reader(csvfile)
		my_list2 = list(reader_2)
sensor_2_goal = 200
for b in my_list2:
    x =int(b[0])
    y =int(b[1])
    readings_2_m_lidar.append(x)
    readings_2_m_ultra.append(y) 

lidar_2_m_mean = np.mean(readings_2_m_lidar)
ultra_2_m_mean = np.mean(readings_2_m_ultra)
lidar_2_m_stddev= np.std(readings_2_m_lidar,ddof = 1)
ultra_2_m_stddev = np.std(readings_2_m_ultra,ddof =1)

bias_2_m_lidar=(lidar_2_m_mean- sensor_2_goal)
bias_2_m_ultra= (ultra_2_m_mean-sensor_2_goal)

Adjust_2_m=[]
lidar_var_2 = np.var(readings_2_m_lidar,ddof=1)
ultra_var_2 = np.var(readings_2_m_ultra,ddof =1)
w1 = lidar_var_2/float(lidar_var_2+ultra_var_2)
w2 = ultra_var_2/float(lidar_var_2+ultra_var_2)

for x in my_list2:
	w1z1 = w1*(int(x[0])-bias_2_m_lidar)
	w2z2 = w2*(int(x[1])-bias_2_m_ultra)
	s= w1z1+w2z2
	Adjust_2_m.append(s)

print 'Answer 9a Bias for lidar sensor at 1 m range:',bias_1_m_lidar
print 'Answer 9a Bias for lidar sensor at 2 m range:',bias_2_m_lidar
print 'Answer 9a Standard deviation for lidar sensor at 1m range:',lidar_1_m_stddev
print 'Answer 9a Standard deviation for lidar sensor at 2m range:',lidar_2_m_stddev

print 'Answer 9b Bias for ultrasound sensor at 1 m range:',bias_1_m_ultra
print 'Answer 9b Bias for ultrasound sensor at 2 m range:',bias_2_m_ultra
print 'Answer 9b Standard deviation for ultrasound sensor at 1m range:',ultra_1_m_stddev
print 'Answer 9b Standard deviation for ultrasound sensor at 2m range:',ultra_2_m_stddev

#print 'Answer 8c Adjusted array by combing readings of lidar and ultrasound sensors at 1m range:',Adjust_1_m
print 'Answer 9c mean for combined readings for 1 m range:',np.mean(Adjust_1_m)
print 'Answer 9c Standard deviation for combined readings for 1 m range:',np.std(Adjust_1_m,ddof=0)
#print 'Answer 8c Adjusted array by combing readings of lidar and ultrasound sensors at 2m range:',Adjust_2_m
print 'Answer 9c mean for combined readings for 2 m range:',np.mean(Adjust_2_m)
print 'Answer 9c Standard deviation for combined readings for 2 m range:',np.std(Adjust_2_m,ddof=0)