import pyautogui as pag
from funcpvz import *
import time

class CoinCollecter:
    def __init__(self) -> None:
        
        #Defino las rutas con las imagenes de la moneda de 10 de Plants vs Zombies
        #En diferentes instancias de su movimiento en una lista

        self.coin_10_rutas = [
            r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\silver_coin\one_.png",
            r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\silver_coin\three_.png",
            r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\silver_coin\four_.png",
            r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\silver_coin\five_.png"
        ]
        
        #Intentos que tiene el bot para encontrar monedas
        self.coin_tries = 5
        
    def collect(self):
        for c in range(self.coin_tries):
            #Crea la variable result que almacena la posición de alguna de las imagenes que encuentre
            result = reconocer_coins(self.coin_10_rutas)
    
            #Busca si result es distinto de None
            if result != None:
                #Si es distinto muestra la posición en consola
                print(f"Moneda Encontrada: {result}")
                #se mueve y clickea
                moverse_posicion(result,clicar="si")
            else:
                #Muestra "No se puede ver" en consola para mas claridad al usuario
                print(f"{c+1}. No hay/No veo monedas")
                #Si result no es distinto de None, pasa a la siguiente vuelta
                pass