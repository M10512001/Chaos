# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:07:52 2018

@author: M10512001
"""
import numpy as np

def To3DProjector(xs, ys, zs, ws):
    cdict = {'XYZ':[xs, ys, zs], 'XYW':[xs, ys, ws],
             'XZW':[xs, zs, ws], 'YZW':[ys, zs, ws]}
    for i in ('XYZ', 'XYW', 'XZW', 'YZW'):
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot(cdict[i][0], cdict[i][1], cdict[i][2], lw=0.5)
        dim = list(i)
        ax.set_xlabel(str(dim[0]) +" Axis")
        ax.set_ylabel(str(dim[1]) +" Axis")
        ax.set_zlabel(str(dim[2]) +" Axis")
        name = "Chaos in " +i
        ax.set_title("Chaos in " +i)
#        plt.savefig(name +'.png',dpi=240)

# line 25-34 are Double(default) type, line 21-30 are Float type.
#x = 0.1
#y = 0.1
#z = 0.1
#w = 0.1
#a = 20
#b = 0.5
#c = 6.8
#d = 8
#e = 0.5
#t = 0.01

x = np.float32(0.1)
y = np.float32(0.1)
z = np.float32(0.1)
w = np.float32(0.1)
a = np.float32(20)
b = np.float32(0.5)
c = np.float32(6.8)
d = np.float32(8)
e = np.float32(0.5)
t = np.float32(0.01)

xl = []
yl = []
zl = []
wl = []

xl.append(x)
yl.append(y)
zl.append(z)
wl.append(w)

for i in range(1, 2501, 1):
# line 59-62, 64-68, and 69-92(Altera IP core reuse method) are three way to get the different literations of the same chaos system. 
#    xdot = ( a * ( y - x ) + y * z + w ) * t + x
#    ydot = ( ( b * x + c * y) - ( x * z + e * w ) ) * t + y
#    zdot = ( x * x - d * z ) * t + z
#    wdot = ( x - w ) * t + w

#    xdot = ( - a * x + a * y + y * z + w ) * t + x
#    ydot = ( b * x + c * y - x * z - e * w ) * t + y
#    zdot = ( x * x - d * z ) * t + z
#    wdot = ( x - w ) * t + w

    x11 = y - x
    x12 = y * z
    x21 = a * x11
    x22 = x12 + w
    x31 = x21 + x22
    x32 = x31 * t
    xdot = x32 + x
    y11 = b * x
    y12 = c * y
    y13 = x * z
    y14 = e * w
    y21 = y11 + y12
    y22 = y13 + y14
    y31 = y21 - y22
    y32 = y31 * t
    ydot = y32 + y
    z21 = x * x
    z22 = d * z
    z31 = z21 - z22
    z32 = z31 * t
    zdot = z32 + z
    w31 = x - w
    w32 = w31 * t
    wdot = w32 + w

    xl.append(xdot)
    yl.append(ydot)
    zl.append(zdot)
    wl.append(wdot)
    x = xdot
    y = ydot
    z = zdot
    w = wdot

#To3DProjector(x,y,z,w)

print('Initial Status:')
print('X: %10f' % xl[0])
print('Y: %10f' % yl[0])
print('Z: %10f' % zl[0])
print('W: %10f' % wl[0])
print('Step 1 ~ 10:')
print('X: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (xl[1], xl[2], xl[3], xl[4], xl[5], xl[6], xl[7], xl[8], xl[9], xl[10]))
print('Y: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (yl[1], yl[2], yl[3], yl[4], yl[5], yl[6], yl[7], yl[8], yl[9], yl[10]))
print('Z: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (zl[1], zl[2], zl[3], zl[4], zl[5], zl[6], zl[7], zl[8], zl[9], zl[10]))
print('W: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (wl[1], wl[2], wl[3], wl[4], wl[5], wl[6], wl[7], wl[8], wl[9], wl[10]))
print('Step 101 ~ 110:')
print('X: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (xl[101], xl[102], xl[103], xl[104], xl[105], xl[106], xl[107], xl[108], xl[109], xl[110]))
print('Y: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (yl[101], yl[102], yl[103], yl[104], yl[105], yl[106], yl[107], yl[108], yl[109], yl[110]))
print('Z: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (zl[101], zl[102], zl[103], zl[104], zl[105], zl[106], zl[107], zl[108], zl[109], zl[110]))
print('W: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (wl[101], wl[102], wl[103], wl[104], wl[105], wl[106], wl[107], wl[108], wl[109], wl[110]))
print('Step 301 ~ 310:')
print('X: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (xl[301], xl[302], xl[303], xl[304], xl[305], xl[306], xl[307], xl[308], xl[309], xl[310]))
print('Y: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (yl[301], yl[302], yl[303], yl[304], yl[305], yl[306], yl[307], yl[308], yl[309], yl[310]))
print('Z: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (zl[301], zl[302], zl[303], zl[304], zl[305], zl[306], zl[307], zl[308], zl[309], zl[310]))
print('W: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (wl[301], wl[302], wl[303], wl[304], wl[305], wl[306], wl[307], wl[308], wl[309], wl[310]))
print('Step 701 ~ 710:')
print('X: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (xl[701], xl[702], xl[703], xl[704], xl[705], xl[706], xl[707], xl[708], xl[709], xl[710]))
print('Y: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (yl[701], yl[702], yl[703], yl[704], yl[705], yl[706], yl[707], yl[708], yl[709], yl[710]))
print('Z: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (zl[701], zl[702], zl[703], zl[704], zl[705], zl[706], zl[707], zl[708], zl[709], zl[710]))
print('W: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (wl[701], wl[702], wl[703], wl[704], wl[705], wl[706], wl[707], wl[708], wl[709], wl[710]))
print('Step 1501 ~ 1510:')
print('X: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (xl[1501], xl[1502], xl[1503], xl[1504], xl[1505], xl[1506], xl[1507], xl[1508], xl[1509], xl[1510]))
print('Y: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (yl[1501], yl[1502], yl[1503], yl[1504], yl[1505], yl[1506], yl[1507], yl[1508], yl[1509], yl[1510]))
print('Z: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (zl[1501], zl[1502], zl[1503], zl[1504], zl[1505], zl[1506], zl[1507], zl[1508], zl[1509], zl[1510]))
print('W: %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f, %10f' % (wl[1501], wl[1502], wl[1503], wl[1504], wl[1505], wl[1506], wl[1507], wl[1508], wl[1509], wl[1510]))
