import math
class SapperCell:
    __x1 = 0
    __y1 = 0
    __x2 = 0
    __y2 = 0
    __value = ''
    __refresh = False

    def __init__(self, x1=0, y1=0, x2=0, y2=0, val=0,refresh = False):
        # self.__x = (x1 + x2) / 2
        # self.__y = (y2 + y1) / 2
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__value = val
        self.__refresh = refresh

    @property
    def x1(self):
        return self.__x1

    @x1.setter
    def x1(self, val):
        self.__x1 = val

    @property
    def y1(self):
        return self.__y1

    @y1.setter
    def y1(self, val):
        self.__y1 = val

    @property
    def x2(self):
        return self.__x2

    @x2.setter
    def x2(self, val):
        self.__x2 = val

    @property
    def y2(self):
        return self.__y2

    @y2.setter
    def y2(self, val):
        self.__y2 = val

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @property
    def refresh(self):
        return self.__refresh

    @refresh.setter
    def refresh(self, val):
        self.__refresh = val

    def SapperCell(self, x1, y1, x2, y2, val):
        # self.__x = (x1 + x2) / 2
        # self.__y = (y2 + y1) / 2
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__value = val
        return self

    def printCell(self):
        # print(self.__x+","+self.__y+","+self.value)
        return "[%d, %d, %d, %d, %s]" % (self.__x1, self.__y1, self.__x2, self.__y2, self.__value)

    def printCellValue(self):
        # print(self.__x+","+self.__y+","+self.value)
        nameCell=''
        if self.__value == '0': nameCell = "\033[0m\033[40m{}".format("0")
        if self.__value == '1': nameCell = "\033[0m\033[1m\033[34m{}".format("1") + "\033[0m"
        if self.__value == '2': nameCell = "\033[0m\033[1m\033[34m{}".format("2") + "\033[0m"
        if self.__value == '3': nameCell = "\033[0m\033[1m\033[34m{}".format("3") + "\033[0m"
        if self.__value == '4': nameCell = "\033[0m\033[1m\033[34m{}".format("4") + "\033[0m"
        if self.__value == '5': nameCell = "\033[0m\033[1m\033[34m{}".format("5") + "\033[0m"
        if self.__value == '6': nameCell = "\033[0m\033[1m\033[34m{}".format("6") + "\033[0m"
        if self.__value == 'X': nameCell = "\033[0m\033[1m\033[31m{}".format("X") + "\033[0m"
        if self.__value == ' ': nameCell = "\033[0m{}".format(" ")
        return "%s " % (nameCell)

    @staticmethod
    def checkIntersectCells(a, b):
        # print( cellA.x2 >= cellB.x1 and cellA.x1 <= cellB.x2 and cellA.y1 <= cellB.y2 and cellA.y2 >= cellB.y1)
        # return a.x2 >= b.x1 and a.x1 <= b.x2 and a.y1 <= b.y2 and a.y2 >= b.y1
        ax1, ay1, ax2, ay2 = a.x1, a.y1, a.x2, a.y2  # прямоугольник А
        bx1, by1, bx2, by2 = b.x1, b.y1, b.x2, b.y2  # прямоугольник B

        xA = [ax1, ax2]  # координаты x обеих точек прямоугольника А
        xB = [bx1, bx2]  # координаты x обеих точке прямоугольника В
        yA = [ay1, ay2]  # координаты x обеих точек прямоугольника А
        yB = [by1, by2]  # координаты x обеих точек прямоугольника В
        if max(xA) < min(xB) or max(yA) < min(yB) or min(yA) > max(yB):
            return False  # не пересекаются
        elif max(xA) > min(xB) and min(xA) < min(xB):
            dx = max(xA) - min(xB)
            return True  # пересекаются
        else:
            return True  # пересекаются
        # print(a.y1 < b.y2 or a.y2 > b.y1 or a.x2 < b.x1 or a.x1 > b.x2)
        #  return a.y1 < b.y2 or a.y2 > b.y1 or a.x2 < b.x1 or a.x1 > b.x2

    @staticmethod
    def checkIntersectCellsDistanceBetweenPoints(a, b):
        centerAX = (a.x1 + a.x2) / 2
        centerAY = (a.y2 + a.y1) / 2
        centerBX = (b.x1 + b.x2) / 2
        centerBY = (b.y2 + b.y1) / 2
        # distans= √(math.fabs(centerAX - centerBX))**2 + (math.fabs(centerAY - centerBY))**2
        distans = math.hypot(math.fabs(centerAX - centerBX), math.fabs(centerAY - centerBY))
        if distans < 50:
            return True
        else:
            return False