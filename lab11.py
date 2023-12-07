import matplotlib.pyplot as plt
import random
import hashlib
import math
n = 32089
G = [0, 5585]
x = [0]
y = [5585]

p = 31991
A = 31988
B = 1000
def P(P1, P2, p, A):
    x1 = P1[0]
    x2 = P2[0]
    y1 = P1[1]
    y2 = P2[1]

    if x1 == 0 and y1 == 0:
        x.append(x2)
        y.append(y2)
        return 0

    if x2 == 0 and y2 == 0:
        y.append(y1)
        x.append(x1)
        return 0


    if x1 == x2 and y1 == y2:

        lam = ((3 * pow(x1, 2) + A) * pow(2 * y1, -1, p)) % p
        x3 = (pow(lam, 2) - x1 - x2) % p
        y3 = (y1 + lam * (x3 - x1)) % p
        x.append(x3), y.append((-y3) % p)
        return 0
    elif x1 == x2 and y1 == - y2 % p:


        x.append(0), y.append(0)
        return 0


    elif x1 != x2 or y1 != y2:

        lam = ((y2 - y1) * pow(x2 - x1, -1, p)) % p  #

        x3 = (pow(lam, 2) - x1 - x2) % p
        y3 = (y1 + lam * (x3 - x1)) % p


        x.append(x3), y.append((-y3) % p)
        return 0
    elif x1 == x2 and y1 == - y2 % p:
        lam = ((y2 - y1) * pow(x2 - x1, -1, p)) % p

        x3 = (pow(lam, 2) - x1 - x2) % p
        y3 = (y1 + lam * (x3 - x1)) % p
        x.append(0), y.append(0)
        return 0
def fast(secret_bin, generate_points):
    P0 = [0, 0]
    flag = True
    for i in secret_bin:

        if flag == True:
            if i == '1':
                P(P0, P0, p, A)
                P3 = [x[-1], y[-1]]
                x.pop(-1)
                y.pop(-1)
                P(P0, generate_points, p, A)
            elif i == "0":
                x.append(0)
                y.append(0)
                #P3 = [x[-1], y[-1]]
                #P(P0, P0, p, A)


            flag = False
        else:
            if i == '1':
                P3 = [x[-1], y[-1]]
                P(P3, P3, p, A)
                P3 = [x[-1], y[-1]]
                x.pop(-1)
                y.pop(-1)

                P(P3, generate_points, p, A)
            elif i == "0":
                P3 = [x[-1], y[-1]]
                P(P3, P3, p, A)
    code = [x[-1], y[-1]]
    del x[1:]
    del y[1:]


    return code

def El_Gam(message):
    k = random.randint(0, p)

    print('Число k=', k)
    secret_key_A = random.randint(0, p)
    secret_key_B = random.randint(0, p)
    print('Sec=', secret_key_B)
    bit_k = bin(k)[2:]

    secret_key_A_bin = bin(secret_key_A)[2:] # Ca
    secret_key_B_bin = bin(secret_key_B)[2:] # Cb



    Db = fast(secret_key_B_bin, G)
    print('D=', Db)
    R = fast(bit_k, G)
    print("R= ", R)
    P = fast(bit_k, Db)
    print('P=', P)
    encode = (message * P[0]) % p
    print('Закодированное сообщение:', encode)
    Q = fast(secret_key_B_bin, R)
    print('Q= ', Q)

    message_decode = (encode * pow(Q[0], -1, p)) % p


    return message_decode

def Def_Helm():
    Ka = random.randint(0, p)
    Kb = random.randint(0, p)
    Ka_bin = bin(Ka)[2:]
    Kb_bin = bin(Kb)[2:]
    key = Ka * Kb
    key_bin = bin(key)[2:]
    general_key = fast(key_bin, G)
    print('General key = ', general_key)
    print('KaG', fast(Kb_bin, G))

    print('A пересылает B', fast(Ka_bin, G))
    print('B пересылает A', fast(Kb_bin, G))
def generation_prime(k):
    binary = []
    for i in range(k):
        bit = random.randint(0, 1)
        binary.append(bit)

    del binary[-1]
    binary.append(1)
    del binary[0]
    binary.insert(0, 1)

    p = int(''.join(str(x) for x in binary), 2)

    test = []
    for i in range(5):
        test.append(test_miller2(p))

    if test.count(True) == len(test):

        return p

    else:
        return generation_prime(k)
