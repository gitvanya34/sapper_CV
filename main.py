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
#         2)найти способ перенести контуры в массив с определением типа контура
#         3) эмулировтаь работу пользоватея
sapper = Sapper()
# sapper.print()
sapper.tableSet(1, 1, 1,2,3,4,"[eq")
sapper.print()

obj = ComputerVision()
obj.searchNumber(cv.imread('source/StartTable.jpg', 0), imageStart)

imageSource = obj.searchNumbers(imageSource)
obj.display(imageSource)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
