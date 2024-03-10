from funcpvz import * 
import time

class Fertilizador:
    def __init__(self) -> None:
        
        self.ruta_fertilizer = r"images\fertilizer.png"
        self.ruta_fertilize_plant = r"images\fertilize_plant.png"
        
        
    def grab_fertilizer(self):
        need = reconocer_img(self.ruta_fertilizer, confianza=0.8)
        if need:
            moverse_posicion(need, clicar="si")
    
    def fertilize(self):
        need_fert = reconocer_img(self.ruta_fertilize_plant, confianza=0.9)
        if need_fert:
            self.grab_fertilizer()
            moverse_posicion(need_fert,clicar="si")
        else:
            print("No se necesita fertilizante")
            print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
