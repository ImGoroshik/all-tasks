import random

list = [random.randint(3, 15) for j in range(random.randint(3, 15))]

summ = 0
a = 0
for a in range(len(list)):
 if list[a] % 3 == 0 and list[a] % 2 == 1:
  summ = list[a]
print(list)
print(summ)
