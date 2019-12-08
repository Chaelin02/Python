import pyautogui as pag
import time     #sleep 때문에 가져옴

if __name__ == '__main__':
    pag.moveTo(200,200,2)
    pag.click()
    pag.typewrite("happy birthday day to seungyeon!",interval=0.2)
    pag.press("enter")
    pag.typewrite("happy birthday to namkyeong!")
    pag.press("hangul")
    pag.typewrite("skaruddk toddlfcnrgkgo!!!!")\

