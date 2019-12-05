import pyautogui as pag

if __name__=='__main__':
    pag.moveTo(498,47, duration=2)
    pag.click(clicks=2)     #더블클릭3
    # pag.click()   더블클릭1
    # pag.doubleClick() 더블클릭2
    # pag.move(100,200,duration=1)
    # pag.rightClick()
    # pag.click(button="right")

pag.drag(0,200,duration=1)