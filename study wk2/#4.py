a = int(input())
b = input().split(" ")
c = list()
for i in range(0, a):
    c.append(int(b[i]))
print(min(c), max(c))
