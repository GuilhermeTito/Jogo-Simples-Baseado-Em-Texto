import personagens as p
import random

random.seed()

num = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

i = 0
while i < 6:
    num[i]=random.random()
    print(num[i])
    i += 1