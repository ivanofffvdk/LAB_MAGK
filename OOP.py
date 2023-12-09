from itertools import groupby


class Polinom:
    """Класс, определяющий сложение, вычитание, деление, умножение многочленов"""
    @classmethod
    def __equalization(cls, first_coefficient, second_coefficient):
        while True:
            first_len = len(first_coefficient)
            second_len = len(second_coefficient)
            if first_len != second_len:
                if first_len > second_len:
                    second_coefficient.append(0)
                else:
                    first_coefficient.append(0)
            else:


                return print('OK')
    @classmethod
    def clean(cls, first_coefficient):
        first = first_coefficient

        first = [el for el, _ in groupby(first)]
        first.remove(0)
        return first


    def __init__(self, first = list, second = list):
        self.first_coefficient = first
        self.second_coefficient = second
        self.__equalization(self.first_coefficient, self.second_coefficient)
        self.p = 31991
    def __getattr__(self, item):
        return False


    def plus(self):
        first = self.first_coefficient
        second = self.second_coefficient
        p = self.p
        self.end_coef = []
        for i in range(len(first)):
            coefficient = (int(first[i]) + int(second[i])) % p
            self.end_coef.append(coefficient)
        return self.end_coef


    def minus(self):
        first = self.first_coefficient
        second = self.second_coefficient
        p = self.p
        self.end_coef = []
        for i in range(len(first)):
            coefficient = (int(first[i]) - int(second[i])) % p
            self.end_coef.append(coefficient)
        return self.end_coef




    def division(self):
            from itertools import groupby
            first = self.first_coefficient
            second = [el for el, _ in groupby(self.second_coefficient)]
            second.remove(0)
            if len(first) >= len(second):

                shiftlen = len(first) - len(second)
                den = [0] * shiftlen + second
            else:
                return [0], first

            quot = []
            divisor = int(second[-1])
            for i in range(shiftlen + 1):

                mult = int(first[-1] / divisor)
                quot = [mult] + quot

                if mult != 0:
                    d = [mult * u for u in den]
                    num = [u - v for u, v in zip(first, d)]

                first.pop()
                if len(second) == 0:
                    continue
                else:
                    second.pop(0)
                #print(len(second), 'len')

            # quot.reverse()

            return quot, second




    def multiplication(self):
        first = self.first_coefficient
        second = self.clean(self.second_coefficient)

        p = self.p
        n1 = len(first)
        n2 = len(second)
        n = (n1 + n2 - 1) % p
        r = [0 for i in range(n)]
        for k in range(n):
            for i in range(k + 1):
                j = k - i
                if (j < n2) and (i < n1):
                    r[k] += (first[i] * second[j]) % p
        return r








c = [6, 11, 6, 1]
print(len(c))

a = Polinom([6, 11, 6, 1], [1, 1])
print(a.__doc__)
#print(a.__dict__)
print(a.division())


#print(a.minus())
# first = setattr(Polinom, 'first_coefficient', [1, 2, 5, 8 ])
# second = setattr(Polinom, 'second_coefficient', [1, 2, 2, 8 ])
# print(Polinom.__dict__)

