n = int(input())
a = []
for r in range(1, n+1):
    for t in range(1, n+1):
        if n % (r+t) == 0 and r < t:
            a.append(r)
            a.append(t)
print(*a, sep="")


p = int(input())
g = []
for a in range(1, p+1):
    for b in range(1, p+1):
        if p % (a+b) == 0 and a < b:
          g.append(a)
          g.append(b)
print(*g, sep="")
