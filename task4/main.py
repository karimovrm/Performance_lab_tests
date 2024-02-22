import math

with open('elements.txt', 'r') as f:
    elements = [int(i) for i in f.read().split()]
    # print(elements)

# m = round(sum(elements)/len(elements))

m = sorted(elements)[len(elements) // 2]
n = sum(abs(v - m) for v in elements)
print(n)