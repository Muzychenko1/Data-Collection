from string import ascii_letters


class Person:
    S_ENG = 'abcdifghijklmnopqrstuvwxyz-'
    S_ENG_UPPER = S_ENG.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('Full name must be a string')

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Invalid full name format")

        letters = ascii_letters + cls.S_ENG + cls.S_ENG_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("Full name must contain at least one character")
            if len(s.strip(letters)) != 0:
                raise TypeError("Only alphabetic characters and a hyphen can be used in your full name")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Age must be an integer in the range [14; 120]")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Weight must be at least 20")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Passport must be a string")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Invalid passport format")

        for p in s:
            if not p.isdigit():
                raise TypeError("Passport series and number must be numbers")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps


p = Person('Matvey Muzychenko Evgenievich', 15, '1234 567890', 65.0)