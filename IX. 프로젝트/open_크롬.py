import pyautogui as pag
import time

if __name__ == '__main__':
    #크롬이미지 인식하자
    data = pag.locateOnScreen("crome_icon.PNG")
    print(data)
    # 가운데 좌표 찾자
    #center = (data.left+(data.width/2),(data.height/2))
    center = pag.center(data)
    # 마우스 이동
    pag.moveTo(center,duration=2)
    # 더블클림하자
    pag.click()