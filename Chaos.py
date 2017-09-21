# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:31:58 2017

@author: M10512001
"""
import binascii as bas
import matplotlib.pyplot as plt
import numpy as np
import time
import math

def ElementAnalysis(name1, name2):
    print(time.asctime(time.localtime(time.time())))
    frb = open(name1 +'.' +name2, 'rb')
    data = frb.read()
    ddict = {}
    for i in range(len(data)):
        obj=data[i:i+1]
        if obj in ddict:
            ddict[obj]+=1
        else:
            ddict[obj]=1
    plt.figure(figsize=(80,8))
    plt.bar(range(len(ddict.keys())), list(ddict.values()))
    plt.xticks(range(len(ddict.keys())), list(ddict.keys()), rotation=40)
    plt.savefig(name1 +'_Analysis.png', dpi=240)

def ChaosFunction(x, y, z, w, a=20, b=0.5, c=6.8, d=8, e=0.5):
    x_dot = -a*x +a*y +y*z +w
    y_dot = b*x +c*y -x*z -e*w 
    z_dot = x*x -d*z
    w_dot = x -w
    return x_dot, y_dot, z_dot, w_dot

def ChaosGenerator(stepCnt, dt):
    xs = np.empty((stepCnt +1,))
    ys = np.empty((stepCnt +1,))
    zs = np.empty((stepCnt +1,))
    ws = np.empty((stepCnt +1,))
    xs[0], ys[0], zs[0], ws[0] = (0.1, 0.1, 0.1, 0.1)
    for i in range(stepCnt):
        x_dot, y_dot, z_dot, w_dot = ChaosFunction(xs[i], ys[i], zs[i], ws[i])
        xs[i +1] = xs[i] +(x_dot *dt)
        ys[i +1] = ys[i] +(y_dot *dt)
        zs[i +1] = zs[i] +(z_dot *dt)
        ws[i +1] = ws[i] +(w_dot *dt)
    return xs, ys, zs, ws

def To3DProjector(xs, ys, zs, ws):
    cdict = {'XYZ':[xs, ys, zs], 'XYW':[xs, ys, ws],
             'XZW':[xs, zs, ws], 'YZW':[ys, zs, ws]}
    for i in ('XYZ', 'XYW', 'XZW', 'YZW'):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(cdict[i][0], cdict[i][1], cdict[i][2], lw=0.5)
        dim = list(i)
        ax.set_xlabel(str(dim[0]) +" Axis")
        ax.set_ylabel(str(dim[1]) +" Axis")
        ax.set_zlabel(str(dim[2]) +" Axis")
        name = "Chaos in " +i
        ax.set_title("Chaos in " +i)
        plt.savefig(name +'.png',dpi=240)
        
def Cypher(name1, name2):
    frb = open(name1 +'.' +name2, 'rb')
    ptext = list(frb.read())
    pair = int((len(ptext) -54))
    x, y, z, w = ChaosGenerator(pair,0.01)
    xs = (np.floor(x *100) %256)
    ys = (np.floor(y *100) %256)
    zs = (np.floor(z *100) %256)
    ws = (np.floor(w *100) %256)
#    print(ptext[100:150])
    for i in range(pair):
        if ((pair%4)==0):
            ptext[i+54] = ptext[i+54]^int(xs[i])
        elif ((pair%4)==1):
            ptext[i+54] = ptext[i+54]^int(ys[i])
        elif ((pair%4)==2):
            ptext[i+54] = ptext[i+54]^int(zs[i])
        elif ((pair%4)==3):
            ptext[i+54] = ptext[i+54]^int(ws[i])
    ctext = open(name1 +'_cyphered.' +name2, 'wb')
#    print(ptext[100:150])
    ctext.write(bytearray(list(ptext)))
    ctext.close

def Decyp(name1, name2):
    frb = open(name1 +'.' +name2, 'rb')
    ptext = list(frb.read())
    pair = int((len(ptext) -54))
    x, y, z, w = ChaosGenerator(pair,0.01)
    xs = (np.floor(x *100) %256)
    ys = (np.floor(y *100) %256)
    zs = (np.floor(z *100) %256)
    ws = (np.floor(w *100) %256)
#    print(ptext[100:150])
    for i in range(pair):
        if ((pair%4)==0):
            ptext[i+54] = ptext[i+54]^int(xs[i])
        elif ((pair%4)==1):
            ptext[i+54] = ptext[i+54]^int(ys[i])
        elif ((pair%4)==2):
            ptext[i+54] = ptext[i+54]^int(zs[i])
        elif ((pair%4)==3):
            ptext[i+54] = ptext[i+54]^int(ws[i])
    ctext = open(name1 +'_decyped.' +name2, 'wb')
#    print(ptext[100:150])
    ctext.write(bytearray(list(ptext)))
    ctext.close

x,y,z,w=ChaosGenerator(10000,0.01)
print((np.floor(x*10)%10)[0]==1)
#To3DProjector(x,y,z,w)
Cypher('lena', 'bmp')
ElementAnalysis('lena_cyphered', 'bmp')
Decyp('lena_cyphered', 'bmp')
