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
        if ball > 190 and ball < 250:
            beauty.append(ball)
        if ball >= 250:
            smart.append(ball)
k_beauty = len(beauty)
k_smart = round(k_beauty * 0.8) # 1023.2 - 80 %, максимально возможное получается 1023
smart.sort(reverse=True)
proxod_smart = smart[k_smart - 1]
print(k_beauty, proxod_smart)



#1279 268