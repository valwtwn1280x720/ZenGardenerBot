import pyautogui as pag
from funcpvz import *
import time

#Create the class coincollecter
class CoinCollecter:
    def __init__(self) -> None:
        
        #Defino las rutas con las imagenes de la moneda de 10 de Plants vs Zombies
        #En diferentes instancias de su movimiento en una lista

        #Define the routes with the multiple 10 coin images from PvZ
        #In different instances of it's movement

        self.coin_10_rutas = [
            r"images\silver_coin\one_.png",
            r"images\silver_coin\three_.png",
            r"images\silver_coin\four_.png",
            r"images\silver_coin\five_.png"
        ]
        
        #Intentos que tiene el bot para encontrar monedas
        #Number of tries that the bot has to find coins in the screen
        self.coin_tries = 5

    #Main function to collect
    def collect(self):
        #for loop with the number of tries
        for c in range(self.coin_tries):
            #Crea la variable result que almacena la posición de alguna de las imagenes que encuentre
            #Creates the variable result that contains the position of any of the images it founds
            result = reconocer_coins(self.coin_10_rutas)
    
            #Busca si result es distinto de None // Search if result isn't None
            if result != None:
                #Si es distinto muestra la posición en consola // If isn't None prints the position 
                print(f"Moneda Encontrada: {result}")
                moverse_posicion(result,clicar="si")
            else:
                print(f"{c+1}. No hay/No veo monedas")
                
                pass
