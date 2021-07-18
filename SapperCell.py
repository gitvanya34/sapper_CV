class SapperCell:
    __x = 0
    __y = 0
    __value = ''

    def __init__(self):
        self.__value = ''

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    def SapperCell(self, x1, y1, x2, y2, val):
        self.__x = (x1 + x2) / 2
        self.__y = (y2 + y1) / 2
        self.__value = val
        return self

    def printCell(self):
        # print(self.__x+","+self.__y+","+self.value)
        return "[%d, %d, %s]" % (self.__x, self.__y, self.__value)
