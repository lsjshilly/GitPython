import numpy as np
import matplotlib.pyplot as plt
from vmdpy import VMD
from numpy import pi as pi

L = 1000
Fs = 1000
t = np.arange(1, L+1)/Fs
freqs = np.arange(-L/2, L/2)*(Fs/L)

v_1 = np.cos(2*pi*2*t)
v_2 = 1/4*np.cos(2*pi*24*t)
v_3 = 1/16*np.cos(2*pi*288*t)

f = v_1+v_2+v_3+0.1*np.random.randn(v_1.size)

alpha = 2000
tau = 0
K = 4
DC = 0
init = 1
tol = 1e-7

u, u_hat, omega = VMD(f, alpha, tau, K, DC, init, tol)

plt.figure()
plt.plot(t, v_1)
plt.figure()
plt.plot(t, v_2)
plt.figure()
plt.plot(t, v_3)
for k in range(K):
    plt.figure()
    plt.plot(t,u[k,:])

plt.show()


