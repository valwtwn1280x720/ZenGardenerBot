import pyautogui as pag
from funcpvz import *
import time

class Regador:
    def __init__(self) -> None:
        
        #Se define las rutas de las imagenes necesarias a encontrar
        #Defines the images routes
        self.ruta_water = r"images\water.png"
        self.ruta_regadera = r"images\regadera.png"
    
    #Funcion para agarrar la regadera / grab the watering can
    def grab_regadera(self):
        #busca la imagen y la posicion la almacena en need 
        #contains position
        need = reconocer_img(self.ruta_regadera,confianza=0.9)
        
        if need: #si need no es None se mueve y clickea en esa posicion
            moverse_posicion(need,clicar="si")
            
    def regar(self):
        #busca imagen y almacena su posicion
        #contains position
        need_water = reconocer_img(self.ruta_water, confianza=0.85)
        
        #si se encuentra
        #if its found
        if need_water:
            print(f"Agua Encontrada: {need_water}")
            self.grab_regadera()
            moverse_posicion(need_water,clicar="si")
            time.sleep(1)
        #si no se encuentra se muestra el mensaje
        #if it isn't found
        else:
            print("No se necesita agua")
            print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
