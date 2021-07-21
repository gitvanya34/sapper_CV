import copy
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from SapperCell import SapperCell
from Sapper import Sapper
import UserActions
import sys
import time


class ComputerVision(object):

    @staticmethod
    def display(img, frameName="OpenCV Image"):
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

    def grayImage(self, image):
        image = cv.imread(image)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (3, 3), 0)
        ComputerVision.display(gray)

    #
    #
    def edgedImage(self, image):
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

    # определяем поле рабочего пространства #ограничить поле поиска по значениям координат поля searchField
    @staticmethod
    def searchField(template,
                    img_rgb):  # Выполняется только один раз для определеения координат рабочей области # 100 на 100
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        # template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray, template, cv.TM_CCORR_NORMED)
        threshold = 0.999
        loc = np.where(res >= threshold)

        listTable = []
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            listTable.append(SapperCell(pt[0], pt[1], pt[0] + w, pt[1] + h, 'table'))

        ComputerVision.display(img_rgb)
        print(len(listTable))
        return listTable[-1]

        # if image is None:
        #     sys.exit("Could not read the image.")

    @staticmethod
    def searchNumbers2(tableFieldCoord, image):
        # img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        templates = [cv.imread('top2/cell.jpg', cv.IMREAD_COLOR),
                     cv.imread('top2/1.jpg', cv.IMREAD_COLOR),
                     cv.imread('top2/2.jpg', cv.IMREAD_COLOR),
                     cv.imread('top2/3.jpg', cv.IMREAD_COLOR),
                     cv.imread('top2/4.jpg', cv.IMREAD_COLOR),
                     cv.imread('top2/5.jpg', cv.IMREAD_COLOR),
                     cv.imread('top2/6.jpg', cv.IMREAD_COLOR),
                     cv.imread('top2/flag.jpg', cv.IMREAD_COLOR)
                     ]

        listCell = []
        # listCell.append(SapperCell(0, 0, 0, 0, 0))

        for idx, template in enumerate(templates):
            # image = cv.imread('smiley.png', cv.IMREAD_COLOR)
            # template = cv.imread('template.png', cv.IMREAD_COLOR)
            if idx == 0: nameCell = "\033[0m\033[40m{}".format("0")
            if idx == 1: nameCell = "\033[0m\033[1m\033[34m{}".format("1")+"\033[0m"
            if idx == 2: nameCell = "\033[0m\033[1m\033[34m{}".format("2")+"\033[0m"
            if idx == 3: nameCell = "\033[0m\033[1m\033[34m{}".format("3")+"\033[0m"
            if idx == 4: nameCell = "\033[0m\033[1m\033[34m{}".format("4")+"\033[0m"
            if idx == 5: nameCell = "\033[0m\033[1m\033[34m{}".format("5")+"\033[0m"
            if idx == 6: nameCell = "\033[0m\033[1m\033[34m{}".format("6")+"\033[0m"
            if idx == 7: nameCell = "\033[0m\033[1m\033[31m{}".format("X")+"\033[0m"

            h, w = template.shape[:2]

            method = cv.TM_CCORR_NORMED
            threshold = 0.99
            start_time = time.time()
            res = cv.matchTemplate(image, template, method)

            # fake out max_val for first run through loop
            max_val = 1
            while max_val > threshold:
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

                if max_val > threshold:
                    res[max_loc[1] - h // 2:max_loc[1] + h // 2 + 1, max_loc[0] - w // 2:max_loc[0] + w // 2 + 1] = 0
                    a = SapperCell(max_loc[0], max_loc[1], max_loc[0] + w + 1, max_loc[1] + h + 1, nameCell)
                    if SapperCell.checkIntersectCells(a, tableFieldCoord):
                        image = cv.rectangle(image, (max_loc[0], max_loc[1]), (max_loc[0] + w + 1, max_loc[1] + h + 1),
                                             (0, 0, 255), 2)
                        listCell.append(a)

        listCell.sort(key=lambda cell: (cell.y1, cell.x1))
        # удаляем первый элемент (ложное срабатывание на кнопку)
        # del listCell[0]
        # for i in listCell:
        #     print(i.printCell())

        return image, listCell

    #     TODO Заполняем таблицу построчно из сортированного массива первой итерации, затем обновляем значения
    #      посредством нахождения точки внутри контура.
    #       необновленные ячейки становятся пустыми (костыли тема)

    @staticmethod
    def searchNumbers(img_rgb):
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        templates = [cv.imread('top/cell.jpg', 0),
                     cv.imread('top/1.jpg', 0),
                     cv.imread('top/2.jpg', 0),
                     cv.imread('top/3.jpg', 0),
                     cv.imread('top/flag.jpg', 0)]

        listCell = []
        listCell.append(SapperCell(0, 0, 0, 0, 0))

        for idx, temp in enumerate(templates):

            w, h = temp.shape[::-1]
            res = cv.matchTemplate(img_gray, temp, cv.TM_CCORR_NORMED)
            threshold = 0.99
            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                # cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                # if SapperCell.checkIntersectCells(listCell[-1], listCell[-2]):
                # for i in listCell:
                #     if not SapperCell.checkIntersectCellsDistanceBetweenPoints(
                #             SapperCell(pt[0], pt[1], pt[0] + w, pt[1] + h, idx), listCell[-1]):
                listCell.append(SapperCell(pt[0], pt[1], pt[0] + w, pt[1] + h, idx))

        listCell.sort(key=lambda cell: (cell.y1, cell.x1))
        for i, temp in enumerate(listCell):
            try:
                if SapperCell.checkIntersectCells(listCell[i], listCell[i + 1]):
                    del listCell[i + 1]
            except:
                print(-i)

        listCell.sort(key=lambda cell: (cell.x1, cell.y1))
        for i, temp in enumerate(listCell):
            try:
                if SapperCell.checkIntersectCells(listCell[i], listCell[i + 1]):
                    del listCell[i + 1]
            except:
                print(-i)

            # ut.sort(key=lambda x: x.count, reverse=True)
            # sorted(listCell, key=lambda x: (x[0], -x[1]))
        # for i, tempI in enumerate(listCell):
        #     for j, tempJ in enumerate(listCell):
        #         if not i == j:
        #             if not SapperCell.checkIntersectCells(listCell[i], listCell[j]):
        #                 del listCell[j]
        for item in listCell:
            cv.rectangle(img_rgb, (item.x1, item.y1), (item.x2, item.y2), (0, 0, 255), 2)

        ###TODO: удалить из списка listCell все пересекающиеся контуры, оставить только один экземпляр

        # delIndex = []
        # for idx in range(len(listCell) - 1):
        #     if SapperCell.checkIntersectCells(listCell[idx], listCell[idx + 1]):
        #         delIndex.append(idx)
        # for idx, obj in enumerate(listCell):
        #     for i in delIndex:
        #         if i == idx:
        #             del listCell[idx]

        for i in listCell:
            print(i.printCell())
            # del listCell[idx]
        # listCell = [item for item in listCell if not SapperCell.checkIntersectCells(listCell[idx], listCell[idx+1])]

        return img_rgb, listCell

    def checkMethodCV(self, imageObj, imageSource):
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
