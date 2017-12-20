import pandas
import numpy as np
from math import sqrt
reading_m = pandas.read_csv('Master.csv',header = 1)
master= reading_m.values
reading_r_1 = pandas.read_csv('Rover_1.csv',header = 1)
rover_1= reading_r_1.values
reading_r_2 = pandas.read_csv('Rover_2.csv',header = 1)
rover_2= reading_r_2.values

def data(a):
	b= []
	for x in a:
		degrees_whole = int(x/100)
		min = x - (degrees_whole*100)
		degrees =b.append (degrees_whole + (min/60))
	mean = np.mean(b)
	return mean

master_latitude = data(master[:,1])
master_longitude = data(master[:,3])
rover_1_latitude = data(rover_1[:,1])
rover_1_longitude = data(rover_1[:,3])
rover_2_latitude = data(rover_2[:,1])
rover_2_longitude = data(rover_2[:,3])

print'5-A The average location of master',(master_latitude),'N',(master_longitude),'W'
print'5-A The average location of Rover 1',(rover_1_latitude),'N',(rover_1_longitude),'W'
print'5-A The average location of Rover 2',(rover_2_latitude),'N',(rover_2_longitude),'W'

master_latitude_meters= 111073.9415780662
master_longitude_meters=82804.80196213457
rover_1_latitude_meters=111073.94016983348
rover_1_longitude_meters=82804.89609216161
rover_2_latitude_meters=111073.93847293993
rover_2_longitude_meters=82805.00951690557

# master_latitude_error = master[:,1]-master_latitude
# master_longitude_error= master[:,3]-master_longitude
#
# rover_1_latitude_error = rover_1[:,1]-rover_1_latitude
# rover_1_longitude_error = rover_1[:,3]-rover_1_longitude
#
# rover_2_latitude_error = rover_2[:,1]-rover_2_latitude
# rover_2_longitude_error = rover_2[:,3]-rover_2_longitude

def std(reading,mean,conversion):
	q = []
	for x in reading:
		degrees_whole = int(x/100)
		min = x -(degrees_whole*100)
		degrees = (degrees_whole + (min/60))
		error = degrees - mean
		error_conversion = q.append(error * conversion)
		std_dev = np.std(q)
	return std_dev


stddev_master_error_latitude = std(master[:,1],master_latitude,master_latitude_meters)
stddev_master_error_longitude = std(master[:,3],master_longitude,master_longitude_meters)
stddev_rover_1_error_latitude = std(rover_1[:,1],rover_1_latitude,rover_1_latitude_meters)
stddev_rover_1_error_longitude = std(rover_1[:,3],rover_1_longitude,rover_1_longitude_meters)
stddev_rover_2_error_latitude = std(rover_2[:,1],rover_2_latitude,rover_2_latitude_meters)
stddev_rover_2_error_longitude = std(rover_2[:,3],rover_2_longitude,rover_2_longitude_meters)


print'5-B The Standard Deviation of errors in master',(stddev_master_error_latitude),'-->(latitude)',(stddev_master_error_longitude),'-->(longitude)'
print'5-B The Standard Deviation of errors in rover_1',(stddev_rover_1_error_latitude),'-->(latitude)',(stddev_rover_1_error_longitude),'-->(longitude)'
print'5-B The Standard Deviation of errors in rover_2',(stddev_rover_2_error_latitude),'-->(latitude)',(stddev_rover_2_error_longitude),'-->(longitude)'



master_latitude_conv = master_latitude * master_latitude_meters
master_longitude_conv = master_longitude * master_longitude_meters
rover_1_latitude_conv = rover_1_latitude * rover_1_latitude_meters
rover_1_longitude_conv = rover_1_longitude * rover_1_longitude_meters
rover_2_latitude_conv = rover_2_latitude * rover_2_latitude_meters
rover_2_longitude_conv = rover_2_longitude * rover_2_longitude_meters
# print(master_latitude_conv)
# print(rover_1_latitude_conv)
# print(master_longitude_conv)
# print(rover_1_longitude_conv)
def distance(x1,y1,x2,y2):
	d = np.sqrt((x1-x2)**2 + (y1-y2)**2)
	return d


print '5-C the distance between Master and Rover 1',(distance(master_latitude_conv,master_longitude_conv,rover_1_latitude_conv,rover_1_longitude_conv))
print '5-C the distance between Master and Rover 2',(distance(master_latitude_conv,master_longitude_conv,rover_2_latitude_conv,rover_2_longitude_conv))

def error_conversion(reading,mean,conversion):
	q = []
	for x in reading:
		degrees_whole = int(x/100)
		min = x -(degrees_whole*100)
		degrees = (degrees_whole + (min/60))
		error = degrees - mean
		error_conversion = q.append(error * conversion)

	return q



master_latitude_error  = error_conversion(master[:,1],master_latitude,master_latitude_meters)
master_longitude_error = error_conversion(master[:,3],master_longitude,master_longitude_meters)
rover_1_latitude_error = error_conversion(rover_1[:,1],rover_1_latitude,rover_1_latitude_meters)
rover_1_longitude_error = error_conversion(rover_1[:,3],rover_1_longitude,rover_2_longitude_meters)
rover_2_latitude_error = error_conversion(rover_2[:,1],rover_2_latitude,rover_2_latitude_meters)
rover_2_longitude_error = error_conversion(rover_2[:,3],rover_2_longitude,rover_2_longitude_meters)
m_1_error_la= master_latitude_error[0:920]
m_1_error_lo = master_longitude_error[0:920]
m_2_error_la = master_latitude_error[1093:1740]
m_2_error_lo = master_longitude_error[1093:1740]
r_1_error_la = rover_1_latitude_error[11:len(rover_1_latitude_error)]
r_1_error_lo = rover_1_longitude_error[11:len(rover_1_longitude_error)]


R1_m_latitude = [a - b for a,b in zip(r_1_error_la,m_1_error_la)]
R1_m_longitude = [a - b for a,b in zip(r_1_error_lo,m_1_error_lo)]
R2_m_longitude =[a - b for a,b in zip(rover_2_longitude_error,m_2_error_lo)]
R2_m_latitude = [a - b for a,b in zip(rover_2_latitude_error,m_2_error_la)]

R1_m_latitude_std = np.std(R1_m_latitude)
R1_m_longitude_std = np.std(R1_m_longitude)

R2_m_latitude_std = np.std(R2_m_latitude)
R2_m_longitude_std = np.std(R2_m_longitude)

print'5-D The Standard deviation after subtraction from rover 1 and master:',(R1_m_latitude_std),'-->latitude',(R1_m_longitude_std),'-->longitude'
print'5-D The Standard Deviation after substraction from rover 2 and master:',(R2_m_latitude_std),'-->latitude',(R2_m_longitude_std),'-->longitude'
