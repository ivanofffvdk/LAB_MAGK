
import matplotlib.pyplot as plt
A = 31988
B = 1000

p = 31991
n = 32089
G = [0, 5585]
points = [[0, 5585], [0, 5585]]
x = [0]
y = [5585]


def check(p, y, x, A, B):
    if (pow(y, 2, 31991) == x ** 3 + A * x + 1000) and ((4 * pow(A, 3) + 27 * pow(B, 2)) % p != 0):
        return True
    else:
        return False

# P = P
def P(G, P3):




        P1 = G
        P2 = P3
        if P1 == P2:


            lam = ((3 * pow(P1[0], 2) + A) * pow(2 * P1[1], -1, p)) % p
            x3 = (pow(lam, 2) - P1[0] * 2) % p
            y3 = (P1[1] + lam * (x3 - P1[0])) % p

            points.append([x3, y3])
            x.append(x3)
            y.append(y3)



        if P2 != P1:

            if P1[1] == (- P2[1]) % p:

                x3 = (P1[0] + P2[0]) % p
                y3 = -(P1[1] + P2[1]) % p
                points.append([x3, y3])
                x.append(x3)
                y.append(y3)

            else:     #lam = 0
                lam = ((P2[1] - P1[1]) * pow(P2[0] - P1[0], -1, p)) % p
                x3 = (pow(lam, 2) - P1[0] - P2[0]) % p# тут p относится ко всему выражению или нет?

                y3 = (P1[1] + lam * (x3 - P1[0])) % p

                points.append([x3, y3])
                x.append(x3)
                y.append(y3)




for i in range(n):
    P3 = points[-1]
    P(G, P3)


plt.scatter(x, y, s=0.7)

plt.show()
print(x, y)