def test_miller2(n):
    a = random.randint(1, n - 2)
    exp = n - 1
    while not exp & 1:
        exp >>= 1

    if pow(a, exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
        exp <<= 1

    return False
def euclid_algorithm2(a, b):

    r = [a, b]
    x = [1, 0]
    y = [0, 1]

    i = 0
    while r[i] != 0:
        if r[i + 1] != 0:

            q = (r[i] // r[i + 1])
            c = r[i] - q * r[i + 1]
            a = x[i] - q * x[i + 1]
            b = y[i] - q * y[i + 1]

            x.append(a)
            y.append(b)
            r.append(c)
            i += 1

        elif r[i + 1] == 0:
            break

    d = r[i]
    u = x[i]
    v = y[i]

    return [d, u, v]

def first_degree(a, b, m):
    d = euclid_algorithm2(a, m)
    x = []

    if b % d[0] != 0:
        return f"Сравнение {a}x = {b} (mod {m}) не имеет решений."

    elif d[0] != 1:
        a1 = int(a/d[0])
        b1 = int(b/d[0])
        m1 = int(m/d[0])
        d1 = euclid_algorithm2(a1, m1)
        if d1[0] == a1 * d1[1] + m1 * d[2]:
            x1 = b1 * d1[1]
            while x1 < 0:
                x1 += m1
            for i in range(0, d[0]):
                c = x1 + m1 * i
                x.append(c)

    elif d[0] == 1:
        if d[0] == a * d[1] + m * d[2]:
            x1 = b * d[1]
            while x1 < 0:
                x1 += m
            while x1 > m:
                x1 -= m
            x.append(x1)
    return int(x[-1])



def gen_ell():
    p = generation_prime(512)
    t = int(math.log2(p))
    s = int((t - 1) / 160)
    v = t - 160 * s
    print(t, s, v)
    bit_z = ''
    bit_list = []
    for i in range(160):
        choose = str(random.randint(0, 1))
        bit_list.append(choose)
    bit_z = ''.join(bit_list)
    bit_z = '0b' + bit_z
    z = int(bit_z, 2)
    str_z = str(z).encode('utf-8')
    #z_sha = hashlib.sha256(str_z).hexdigest()
    z_sha = hashlib.sha1(str_z).hexdigest()

    int_z = bin(int(z_sha, 16))
    c0 = int_z[-v:]
    w0 = '0' + c0[1:]
    str_w0 = str(w0).encode('utf-8')
    w0_sha1 = hashlib.sha1(str_w0).hexdigest()

    list_w = []
    list_w.append(w0_sha1)
    for i in range(1, s + 1):
        #print(type(i))
        if s == 0:
            break
        si = bin(pow(z + i, 1, 2 ** 512))[2:]
        #si = - si
        #wi = hashlib.sha1(si)
        #print('si - ', si)

        i_bit_list = []
        for i_bit in si:
            if i_bit == '0':
                i_bit_list.append('1')
            else:
                i_bit_list.append('0')
        #print(i_bit_list)
        wi = ''.join(i_bit_list)
        str_wi = str(wi).encode('utf-8')
        wi_sha = hashlib.sha1(str_wi).hexdigest()
        list_w.append(wi_sha)
        w = ''.join(list_w)
        r = int(w, 16)

    if r == 0 or ((4 * r + 27) % p == 0):
        gen_ell()
        print('error')
    else:
        b = random.randint(2, p - 1)
        d = int(first_degree(3, 1, p - 1))
        a = pow((r * pow(b, 2)) % p, d, p)
        #print((r * pow(b, 2)) % p == pow(a, 3, p))
        print(f'y ** 2 = x ** 3 + {a}x + {b}')

        #if (r * pow(b, 2)) % p == pow(a, 3, p):
            #print('E: y ** 2 = x ** 3 + %a * x + %b' % (a, b))
















    #print(c0)
    #print(w0)
    #print(int_z)







def auth(passwd_db = list):
    passwd = input('Enter your passwd: ').encode('utf-8')
    passwd_hash = hashlib.sha256(passwd).hexdigest()
    if passwd_db.count(passwd_hash) != 0:
        print('Valid passwd')
        Def_Helm()
    else:
        print('Invalid passwd')
        return False
def lab_1():
    for i in range(n):

        if i == 0:
            P(G, G, p, A)
        if i == 36:
            P1 = [x[-1], y[-1]]
            print(P1)
        else:
            P1 = [x[-1], y[-1]]
            P(P1, G, p, A)
def lab_2():
    print(El_Gam(int(input('Сообщение? '))))
def lab_3():
    passwd_db = []
    while True:
        choose = input('New user? Y/N ').lower()
        if choose == 'n':
            break
        passwd = input('Password? ').encode('utf-8')
        passwd_hash = hashlib.sha256(passwd).hexdigest()
        passwd_db.append(passwd_hash)
    auth(passwd_db)
def lab_4():
    print(gen_ell())

class Polinom():


lab_4()



