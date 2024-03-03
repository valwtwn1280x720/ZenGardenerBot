import time

from funcpvz import *
from Regar import Regador
from CollectCoins import CoinCollecter
from Fumigar import Fumigador
from CajadeMusica import CajaMusical

#Creates the class that cointains all the other bots
class ZenGardenBot:
    def __init__(self) -> None:
        #Bots
        self.BotR = Regador()
        self.BotF = Fumigador()
        self.BotCM = CajaMusical()
        self.BotCC = CoinCollecter()

        #variable that confirms if the loop runs (=1) or not (=0)
        self.running_loop = 0

        #Pause time between the bots and CC (to be added to the options panel)
        self.pause_time = 0.8

    #main loop
    def gardenloop(self):
        while self.running_loop == 1:
            print("-----------------------------------")
            print("-----------------------------------")
            self.BotR.regar() #first one on execution
            self.BotF.fumigar() # second one
            self.BotCM.poner_musica() #third one
            time.sleep(0.3)
            #checks if runnign_loop was changed for it to break
            if self.running_loop == 0:
                break
            self.BotCC.collect() #fourth one with his many attemps
            time.sleep(self.pause_time) #pause time between 
            
            

if __name__ == "__main__":
    Zgb = ZenGardenBot()
    #Zgb.gui.mainloop()


