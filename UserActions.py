import pyautogui


class UserActions(object):

    @staticmethod
    def screenshot():
        screen = pyautogui.screenshot('screenshot.jpg')
        print(screen)
        return screen

    #     pyautogui.moveTo(25, 25)  # Передвинули мышку в левый нижний угол (в район кнопки Start)
    #     pyautogui.click()  # Сэмулировали нажатие левой кнопки

    @staticmethod
    def clickLeft(x, y):
        pyautogui.moveTo(x + 15, y + 15, 0, _pause=False)  # Передвинули мышку в левый нижний угол (в район кнопки Start)
        pyautogui.click()  # Сэмулировали нажатие левой кнопки
        pyautogui.click()  # Сэмулировали нажатие левой кнопки

    @staticmethod
    def clickRight(x, y):
        pyautogui.moveTo(x + 15, y + 15, 0, _pause=False)  # Передвинули мышку в левый нижний угол (в район кнопки Start)
        pyautogui.rightClick()  # Сэмулировали нажатие левой кнопки
        # pyautogui.click()  # Сэмулировали нажатие левой кнопки

    @staticmethod
    def clickMiddle(x, y):
        pyautogui.moveTo(x + 15, y + 15, 0, _pause=False)  # Передвинули мышку в левый нижний угол (в район кнопки Start)
        pyautogui.click(button='middle')  # Сэмулировали нажатие левой кнопки
