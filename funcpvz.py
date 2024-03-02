import pyautogui as pag
import time

#click en la posicion a la que se movió el cursos
def click(doble="no"):
    if doble=="si":pag.doubleClick()
    else:
        pag.mouseDown()
        time.sleep(0.01)
        pag.mouseUp()

#reconocer si la imagen se encuentra en pantalla
def reconocer_coins(list_img):
    for ubicacion in list_img:
        try:
            ubicacion_coin = pag.locateCenterOnScreen(ubicacion, confidence=0.75)
            if ubicacion_coin:
                return list(ubicacion_coin)
        except pag.ImageNotFoundException:
            pass
        

#moverse a una posicion especifica
def moverse_posicion(coords, clicar="no", duracion=0.001):
    pag.moveTo(coords[0], coords[1], duration=duracion)
    if clicar=="si":
        click()
    else:pass

def reconocer_img(ruta,confianza):
    try:
        ubicacion = pag.locateCenterOnScreen(ruta, confidence=confianza)
        return list(ubicacion)
    except pag.ImageNotFoundException:
        return None
