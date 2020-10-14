import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

rays    = 5 # jumlah ray
velo    = np.array([2300, 2250, 2200, 2150, 2100, 2050, 2000, 1950]) # velocity setiap lapisan
# velo    = np.array([2200, 1300, 2100, 1800, 2500, 1450]) # velocity setiap lapisan
dz      = np.array([100, 100, 100, 100, 100, 100, 100, 100]) # ketebalan lapisan
# dz      = np.array([800, 200, 750, 1200, 500, 250]) # ketebalan lapisan
layers  = len(velo)

theta = np.empty(shape = [0, rays])
for i in range(1, rays+1):
    t = i * 10
    theta = np.array([np.append(theta, t)])
print("theta : ",theta)

p = np.empty(shape = [0, rays])
for i in range(rays):
    x = np.sin(np.deg2rad(theta[0, i])) / velo[0] # perhitungan nilai px untuk setiap ray
    p = np.array([np.append(p, x)])

pz = np.empty(shape = [layers, rays])
for j in range(rays):
    for i in range(layers):
        pz[i, j] = np.sqrt((1/(velo[i]))**(2) - (p[0, j])**2) # perhitungan nilai pz setiap ray pada setiap lapisan
print("pz : \n",pz)

dx = np.empty(shape = [layers, rays])
for j in range(rays):
    for i in range(layers):
        dx[i, j] = p[0, j] * dz[i]/ pz[i, j] # perpindahan gelombang pada sumbu offset (x) berdasarkan nilai p dan pz
# print(dx)
a = np.array([np.zeros(rays)])
dx = np.append(a, dx, axis = 0)

for j in range(rays):
    for i in range(1, layers + 1):
        dx[i, j] = dx[i, j] + dx[i - 1, j]
# print(dx)

total_depth = np.sum(dz)
dz = np.append(0, dz)
depth = np.array([np.zeros(len(dz))])
for i in range(1, len(dz)):
    depth[0, 0] = total_depth
    depth[0, i] = total_depth - (np.sum(dz[0:i + 1]))
# print(depth)

fig, ax = plt.subplots()
for i in range(rays):
    ax.plot(dx[:, i], depth[0, :])
ax.set_title("Ray Tracing")
for i in range(len(depth)):
    plt.hlines(depth[i], 0, np.amax(dx), colors='r')
plt.gca().invert_yaxis()
plt.show()