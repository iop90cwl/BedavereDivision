
loop = 0

n = 100
d = 775

while loop <= 1000:
    n1 = str(n)
    n1 = n1[:2]
    n1 = float(n1)
    d1 = str(d)
    d1 = d1[-2:]
    d1 = float(d1)

    if d == 0:
        n = n
    elif d1 == 0:
        n = n
    elif d / n == 1:
        n = n
    elif float(n) / float(d) == n1 / d1:
        n = int(n)
        d = int(d)
        n1 = int(n1)
        d1 = int(d1)
        print(''+`n`+' / '+`d`+' = '+`n1`+' / '+`d1`)

    n = n + 1
    loop = loop + 1