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
    def click(x,y):
        pyautogui.moveTo(x, y)  # Передвинули мышку в левый нижний угол (в район кнопки Start)
        pyautogui.click()  # Сэмулировали нажатие левой кнопки
        pyautogui.click()  # Сэмулировали нажатие левой кнопки