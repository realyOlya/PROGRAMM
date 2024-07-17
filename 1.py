from random import randint

f = open("file3", "w")
for i in range(1, 9999):
    text = str(i) + " " + str(randint(100, 300)) + " " + str(randint(0, 10)) + " " +str(randint(1, 4)) + "\n"
    print(text)
    f.write(text)
