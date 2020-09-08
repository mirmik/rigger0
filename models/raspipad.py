#!/usr/bin/env python3

from zencad import *

T = 2

m = box(65+2*T, 30+2*T, 5, center=True)
m += (box(65+2*T+8, 30+2*T, 1, center=True) - box(65+8, 30, 1, center=True)).down(2)
m += (box(65+2*T, 30+2*T+8, 1, center=True) - box(65, 30+8, 1, center=True)).down(2)

m -= sqrmirror()(cylinder(r=2.7/2,h=5, center=True).move(+65/2-4, 30/2-4))

to_stl(m, "raspipad.stl", 0.01)
disp(m)
show()