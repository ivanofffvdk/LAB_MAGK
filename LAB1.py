# y^2 = x^3  + 31988x + 1000
import sys

import matplotlib.pyplot as plt
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
    #for i in range(n): # 32089



        P1 = points[-1]
        P2 = points[-2]
        if P1 == P2:
            lam = pow(round(((3 * pow(P1[0], 2) + A) / (2 * P1[1]))), 1, p)
            x3 = pow(round((pow(lam, 2) - 2 * P1[0]) % p), 1, p)
            y3 = pow(round((y0 + lam * (x3 - P1[0])) % p), 1, p)
            #if check(p, y3, x3, A, B ) == True: #по этому условию не проходит, не принадлежит прямой
            points.append([x3, y3])
            plt.scatter(x3, y3, s=0.7)


        elif points[i] != points[i - 1]:
            if P2[0] - P1[0] == 0:
                lam = 0
            else:
                lam = round((P2[1] - P1[1]) / (P2[0] - P1[0])) % p
            x3 = pow(lam ** 2 - P1[0] - P2[0], 1, p) # тут p относится ко всему выражению или нет?

            y3 = pow(P1[1] + lam, 1, p)
                # if check(p, y3, x3, A, B ) == True: #по этому условию не проходит, не принадлежит прямой
            points.append([x3, y3])
            #plt.scatter(x3, y3, s=0.7)

        else:# P1[1] == (- P2[1]) % p: # не понял
            lam = ((3 * pow(P1[0], 2) + A) * (2 * P1[1])) % p
            x3 = (pow(lam, 2) - (2 * P1[0])) % p
            y3 = pow(P1[1] + lam * (x3 - P1[0]),1, p)
            points.append([x3, y3])
            print(points)
            #plt.scatter(x3, y3, s=0.7)
            ...
    #plt.show()


for i in range(n):

    P()
    #plt.ioff()
    plt.scatter(points[i][0], points[i][1], s=0.7)
plt.savefig('figure', format="png")

print(points)

#plt.show(block=True)



print(points)
#plt.scatter(x3, y3, s=0.7)
#plt.show()


