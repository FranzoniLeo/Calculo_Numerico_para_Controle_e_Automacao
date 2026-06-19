import numpy as np

v0 = 4
theta = (33.8 * np.pi) / 180
h0 = 1
dt = 0.01
g = 9.81

tf = ((v0 * np.sin(theta)) + ((v0 * np.sin(theta))**2 + (2*g*h0))**(1/2)) / (g)
#print(tf)

# numero de iteracoes
n = int(tf // dt)
print(n)

def func (t, v0 = v0, theta = theta, h0 = h0, g = g):
    return ((v0 * np.cos(theta))**2 + (v0 * np.sin(theta) - g*t)**2)**(1/2)


# integral numerica pelo metodo trapezoidal
L = 0
for i in range(n):
    L = L + ((func(i*dt) +  func((i+1)*dt))* dt/2)

print(" ----------------- metodo trapezoidal ----------------- ")
print(L)


# integral numerica pelo metodo de simpson
L = 0 
h = dt/2
for j in range(n):
    y = ((j*dt) + ((j+1)*dt))/2
    L = L + (h/3)*(func(j*dt) + 4*func(y) + func((j+1)*dt))

print(" ----------------- metodo de simpson ----------------- ")
print(L)
 
