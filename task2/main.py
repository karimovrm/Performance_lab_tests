with open('krug.txt', 'r') as f1:
    krug = f1.read().split()

a, b, r = map(int, krug)

with open('tochka.txt', 'r') as f2:
    for line in f2:
        tochka = line.split(' ')
        for number in tochka:
            x, y = map(int, tochka)

        if (x - a) ** 2 + (y - b) ** 2 < r ** 2:
            print(1, end='\n')
        elif (x - a) ** 2 + (y - b) ** 2 > r ** 2:
            print(2, end='\n')
        else:
            print(0, end='\n')
