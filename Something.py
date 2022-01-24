import random
a = 1
for i in range(1000):
    a = random.randrange(1,100) * a

print(a)
