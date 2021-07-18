from SapperCell import SapperCell


class Sapper:
    __n = 16
    __m = 30
    table = []

    def __init__(self):
        self.table = [[SapperCell() for j in range(self.__m)] for i in range(self.__n)]

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    def tableSet(self, x, y):
        self.table[x][y] = self.table[x][y].SapperCell(1, 2, 3, 4, "[eq")

    def print(self):
        for i in range(len(self.table)):
            print(' '.join([self.table[i][j].printCell() for j in range(len(self.table[i]))]))
