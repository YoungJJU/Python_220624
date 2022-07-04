a = int(input())
b = input()
c = []
d = len(b)

for x in range(d):
    c.append(int(b[x]))

c.reverse()

for y in range(d):
    print(a*c[y])
print(a*int(b))
