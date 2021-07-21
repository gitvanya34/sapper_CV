# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import UserActions
import cv2 as cv
from ComputerVision import ComputerVision
from Sapper import Sapper

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

# определяем поле рабочего пространства
tableFieldCoord = ComputerVision.searchField(cv.imread('test3/TempStartTable.jpg', 0),
                           imageStart)  # выполняется только один раз в начале что бы определить координаты рабочей области

# Находим ячейки первой итерацией определяем координаты ячеек
imageSource, listCell = ComputerVision.searchNumbers2(tableFieldCoord ,cv.imread('test3/start.jpg', cv.IMREAD_COLOR))
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
# sapper.print()
sapper.printTableValue()

# Клик по рандомной ячеке (или  не рандомной)
# TODO : КЛик по рандомной ячейке

# следующая итерация после первого клика по полю
imageSource, listCell = ComputerVision.searchNumbers2(tableFieldCoord,cv.imread('test3/firstClick.jpg', cv.IMREAD_COLOR))
# print(len(listCell))
sapper.refreshTable(listCell)
sapper.printTableValue()
ComputerVision.display(imageSource)

# Первый этап решения
# TODO : Заполняем все мины которые изветны
# TODO : Кликаем там где уверены на 100%

# следующая итерация после разметки первого клика
imageSource, listCell = ComputerVision.searchNumbers2(tableFieldCoord,cv.imread('test3/secondClick.jpg', cv.IMREAD_COLOR))
# print(len(listCell))
sapper.refreshTable(listCell)
sapper.printTableValue()
ComputerVision.display(imageSource)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
