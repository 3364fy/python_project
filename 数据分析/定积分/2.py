from sympy import *
x = symbols('x')

print(integrate(log(x)*E**(-x)))
print(Ei(x))
