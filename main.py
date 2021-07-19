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
# sapper.print()
sapper.tableSet(1, 1, 1,2,3,4,"[eq")
sapper.print()

obj = ComputerVision()
obj.searchField(cv.imread('source/StartTable.jpg', 0), imageStart)


imageSource, listCell = obj.searchNumbers(imageSource)
print(len(listCell))
obj.display(imageSource)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
