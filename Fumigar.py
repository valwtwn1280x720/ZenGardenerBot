import pyautogui as pag
from funcpvz import *
import time

class Fumigador:
    def __init__(self) -> None:
        
        #Definicion de rutas
        self.ruta_fumigar_planta = r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\fumigate_plant.png"
        self.ruta_fumigar = r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\fumigate.png"
        
    #Funcion para agarrar el fumigador
    def grab_fumigador(self):
        #almacena posicion
        needf = reconocer_img(self.ruta_fumigar, confianza=0.5)
        
        if needf is not None: #click en posicion
            moverse_posicion(needf,clicar="si",duracion=1.0)
    
    def fumigar(self):
        #almacena posicion
        need_fumigate = reconocer_img(self.ruta_fumigar_planta, confianza=0.85)
            
        if need_fumigate: #click en posicion
            print(f"Necesidad de fumigar en: {need_fumigate}")
            self.grab_fumigador()
            moverse_posicion(need_fumigate,clicar="si")
            time.sleep(1)
        #si no se encuentra se muestra el mensaje
        else:
            print("No se necesita fumigar")
            print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")

