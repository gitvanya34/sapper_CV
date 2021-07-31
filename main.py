# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import UserActions
import cv2 as cv
from ComputerVision import ComputerVision
from Sapper import Sapper
from UserActions import UserActions

imageSource = cv.imread('test3/start.jpg')
imageStart = cv.imread('test3/start.jpg')

###TODO: 1)Засунауть класс Sapper в CV,
#         2)найти способ перенести контуры в массив с определением типа контура(исключить лишние контуры )
#         3) эмулировтаь работу пользоватея
#          4) Определять пустые ячейки путем исключения найденных и не найденых(на первой итерации все нашлись и добавились в массив )
#          5) определеить флаги
sapper = Sapper()
sapper.print()
sapper.tableSet(1, 1, 1, 2, 3, 4, '[eq')
sapper.print()

UserActions.screenshot()
# определяем поле рабочего пространства
UserActions.screenshot()
tableFieldCoord = ComputerVision.searchField(cv.imread('test3/TempStartTable.jpg', 0),
                                             cv.imread('screenshot.jpg',
                                                       cv.IMREAD_COLOR))  # выполняется только один раз в начале что бы определить координаты рабочей области

# Находим ячейки первой итерацией определяем координаты ячеек
imageSource, listCell = ComputerVision.searchNumbers2(tableFieldCoord, cv.imread('screenshot.jpg', cv.IMREAD_COLOR))
print(len(listCell))
ComputerVision.display(imageSource)
# раскидываем координаты по ячейкам в двумерном массиве
i, j = 0, 0
for cell in listCell:
    sapper.tableSet(j, i, cell.x1, cell.y1, cell.x2, cell.y2, cell.value)
    i = i + 1
    if i >= 30:
        i = 0
        j = j + 1
# sapper.print()
sapper.printTableValue()

# Клик по рандомной ячеке (или  не рандомной)
# TODO : КЛик по рандомной ячейке
UserActions.clickLeft(sapper.table[8][15].x1, sapper.table[8][15].y1)

# следующая итерация после первого клика по полю
UserActions.screenshot()
imageSource, listCell = ComputerVision.searchNumbers2(tableFieldCoord,
                                                      cv.imread('screenshot.jpg', cv.IMREAD_COLOR))
# print(len(listCell))
sapper.refreshTable(listCell)
sapper.printTableValue()
ComputerVision.display(imageSource)

# Первый этап решения
sapper.putFlag()
# TODO : Заполняем все мины которые изветны
# TODO : Кликаем там где уверены на 100%

# следующая итерация после разметки первого клика
imageSource, listCell = ComputerVision.searchNumbers2(tableFieldCoord,
                                                      cv.imread('screenshot.jpg', cv.IMREAD_COLOR))
# print(len(listCell))
sapper.refreshTable(listCell)
sapper.table[1][1].value ="lljjjjjjjjjjjjjjl"
sapper.table[1][2].value ="ljjjjjjjjjjjjjjll"
sapper.printTableValue()
ComputerVision.display(imageSource)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
