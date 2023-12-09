from lab11 import P
import random
n = 32089
G = [0, 5585]
x = [0]
y = [5585]

p = 31991
A = 31988
B = 1000
R = [[0,0]]
x = [0]
y = [5585]

#message = int(input("Message int? "))
def fast(secret_bin):
    P0 = [0, 0]
    count = 0
    for i in secret_bin:
        count += 1
        if count == 1:
            if i == '1':
                P(P0, P0, p, A)
                P3 = [x[-1], y[-1]]
                P(P3, G, p, A)
            elif i == "0":
                P3 = [x[-1], y[-1]]
                P(P0, P0, p, A)
        else:
            if i == '1':
                P3 = [x[-1], y[-1]]
                P(P3, P3, p, A)
                P(P3, G, p, A)
            elif i == "0":
                P3 = [x[-1], y[-1]]
                P(P3, P3, p, A)
        code = [x[-1], y[-1]]
    #del x[1:]
    #del y[1:]
    print(x, y)
    return code

def El_Gam():
    k = random.randint(0, n)
    print('Число k=', k)
    secret_key_A = random.randint(0, n)
    secret_key_B = random.randint(0, n)
    bit_k = bin(k)[2:]
    secret_key_A_bin = bin(secret_key_A)[2:] # Cu
    secret_key_B_bin = bin(secret_key_B)[2:] # Cu
    R = fast(bit_k)




    return R
print(fast('101'))