# y^2 = x^3  + 31988x + 1000

A = 31988
B = 1000
x0 = 0
y0 = 5585
p = 31991
n = 32089
points = [[0, 5585], [0, 5585]]

print(points)
def check(p, y, x, A, B):
    if (pow(y, 2, 31991) == x ** 3 + A * x + 1000) and ((4 * pow(A, 3) + 27 * pow(B, 2)) % p != 0):
        return True
    else:
        return False

# P = P
def P():
    for i in range(1, 3): # 32089
        P1 = points[i -1]
        P2 = points[i]
        if P1 == P2:
            lam = ((3 * pow(P1[0], 2) + A) / (2 * P1[1])) % p
            x3 = round((pow(lam, 2) - 2 * P1[0]) % p)
            y3 = round((y0 + lam * (x3 - P1[0])) % p)
            #if check(p, y3, x3, A, B ) == True: #по этому условию не проходит, не принадлежит прямой
            points.append([x3, y3])
        elif points[i] != points[i - 1]:
            lam = round(((P2[1] -P1[1]) / (P2[0] - P1[0])) % p)
            x3 = lam ** 2 - P1[0] - P2[0] % p # тут p относится ко всему выражению или нет?
            y3 = P1[1] + (lam * (x3 - P1[0])) % p
            # if check(p, y3, x3, A, B ) == True: #по этому условию не проходит, не принадлежит прямой
            points.append([x3, y3])
        elif P([]): # не понял
            ...



def func():
    lam = ((3 * pow(x0, 2) + A) / (2 * y0)) % p
    x = (pow(lam, 2) - 2 * x0) % p
    y = (y0 + lam * (x - x0)) % p
    return [x, y]
P()
print(type(points[0][0]))
print(points)



