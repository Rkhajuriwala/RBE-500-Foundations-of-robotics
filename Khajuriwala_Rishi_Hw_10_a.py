import csv
import numpy as np
import matplotlib.pyplot as plt
import math

readings =[]
with open('RBE500-F17-100ms-Constant-Vel.csv', 'r') as g:               ##reading from CSV file
  reader = csv.reader(g)
  for row in reader:
      readings.append(float(row[0]))
readings = np.array(readings)
time = [i/10 for i in range(len(readings))]


stdx = []#standard deviation
stdv = []
cor= []
new_measurements = []

position=[]
velocity=[]

X = np.array([2530,-10]).reshape(2,1)
A = np.array([1,0.1,0,1]).reshape(2,2)
R = np.array([0.1,1,1,10]).reshape(2,2)
P = np.array([100,0,0,100]).reshape(2,2)
H = np.array([1,0]).reshape(1,2)
Q = 10
I = np.array([1,0,0,1]).reshape(2,2)
A_trans = np.transpose(A)
H_trans = np.transpose(H)
for i in readings:
    # state matrix prediction
    x_kp = np.matmul(A,X)
    # covariance matrix
    p_kp = np.matmul((np.matmul(A,P)),A_trans) + R
    # Kalman Gain
    K_g = (np.matmul(p_kp,H_trans)/(np.matmul((np.matmul(H,p_kp)),H_trans) + Q))
    K_gain = np.reshape(K_g,(2,1))
    X = x_kp + K_gain*(i-np.matmul(H,x_kp))
    P = np.matmul((np.identity(2) - np.matmul(K_gain,H)),p_kp)
    stdx.append(math.sqrt(P[0,0]))
    stdv.append(math.sqrt(P[1,1]))
    cor.append(P[0,1] / ((math.sqrt(P[0,0])) * (math.sqrt(P[1,1]))))
    position.append(X[0])
    velocity.append(X[1])





plt.plot(time,position, label = 'Estimated Position')
plt.plot(time,readings, label = 'Raw data')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Positon')
plt.title('Raw data and the estimated position')
plt.show()

plt.plot(time,velocity, label = 'Estimated Velocity')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.title('Velocity')
plt.show()

plt.plot(time,stdx, label = 'Standard Deviation in Position')
plt.plot(time,stdv, label = 'Standard Deviation in Velocity')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Standard Deviation')
plt.title('Standard deviations of position and velocity ')
plt.show()

plt.plot(time,cor, label = 'Correlation coefficient')
plt.legend()
plt.xlabel('Time in sec')
plt.ylabel('Correlation coefficient')
plt.title('Correlation coefficient')
plt.show()
