import random

list = [random.randint(0,80) for i in range(random.randint(10,15))]
max = list[0]
a = 0
while a + 2 < len(list):
    if(list[a] + list[a + 1]+list[a + 2] > max):
        max = list[a] + list[a + 1] + list[a + 2]
    a = a + 1
list.append(max)
print(list)