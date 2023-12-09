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
        first = self.first_coefficient
        second = self.second_coefficient
        p = self.p
        self.end_coef = []
        middle_coef = []

        div = 1
        while div != 0:
            while True:
                ...
    def multiplication(self):
        first = self.first_coefficient
        second = self.second_coefficient
        p = self.p
        self.end_coef = []
        middle_coef = []
        for i in range(len(first)):
            middle_coef.append(0)
        z = 0
        for first_coef in first:
            z += 1
            for j in second:
                end = int(first_coef * j)
                if middle_coef[]








a = Polinom([1, 2], [3])

print(a.__doc__)
print(a.__dict__)

print(a.minus())
# first = setattr(Polinom, 'first_coefficient', [1, 2, 5, 8 ])
# second = setattr(Polinom, 'second_coefficient', [1, 2, 2, 8 ])
# print(Polinom.__dict__)
