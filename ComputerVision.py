import copy
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
import UserActions
import sys


class ComputerVision(object):

    def display(self,img, frameName="OpenCV Image"):
        copyImg = copy.deepcopy(img)
        h, w = img.shape[0:2]
        neww = 1000
        newh = int(neww * (h / w))
        copyImg = cv.resize(copyImg, (neww, newh))
        cv.imshow(frameName, copyImg)
        cv.waitKey(0)

    # def yelowRectangle(img,x1,y1,x2,y2):
    #
    #     img=cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 10)
    #     self.display(img)

    def grayImage(self,image):
        image = cv.imread(image)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (3, 3), 0)
        ComputerVision.display(gray)

    #
    #
    def edgedImage(self,image):
        image = cv.imread(image)
        img = cv.Canny(image, 10, 250)
        # закрытие объектов
        # kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
        # img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
        self.display(img)
        return img

    #
    #
    # image = cv.imread(cv.samples.findFile("scrin1.jpg"))
    # yelowRectangle(copy.deepcopy(image),0,0,100,100)
    # grayImage(copy.deepcopy(image))
    # closed=edgedImage(copy.deepcopy(image))


    def searchNumber(self,imageObj, imageSource):
        img_rgb = cv.imread(imageSource)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread(imageObj, 0)
        # template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray, template, cv.TM_CCORR_NORMED)
        threshold = 0.99
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        self.display(img_rgb)
        cv.waitKey(0)
        # if image is None:
        #     sys.exit("Could not read the image.")


    def checkMethodCV(self,imageObj, imageSource):
        img = cv.imread(imageSource, 0)
        img2 = img.copy()
        template = cv.imread(imageObj, 0)
        w, h = template.shape[::-1]
        # All the 6 methods for comparison in a list
        methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                   'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
        for meth in methods:
            img = img2.copy()
            method = eval(meth)
            # Apply template Matching
            res = cv.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv.rectangle(img, top_left, bottom_right, 255, 2)
            plt.subplot(121), plt.imshow(res, cmap='gray')
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(img, cmap='gray')
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth)
            plt.show()

    # grayImage('number/1.jpg')
    # edgedImage('number/1.jpg')
