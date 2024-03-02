import pyautogui as pag
from funcpvz import *
import time

class Regador:
    def __init__(self) -> None:
        
        #Se define las rutas de las imagenes necesarias a encontrar
        self.ruta_water = r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\water.png"
        self.ruta_regadera = r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\regadera.png"
    
    #Funcion para agarrar la regadera
    def grab_regadera(self):
        #busca la imagen y la posicion la almacena en need
        need = reconocer_img(self.ruta_regadera,confianza=0.9)
        
        if need: #si need no es None se mueve y clickea en esa posicion
            moverse_posicion(need,clicar="si")
            
    def regar(self):
        #busca imagen y almacena su posicion
        need_water = reconocer_img(self.ruta_water, confianza=0.85)
        
        #si se encuentra
        if need_water:
            print(f"Agua Encontrada: {need_water}")
            self.grab_regadera()
            moverse_posicion(need_water,clicar="si")
            time.sleep(1)
        #si no se encuentra se muestra el mensaje
        else:
            print("No se necesita agua")
            print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")