import pyautogui as pag
import time

#click en la posicion a la que se movió el cursos
#click func
def click(doble="no"):
    if doble=="si":pag.doubleClick()
    else:
        pag.mouseDown()
        time.sleep(0.01)
        pag.mouseUp()

#reconocer si la imagen se encuentra en pantalla
#Recognize multiple instances of an object on screen
def reconocer_coins(list_img): #list of routes
    for ubicacion in list_img:
        try:
            ubicacion_coin = pag.locateCenterOnScreen(ubicacion, confidence=0.75)
            if ubicacion_coin:
                return list(ubicacion_coin)
        except pag.ImageNotFoundException:
            pass
        

#moverse a una posicion especifica
#Moves to the coords given, and clicks or no
def moverse_posicion(coords, clicar="no", duracion=0.001):
    pag.moveTo(coords[0], coords[1], duration=duracion)
    if clicar=="si":
        click()
    else:pass

#Only recognizes one image/ instance of an object on screen (for those who don't move)
def reconocer_img(ruta,confianza):
    try:
        ubicacion = pag.locateCenterOnScreen(ruta, confidence=confianza)
        return list(ubicacion)
    except pag.ImageNotFoundException:
        return None
