import itertools as its

words = "1234567890"
r = its.product(words, repeat=3)

for i in r:
    print(i)
