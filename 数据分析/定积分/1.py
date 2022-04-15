from sympy import *
x = symbols('x')
print(integrate((sin(x))**4, (x, 0, pi/2)))

print(integrate((sin(x))**4))

print(integrate(log(x)))

print(integrate((1/2)**x,(x,0,1)))