
from __future__ import print_function, division

import controlpy

import numpy as np

lx = 0.188;
ly = 0.135;
lab = lx+ly;
t = 0.1; 

# A B matrix:
A = np.matrix([[1,0,0],[0,1,0],[0,0,1]])
B = np.matrix([[t*lab,t*lab,t*lab,t*lab],[t*lab,-t*lab,t*lab,-t*lab],[t,-t,-t,t]])

# Define initial costs:
Q = np.matrix([[1,0,0],[0,1,0],[0,0,1]])
R = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

# Compute the LQR controller
gain, X, closedLoopEigVals = controlpy.synthesis.controller_lqr(A,B,Q,R)

print('The computed gain is:')
print(gain)

print('The closed loop eigenvalues are:')
print(closedLoopEigVals)





