import random

for i in range(10):
    a = random.randint(9, 10)
    b = random.random() * 6
    c = random.uniform(4, 10)
    d = random.SystemRandom().uniform(5, 10)
    print(a, round(b, 2), c, d)
