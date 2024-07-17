f = open("file3")
m = int(f.readline())
s = int(f.readline().split()[0])
a = []
b = []
for line in f.readlines():
    ID, EGE, UD, PROT = [int(i) for i in line.split()]
    if PROT == 1 or PROT == 2:
        a.append(EGE + UD)
    b.append(EGE + UD)
sr = sum(b) / len(b)
k = 0
sum_proxod = 0
mx = None
a.sort(reverse=True)
spisok = {}
for ball in a:
    if ball > sr and ball > s:
        k += 1
        sum_proxod += ball
    if k == m:
        break
sr_proxod = round(sum_proxod / m)
for ball in b:
    if ball not in spisok:
        spisok[ball] = 0
    spisok[ball] += 1
for line in spisok:
    if mx is None or spisok[mx] < spisok[line]:
        mx = line
print(sr_proxod, mx)

#306 181