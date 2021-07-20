# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import UserActions
import cv2 as cv
from ComputerVision import ComputerVision
from Sapper import Sapper

imageSource = cv.imread('source/scrin1.jpg')
imageStart = cv.imread('source/test1.jpg')

###TODO: 1)Засунауть класс Sapper в CV,
#         2)найти способ перенести контуры в массив с определением типа контура(исключить лишние контуры )
#         3) эмулировтаь работу пользоватея
#          4) Определять пустые ячейки путем исключения найденных и не найденых(на первой итерации все нашлись и добавились в массив )
#          5) определеить флаги
sapper = Sapper()
sapper.print()
sapper.tableSet(1, 1, 1, 2, 3, 4, '[eq')
sapper.print()

# определяем поле
ComputerVision.searchField(cv.imread('source/StartTable.jpg', 0),
                           imageStart)  # выполняется только один раз в начале что бы определить координаты рабочей области

# Находим ячейки первой итерацией определяем координаты ячеек
# TODO ограничить поле поиска по значениям координат поля searchField
imageSource, listCell = ComputerVision.searchNumbers2(cv.imread('source/test1.jpg', cv.IMREAD_COLOR))
print(len(listCell))
ComputerVision.display(imageSource)
# раскидываем координаты по ячейкам в двумерном массиве
i, j = 0,0
for cell in listCell:
    sapper.tableSet(j, i, cell.x1, cell.y1, cell.x2, cell.y2, cell.value)
    i = i + 1
    if i >= 30:
        i = 0
        j = j + 1

sapper.print()
sapper.printTableValue()

# TODO: расикдать втруб интерацию ,сделать функцию определения причасности к ячейке (запрещенной в россии организации)))
# следующая итерация после первого клика по полю
imageSource, listCell = ComputerVision.searchNumbers2(cv.imread('source/scrin1.jpg', cv.IMREAD_COLOR))
print(len(listCell))
ComputerVision.display(imageSource)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
