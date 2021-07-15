# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy

import cv2 as cv
import sys

def display(img, frameName="OpenCV Image"):
    copyImg=copy.deepcopy(img)
    h, w = img.shape[0:2]
    neww = 1000
    newh = int(neww*(h/w))
    copyImg = cv.resize(copyImg, (neww, newh))
    cv.imshow(frameName, copyImg)
    cv.waitKey(0)


def yelowRectangle(img,x1,y1,x2,y2):

    img=cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 10)
    display(img)


def grayImage(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (3, 3), 0)
    display(gray)


def edgedImage(image):
    img = cv.Canny(image, 10, 250)
    #закрытие объектов
    # kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
    # img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

    display(img)
    return img


image = cv.imread(cv.samples.findFile("scrin1.jpg"))
yelowRectangle(copy.deepcopy(image),0,0,100,100)
grayImage(copy.deepcopy(image))
closed=edgedImage(copy.deepcopy(image))

# найдите контуры в изображении и подсчитайте количество книг
cnts = cv.findContours(closed.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#cnts = imutils.grab_contours(cnts)
total = 0

# цикл по контурам
for c in cnts:
    # аппроксимируем (сглаживаем) контур
    peri = cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, 0.02 * peri, True)

    # если у контура 4 вершины, предполагаем, что это книга
    if len(approx) == 4:
        cv.drawContours(image, [approx], -1, (0, 255, 0), 4)
        total += 1

if image is None:
    sys.exit("Could not read the image.")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
