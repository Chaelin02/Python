import pyautogui as pag
import time
if __name__ == '__main__':
    pag.moveTo(100, 1100, 2)
    pag.click()
    pag.typewrite("notepad",interval=0.2)
    pag.press("enter")
    pag.moveTo(200, 200, 2)
    pag.typewrite("hello world")
    pag.press("enter")
    pag.press("enter")
    pag.press("hangul")
    pag.typewrite(" qksrkqrnsk tptkddk ~")
    pag.press("hangul")
    pag.hotkey('ctrl','s')
    pag.sleep(1)
    pag.typewrite("C:\\Users\\chaelin\\")
    pag.press("hangul")
    pag.typewrite("vkdlTjsdnjfem")
    pag.hotkey('S')



    #메모장 실행
    #hello world 치자
    #두번 내리자 
    #반갑구나 세상아 치자 
    #저장
    #파이썬 월ㄷ