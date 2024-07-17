f = open("file1")
s = int(f.readline().split()[0])
a = []
for line in f.readlines():
    ID, EGE, UD = [int(i) for i in line.split()]
    a.append(EGE + UD)
sr = sum(a) / len(a)
k = 0
mx = None
spisok = {}
for ball in a:
    if ball > sr and ball > s:
        k += 1
    if ball not in spisok:
        spisok[ball] = 0
    spisok[ball] += 1
for line in spisok:
    if mx is None or spisok[mx] < spisok[line]:
        mx = line
print(k, mx)


#2653 266