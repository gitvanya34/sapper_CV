from SapperCell import SapperCell


###TODO: Клтеки лежат внутри контура таблицы

class Sapper:
    __n = 16
    __m = 30
    __table = []

    def __init__(self):
        self.__table = [[SapperCell() for j in range(self.__m)] for i in range(self.__n)]

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, x, y, x1, y1, x2, y2, val):
        self.table[x][y] = self.table[x][y].SapperCell(1, 2, 4, 4, "[eq")

    def tableSet(self, x, y, x1, y1, x2, y2, val):
        self.table[x][y] = self.table[x][y].SapperCell(x1, y1, x2, y2, val)

    def print(self):
        for i in range(len(self.table)):
            print(' '.join([self.table[i][j].printCell() for j in range(len(self.table[i]))]))

    def printTableValue(self):
        for i in range(len(self.table)):
            print(''.join([self.table[i][j].printCellValue() for j in range(len(self.table[i]))]))
