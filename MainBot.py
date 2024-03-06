import time

from funcpvz import *
from Regar import Regador
from CollectCoins import CoinCollecter
from Fumigar import Fumigador
from CajadeMusica import CajaMusical
from Fertilizer import Fertilizador

#Creates the class that cointains all the other bots
class ZenGardenBot:
    def __init__(self) -> None:
        #Bots
        self.BotR = Regador()
        self.BotF = Fumigador()
        self.BotCM = CajaMusical()
        self.BotCC = CoinCollecter()
        self.BotFer = Fertilizador()

        #variable that confirms if the loop runs or not
        self.is_running_loop = False

        #Pause time between the bots and CC (to be added to the options panel)
        self.pause_time = 0.8

    #main loop
    def gardenloop(self):
        while self.is_running_loop:
            print("-----------------------------------")
            print("-----------------------------------")
            self.BotR.regar() #first one on execution
            self.BotF.fumigar() # second one
            self.BotCM.poner_musica() #third one
            self.BotFer.fertilize()
            time.sleep(0.3)
            #checks if is_runnign_loop was changed for it to break
            if self.is_running_loop is not True:
                break
            self.BotCC.collect() #fourth one with his many attemps
            time.sleep(self.pause_time) #pause time between 
            
            

if __name__ == "__main__":
    Zgb = ZenGardenBot()
    #Zgb.gui.mainloop()


