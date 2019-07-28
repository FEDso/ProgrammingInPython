import sys

def discriminant(a, b, c):
    return b**2 - 4*a*c

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
D = discriminant(a, b, c)
print(int((-b + D**0.5)/2*a))
print(int((-b - D**0.5)/2*a))
