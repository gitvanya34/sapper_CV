class Sapper:
    __n = 30
    __m = 16
    table = []

    def __init__(self):
        self.table = [0] * self.n
        for i in range(self.n):
            self.table[i] = [0] * self.m

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    @table.setter
    def table(self,x,y,val):
        self.table[x,y] = val

    def print(self):
        print(self.table)
