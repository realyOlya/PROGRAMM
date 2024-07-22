f = open("file1")
s = int(f.readline().split()[0])
a = []
for line in f.readlines():
    ID, EGE, UD = [int(i) for i in line.split()]
    a.append(EGE + UD)
sr = sum(a) / len(a)
beauty = []
smart =[]
for ball in a:
    if ball > sr and ball > s:
        if ball > 50 and ball < 200:
            beauty.append(ball)
        if ball >= 250:
            smart.append(ball)
print(len(beauty))
print(len(smart))