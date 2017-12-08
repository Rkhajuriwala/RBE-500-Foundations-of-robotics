import csv
import numpy as np 


readings_2_m_45_lidar=[]
readings_2_m_45_ultra=[]
readings_2_m_lidar=[]
readings_2_m_ultra=[]

with open('Midterm_F17_LIDAR_Ultrasound_100ms_2m_045.csv','rb') as csvfile:
		reader_1= csv.reader(csvfile)
		my_list1 = list(reader_1)
sensor_1_goal = 200/0.7071#cos45 = 0.7071
for b in my_list1:
    x =int(b[0])
    y =int(b[1])
    readings_2_m_45_lidar.append(x)
    readings_2_m_45_ultra.append(y) 

lidar_2_m_45mean = np.mean(readings_2_m_45_lidar)
ultra_2_m_45mean = np.mean(readings_2_m_45_ultra)
lidar_2_m_45stddev= np.std(readings_2_m_45_lidar,ddof = 1)
ultra_2_m_45stddev = np.std(readings_2_m_45_ultra,ddof =1)

bias_2_m_lidar_45=(lidar_2_m_45mean- sensor_1_goal)
bias_2_m_ultra_45= (ultra_2_m_45mean-sensor_1_goal)


Adjust_1_m=[]
lidar_var = np.var(readings_2_m_45_lidar,ddof=1)
ultra_var = np.var(readings_2_m_45_ultra,ddof =1)
w1 = lidar_var/float(lidar_var+ultra_var)
w2 = ultra_var/float(lidar_var+ultra_var)

for x in my_list1:
	w1z1 = w1*(int(x[0])-bias_2_m_lidar_45)
	w2z2 = w2*(int(x[1])-bias_2_m_ultra_45)
	s= w1z1+w2z2
	Adjust_1_m.append(s)

with open('Midterm_F17_LIDAR_Ultrasound_100ms_2m_045_soft.csv','rb') as csvfile:
		reader_2= csv.reader(csvfile)
		my_list2 = list(reader_2)
sensor_2_goal = 200/0.7071
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

print 'Answer 10 Bias for lidar sensor at 45 angle at 2 m range:',bias_2_m_lidar_45
print 'Answer 10 Standard deviation for lidar sensor at 45 angle at 2m range:',lidar_2_m_45stddev
print 'Answer 10 Bias for ultrasound sensor at 45 angle at 2 m range:',bias_2_m_ultra_45
print 'Answer 10 Standard deviation for ultrasound sensor at 45 angle at 2m range:',ultra_2_m_45stddev

print 'Answer 10 Bias for lidar sensor at 45 angle at 2 m range for soft wall:',bias_2_m_lidar
print 'Answer 10 Standard deviation for lidar sensor at 45 angle at 2m range for soft wall:',lidar_2_m_stddev
print 'Answer 10 Bias for ultrasound sensor at 45 angle at 2 m range for soft wall:',bias_2_m_ultra
print 'Answer 10 Standard deviation for ultrasound sensor at 45 angle at 2m range for soft wall:',ultra_2_m_stddev



#print 'Answer  Adjusted array by combing readings of lidar and ultrasound sensors at 2m range:',Adjust_1_m
print 'Answer 10 mean for adjusted array FOR 2m range at 45 angle for hard wall:',np.mean(Adjust_1_m)
print 'Answer 10 Standard deviation for adjusted array for 2 m range at 45 angle for hard wall:',np.std(Adjust_1_m,ddof=1)
#print 'Answer 8c Adjusted array by combing readings of lidar and ultrasound sensors at 2m range:',Adjust_2_m
print 'Answer 10 mean for adjusted array for 2 m range at 45 angle for soft wall:',np.mean(Adjust_2_m)
print 'Answer 10 Standard deviation for adjusted array for 2 m range at 45 angle for soft wall:',np.std(Adjust_2_m,ddof=1)