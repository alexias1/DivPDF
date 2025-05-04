import pywhatkit as kit
import pyautogui
import time

def EnviarPDF(PDF, numero, messagem, nome):

    kit.sendwhatmsg_instantly(numero, messagem, wait_time=15, tab_close=False)
    time.sleep(5)
    pyautogui.press("enter")

    pass

