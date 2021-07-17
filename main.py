# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import UserActions
import cv2 as cv


from ComputerVision import ComputerVision
imageSource = cv.imread('source/scrin1.jpg')
imageStart = cv.imread('source/test1.jpg')

obj=ComputerVision()

obj.searchNumber(cv.imread('source/StartTable.jpg', 0), imageStart)

imageSource=obj.searchNumbers(imageSource)
obj.display(imageSource)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
