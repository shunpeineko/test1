import matplotlib.pyplot as plt
import sys
import streamlit as st
from colorsys import hsv_to_rgb

x0 = st.text_input("x=")
y0 = st.text_input("y=")
z0 = st.text_input("倍率=",1)
mj0 = st.radio(label="選んでください",
                 options=("Mandel","Julia"),
                 horizontal=True)

cL = []
maxn = 100

def mandel(a,b):
    a0,b0 = a,b
    i = 0
    while a**2+b**2 <= 4 and i < maxn:
        #print(i,a,b)
        a2 = a*a - b*b + a0
        b2 = a*b*2 + b0
        a,b = a2,b2
        i += 1
    return i

def julia(x0, y0, cx,cy,maxn=100):
    x, y = x0, y0
    for n in range(maxn):
        if x*x + y*y > 4.0: break
        x, y = x*x-y*y, 2*x*y
        x += cx
        y += cy
    return n+1

nn = 500
size = 4

if mj0 == "Julia":
    cx0 = float(st.text_input("cx=",0))
    cy0 = float(st.text_input("cy=",0))

if st.button("calc"):
    xc = float(x0) if x0 else 0
    yc = float(y0) if y0 else 0
    size /= float(z0)
    xlow = xc-size/2
    ylow = yc-size/2
    dx = size/nn
    dy = size/nn
    D = []
    xL = []
    yL = []

    for i in range(nn):
        y0 = ylow + dy*i
        for j in range(nn):
            x0 = xlow + dx*j
            if mj0 == "Mandel":
                r = mandel(x0,y0)
            else:
                r = julia(x0,y0,cx0,cy0,maxn)
            if r == maxn:
                xL.append(x0)
                yL.append(y0)
                cL.append("black")
            else:
                mandeljulia2 = min((r+0.25)*10/256,1+0.25)
                xL.append(x0)
                yL.append(y0)
                cL.append((hsv_to_rgb(mandeljulia2,1,1)))

    st.write(f""" # {mj0}""")
    plt.scatter(xL,yL,c = cL,marker = "o",s = 0.5)
    #plt.title(mj0)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    st.pyplot(plt)
