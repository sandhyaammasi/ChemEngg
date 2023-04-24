'''from sympy import * 
x = symbols('x') 
expr=x**2 + x + 1 
print(integrate(expr, x))'''

'''from scipy.integrate import quad

def integran(x):
    return x**2

lower_limit = 0
upper_limit = 1

result, error = quad(integran, lower_limit, upper_limit)

print("The result of integration is:", result)'''

from scipy.integrate import quad

def integrand(x):
    return x

x = 1.03
lower_limit = x
upper_limit = 298.15

result, error = quad(integrand, lower_limit, upper_limit)

print("The result of integration is:", result)