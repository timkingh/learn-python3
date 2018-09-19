from sympy import *
Cf = Matrix([[1,1,1,1], [2,1,-1,-2], [1,-1,-1,1], [1,-2,2,-1]])
print(Cf)
print(Cf.T)

x00,x01,x02,x03 = symbols('x00 x01 x02 x03')
x10,x11,x12,x13 = symbols('x10 x11 x12 x13')
x20,x21,x22,x23 = symbols('x20 x21 x22 x23')
x30,x31,x32,x33 = symbols('x30 x31 x32 x33')

X = Matrix([
[x00,x01,x02,x03],
[x10,x11,x12,x13],
[x20,x21,x22,x23],
[x30,x31,x32,x33]
])

Y = Cf*X*Cf.T

for i in range(0,16):
    print(Y[i])
    print('\n')



