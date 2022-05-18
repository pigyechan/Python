a = list()
for i in range(0,9):
    a.append(int(input()))

maxe = max(a)
print(maxe)
print(a.index(maxe)+1)
