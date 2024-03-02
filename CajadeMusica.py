import pyautogui as pag
from funcpvz import *
import time

class CajaMusical:
    def __init__(self) -> None:
        
        #definicion de rutas
        self.ruta_musica = r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\music_plant.png"
        self.ruta_cajamusica = r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\music_box.png"
        
    #Agarrar la caja
    def grab_caja(self):
        caja = reconocer_img(self.ruta_cajamusica, confianza=0.9)
        if caja:
            moverse_posicion(caja,clicar="si")
            
    def poner_musica(self):
        need_music = reconocer_img(self.ruta_musica, confianza=0.85)
            
        if need_music:
            print(f"Musica necesitada en: {need_music}")
            self.grab_caja()
            moverse_posicion(need_music,clicar="si")
            time.sleep(1.5)
        else:
            print("No se necesita musica")
            print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
    

