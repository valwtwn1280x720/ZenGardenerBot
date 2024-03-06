import pyautogui as pag
from funcpvz import *
import time

class Fumigador:
    def __init__(self) -> None:
        
        #Definicion de rutas // Routes definition
        self.ruta_fumigar_planta = r"images\fumigate_plant.png"
        self.ruta_fumigar = r"images\fumigate.png"
        
    #Funcion para agarrar el fumigador
    #Function for grabbing the pesticide
    def grab_fumigador(self):
        #almacena posicion / contains position
        needf = reconocer_img(self.ruta_fumigar, confianza=0.5) #this one fails a lot, i don't know why
        
        if needf is not None: #click en posicion / click on position
            moverse_posicion(needf,clicar="si",duracion=1.0)
    
    def fumigar(self):
        #almacena posicion / contains position
        need_fumigate = reconocer_img(self.ruta_fumigar_planta, confianza=0.85)
            
        if need_fumigate: #click en posicion / clicks on position
            print(f"Necesidad de fumigar en: {need_fumigate}")
            self.grab_fumigador()
            moverse_posicion(need_fumigate,clicar="si")
            #time for the action to finish
            time.sleep(1)
        #si no se encuentra se muestra el mensaje
        #If isn't found prints the message
        else:
            print("No se necesita fumigar")
            print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")

