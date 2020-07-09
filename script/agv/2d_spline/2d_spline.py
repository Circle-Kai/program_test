#! /bin/usr/python3
from numpy import genfromtxt
map_data = genfromtxt('/home/kai/Scripts/agv/create_a_map/map/map.csv', delimiter=',')
from pycubicspline import * 
import matplotlib.pyplot as plt
x = map_data[:,0]
qy = map_data[:,1]

sp = Spline2D(x, y)
s = np.arange(0, sp.s[-1], 0.01)

rx, ry, ryaw, rk = [], [], [], []
for i_s in s:
  ix, iy = sp.calc_position(i_s)
  rx.append(ix)
  ry.append(iy)
  ryaw.append(sp.calc_yaw(i_s))
  rk.append(sp.calc_curvature(i_s))
# # CSV #  #
import csv
with open('/home/kai/Scripts/agv/create_a_map/map/2d_spline_map.csv', 'w', newline='') as csvfile:
    csv_file = csv.writer(csvfile)
    for i in range(len(rx)):
        csv_file.writerow([rx[i], ry[i]])

flg, ax = plt.subplots(1)
plt.plot(x, y, "xb", label="input")
plt.plot(rx, ry, "-r", label="spline")
plt.grid(True)
plt.axis("equal")
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()

flg, ax = plt.subplots(1)
plt.plot(s, [math.degrees(iyaw) for iyaw in ryaw], "-r", label="yaw")
plt.grid(True)
plt.legend()
plt.xlabel("line length[m]")
plt.ylabel("yaw angle[deg]")

flg, ax = plt.subplots(1)
plt.plot(s, rk, "-r", label="curvature")
plt.grid(True)
plt.legend()
plt.xlabel("line length[m]")
plt.ylabel("curvature [1/m]")

plt.show()
