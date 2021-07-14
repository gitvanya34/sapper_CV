# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2 as cv
import sys

def display(img, frameName="OpenCV Image"):
    h, w = img.shape[0:2]
    neww = 800
    newh = int(neww*(h/w))
    img = cv.resize(img, (neww, newh))
    cv.imshow(frameName, img)
    cv.waitKey(0)

img = cv.imread(cv.samples.findFile("sap.jpg"))
display(img)
if img is None:
    sys.exit("Could not read the image.")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
