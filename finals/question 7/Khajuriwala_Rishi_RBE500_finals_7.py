import numpy as np

fb = [3.351797405,1.599123929,-9.069082468]
# print(fb)
sf = -fb[1]/np.sqrt(fb[1]**2+fb[2]**2)
# print(sf)
cf = -fb[2]/np.sqrt(fb[1]**2+fb[2]**2)
# print(cf)
g = np.sqrt(fb[0]**2+fb[1]**2+fb[2]**2)

st = fb[0]/g
# print(st)
ct = -(sf*fb[1]+cf*fb[2])/g
# print(ct)
sa = 0
ca = 1
c_nb = [(ct*ca),(ct*sa),-(st),
        (sf*st*ca)-(cf*sa),(sf*st*sa)+(cf*ca),(sf*ct),
        (cf*st*ca)+(sf*sa),(cf*st*sa)-(sf*ca),(cf*ct)]
c_n_b =np.reshape(c_nb,(3,3))
# print(c_b_n)

print'7-A The Direction Cosine Matrix C:\n',(c_n_b)

c_b_n = np.transpose(c_n_b)

print'7-B the Cbn matrix:\n',(c_b_n)

ca_2 = 1
sa_2 = 0
ct_2 = np.sqrt((1+ct)/2)
st_2 = st /(2*ct_2)
cf_2 = np.sqrt((1+cf)/2)
sf_2 = sf /(2*cf_2)

q_nb =[(ca_2*ct_2*cf_2)+(sa_2*st_2*sf_2),
        (ca_2*ct_2*sf_2)-(sa_2*st_2*cf_2),
        (ca_2*st_2*cf_2)+(sa_2*ct_2*sf_2),
        (sa_2*ct_2*cf_2)-(ca_2*st_2*sf_2)]
q_n_b = np.reshape(q_nb,(4,1))

q = q_n_b * np.reshape(np.transpose([1,-1,-1,-1]),(4,1))
print'7-C The conjugate quaternion:\n',(q)

Cq = [((q[0]**2)+(q[1]**2)-(q[2]**2)-(q[3]**2)),(2*((q[1]*q[2])+(q[0]*q[3]))),(2*(q[1]*q[3])-(q[0]*q[2])),
      (2*((q[1]*q[2])-(q[0]*q[3]))),((q[0]**2)-(q[1]**2)+(q[2]**2)-(q[3]**2)),(2*((q[2]*q[3])+(q[0]*q[1]))),
      (2*((q[1]*q[3])-(q[0]*q[2]))),(2*((q[2]*q[3])-(q[0]*q[1]))),((q[0]**2)-(q[1]**2)-(q[2]**2)+(q[3]**2))]

print(np.shape(Cq))
Cq = np.reshape(Cq, (3,3))
print'7-D quaternion to a Direction cosine matrix:\n',(Cq)
