# y^2 = x^3  + 31988x + 1000

A = 31988
B = 1000
x0 = 0
y0 = 5585
p = 31991


# P = P
def func():
    lam = ((3 * pow(x0, 2) + A) / (2 * y0)) % p
    x = (pow(lam, 2) - 2 * x0) % p
    y = (y0 + lam * (x - x0)) % p
    return [x, y]

print(pow(A / (2 * 5585), 1, p))
