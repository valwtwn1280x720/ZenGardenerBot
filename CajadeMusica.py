import pyautogui as pag
from funcpvz import *
import time

class CajaMusical:
    def __init__(self) -> None:
        
        #definicion de rutas // routes definition
        self.ruta_musica = r"images\music_plant.png"
        self.ruta_cajamusica = r"images\music_box.png"
        
    #Agarrar la caja // Grab the musicbox
    def grab_caja(self):
        #contains the position
        caja = reconocer_img(self.ruta_cajamusica, confianza=0.9)
        if caja:
            moverse_posicion(caja,clicar="si") #moves to it and clicks it

    #The main function
    def poner_musica(self):
        #Searchs if the image is in screen
        need_music = reconocer_img(self.ruta_musica, confianza=0.85)
            
        if need_music:
            #If it is prints the position, moves to it and click
            print(f"Musica necesitada en: {need_music}")
            self.grab_caja()
            moverse_posicion(need_music,clicar="si")
            #time pause for the thing to finish
            time.sleep(1.5)
        else:
            #If can't be seen prints this
            print("No se necesita musica")
            print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
    

