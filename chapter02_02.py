# 파이썬 변수

n = 700

print(n)
print(type(n))

#동시 선언
x = y = z = 500
print(x, y, z)

var = 75
var = "Change Value"

print(var)
print(type(var))

m = 300
n = 900
print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m = 900
print(id(m) == id(n))