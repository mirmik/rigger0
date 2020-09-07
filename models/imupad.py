#!/usr/bin/env python3

from zencad import *

I_XY = 25.6 
T = 2

m = box(I_XY+2*T, I_XY+2*T, 5, center=True)
m += (box(I_XY+2*T+8, I_XY+2*T, 1, center=True) - box(I_XY+8, I_XY, 1, center=True)).down(2)
m += (box(I_XY+2*T, I_XY+2*T+8, 1, center=True) - box(I_XY, I_XY+8, 1, center=True)).down(2)

m -= sqrmirror()(cylinder(r=1.8/2,h=5, center=True).move(-I_XY/2, I_XY/2))

to_stl(m, "imupad.stl", 0.01)
disp(m)
show()