from SapperCell import SapperCell
from UserActions import UserActions


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
        print(" ")
        for i in range(len(self.table)):
            print(''.join([self.table[i][j].printCellValue() for j in range(len(self.table[i]))]))

    # Обновляем ячейки актуальным изображением, ищем пустые клетки
    def refreshTable(self, listCell):
        for i in range(self.n):
            for j in range(self.m):
                for l in listCell:
                    x = (l.x1 + l.x2) / 2
                    y = (l.y1 + l.y2) / 2
                    if self.table[i][j].x1 <= x <= self.table[i][j].x2 and \
                            self.table[i][j].y1 <= y <= self.table[i][j].y2:
                        self.table[i][j].value = l.value
                        self.table[i][j].refresh = True  # обновилась ли ячейка в таблице
                        # print (True)

        for i in range(self.n):
            for j in range(self.m):
                if not self.table[i][j].refresh:
                    self.table[i][j].value = " "  # "\033[0m{}".format(" ")
                self.table[i][j].refresh = False

    def checkFlag(self):
        countNumber = ['1', '2', '3', '4', '5', '6']
        for i in range(0, self.n):
            for j in range(0, self.m):
                for number in countNumber:
                    countLockCell = 0
                    if self.table[i][j].value == number:  # TODO баг с повтором первых строк
                        try:
                            if self.table[i - 1][j - 1].value == '0' \
                                    or self.table[i - 1][j - 1].value == 'newX' \
                                    or self.table[i - 1][j - 1].value == 'X' \
                                    and 0 <= i - 1 \
                                    and 0 <= j - 1:
                                countLockCell += 1
                        except:
                            print()
                        try:
                            if self.table[i - 1][j].value == '0' \
                                    or self.table[i - 1][j].value == 'newX' \
                                    or self.table[i - 1][j].value == 'X' \
                                    and 0 <= i - 1:
                                countLockCell += 1
                        except:
                            print()
                        try:
                            if self.table[i - 1][j + 1].value == '0' \
                                    or self.table[i - 1][j + 1].value == 'newX' \
                                    or self.table[i - 1][j + 1].value == 'X' \
                                    and 0 <= i - 1 \
                                    and j + 1 < self.m:
                                countLockCell += 1
                        except:
                            print()
                        try:
                            if self.table[i + 1][j - 1].value == '0' \
                                    or self.table[i + 1][j - 1].value == 'newX' \
                                    or self.table[i + 1][j - 1].value == 'X'\
                                    and 0 <= j - 1 \
                                    and i + 1 < self.n:
                                countLockCell += 1
                        except:
                            print()
                        try:
                            if self.table[i + 1][j].value == '0' \
                                    or self.table[i + 1][j].value == 'newX' \
                                    or self.table[i + 1][j].value == 'X'\
                                    and i + 1 < self.n:
                                countLockCell += 1
                        except:
                            print()
                        try:
                            if self.table[i + 1][j + 1].value == '0' \
                                    or self.table[i + 1][j + 1].value == 'newX' \
                                    or self.table[i + 1][j + 1].value == 'X' \
                                    and i + 1 < self.n \
                                    and j + 1 < self.m:
                                countLockCell += 1
                        except:
                            print()
                        try:
                            if self.table[i][j - 1].value == '0' \
                                    or self.table[i][j - 1].value == 'newX' \
                                    or self.table[i][j - 1].value == 'X'\
                                    and 0 <= j - 1:
                                countLockCell += 1
                        except:
                            print()
                        try:
                            if self.table[i][j + 1].value == '0' \
                                    or self.table[i][j + 1].value == 'newX' \
                                    or self.table[i][j + 1].value == 'X'\
                                    and j + 1 < self.m:
                                countLockCell += 1
                        except:
                            print()


                    if countLockCell == int(number):  # and countLockCell
                        try:
                            if self.table[i - 1][j - 1].value == '0' \
                                    and 0 <= i - 1 \
                                    and 0 <= j - 1:
                                self.table[i - 1][j - 1].value = 'X'
                                UserActions.clickRight(self.table[i - 1][j - 1].x1, self.table[i - 1][j - 1].y1)
                        except:
                            print()
                        try:
                            if self.table[i - 1][j].value == '0' \
                                    and 0 <= i - 1:
                                self.table[i - 1][j].value = 'X'
                                UserActions.clickRight(self.table[i - 1][j].x1, self.table[i - 1][j].y1)
                        except:
                            print()
                        try:
                            if self.table[i - 1][j + 1].value == '0' \
                                    and 0 <= i - 1 \
                                    and j + 1 < self.m:
                                self.table[i - 1][j + 1].value = 'X'
                                UserActions.clickRight(self.table[i - 1][j + 1].x1, self.table[i - 1][j + 1].y1)
                        except:
                            print()
                        try:
                            if self.table[i + 1][j - 1].value == '0'\
                                    and 0 <= j - 1 \
                                    and i + 1 < self.n:
                                self.table[i + 1][j - 1].value = 'X'
                                UserActions.clickRight(self.table[i + 1][j - 1].x1, self.table[i + 1][j - 1].y1)
                        except:
                            print()
                        try:
                            if self.table[i + 1][j].value == '0'\
                                    and i + 1 < self.n:
                                self.table[i + 1][j].value = 'X'
                                UserActions.clickRight(self.table[i + 1][j].x1, self.table[i + 1][j].y1)
                        except:
                            print()
                        try:
                            if self.table[i + 1][j + 1].value == '0' \
                                    and i + 1 < self.n \
                                    and j + 1 < self.m:
                                self.table[i + 1][j + 1].value = 'X'
                                UserActions.clickRight(self.table[i + 1][j + 1].x1, self.table[i + 1][j + 1].y1)
                        except:
                            print()
                        try:
                            if self.table[i][j - 1].value == '0'\
                                    and 0 <= j - 1:
                                self.table[i][j - 1].value = 'X'
                                UserActions.clickRight(self.table[i][j - 1].x1, self.table[i][j - 1].y1)
                        except:
                            print()
                        try:
                            if self.table[i][j + 1].value == '0'\
                                    and j + 1 < self.m:
                                self.table[i][j + 1].value = 'X'
                                UserActions.clickRight(self.table[i][j + 1].x1, self.table[i][j + 1].y1)
                        except:
                            print()

    def putFlag(self):
        self.checkFlag()
        # for i in range(self.n):
        #     for j in range(self.m):
        #         if self.table[i][j].value == 'newX':
        #             self.table[i][j].value = 'X'
        #             UserActions.clickRight(self.table[i][j].x1, self.table[i][j].y1)
        self.openCell()

    def openCell(self):
        countNumber = ['1', '2', '3', '4', '5', '6']
        for i in range(self.n):
            for j in range(self.m):
                for number in countNumber:
                    countFlag = 0
                    countClosed = 0
                    if self.table[i][j].value == number:  #
                        try:
                            if self.table[i - 1][j - 1].value == 'X' \
                                    and 0 <= i - 1 \
                                    and 0 <= j - 1:
                                countFlag += 1
                        except:
                            print()
                        try:
                            if self.table[i - 1][j].value == 'X' \
                                    and 0 <= i - 1:
                                countFlag += 1
                        except:
                            print()
                        try:
                            if self.table[i - 1][j + 1].value == 'X' \
                                    and 0 <= i - 1 \
                                    and j + 1 < self.m:
                                countFlag += 1
                        except:
                            print()
                        try:
                            if self.table[i + 1][j - 1].value == 'X' \
                                    and 0 <= j - 1 \
                                    and i + 1 < self.n:
                                countFlag += 1
                        except:
                            print()
                        try:
                            if self.table[i + 1][j].value == 'X' \
                                    and i + 1 < self.n:
                                countFlag += 1
                        except:
                            print()
                        try:
                            if self.table[i + 1][j + 1].value == 'X' \
                                    and i + 1 < self.n \
                                    and j + 1 < self.m:
                                countFlag += 1
                        except:
                            print()
                        try:
                            if self.table[i][j - 1].value == 'X' \
                                    and 0 <= j - 1:
                                countFlag += 1
                        except:
                            print()
                        try:
                            if self.table[i][j + 1].value == 'X' \
                                    and j + 1 < self.m:
                                countFlag += 1
                        except:
                            print()

                        if countFlag == int(number):
                            try:
                                if self.table[i - 1][j - 1].value == '0' \
                                        and 0 <= i - 1 \
                                        and 0 <= j - 1:
                                    countClosed += 1
                            except:
                                print()
                            try:
                                if self.table[i - 1][j].value == '0' \
                                        and 0 <= i - 1:
                                    countClosed += 1
                            except:
                                print()
                            try:
                                if self.table[i - 1][j + 1].value == '0' \
                                        and 0 <= i - 1 \
                                        and j + 1 < self.m:
                                    countClosed += 1
                            except:
                                print()
                            try:
                                if self.table[i + 1][j - 1].value == '0' \
                                        and 0 <= j - 1 \
                                        and i + 1 < self.n:
                                    countClosed += 1
                            except:
                                print()
                            try:
                                if self.table[i + 1][j].value == '0' \
                                        and i + 1 < self.n:
                                    countClosed += 1
                            except:
                                print()
                            try:
                                if self.table[i + 1][j + 1].value == '0' \
                                        and i + 1 < self.n \
                                        and j + 1 < self.m:
                                    countClosed += 1
                            except:
                                print()
                            try:
                                if self.table[i][j - 1].value == '0' \
                                        and 0 <= j - 1:
                                    countClosed += 1
                            except:
                                print()
                            try:
                                if self.table[i][j + 1].value == '0' \
                                        and j + 1 < self.m:
                                    countClosed += 1
                            except:
                                print()
                    if countFlag == int(number) and countClosed > 0:  # and countLockCell
                        UserActions.clickMiddle(self.table[i][j].x1, self.table[i][j].y1)

    # def openCell(self):
    #     self.checkFlag()
    #     for i in range(self.n):
    #         for j in range(self.m):
    #             if self.table[i][j].value == 'open':
    #                 # self.table[i][j].value = 'X'
    #                 UserActions.clickLeft(self.table[i][j].x1, self.table[i][j].y1)
