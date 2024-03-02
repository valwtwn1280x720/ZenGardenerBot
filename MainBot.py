import time

from funcpvz import *
from Regar import Regador
from CollectCoins import CoinCollecter
from Fumigar import Fumigador
from CajadeMusica import CajaMusical


class ZenGardenBot:
    def __init__(self) -> None:
        #Bots
        self.BotR = Regador()
        self.BotF = Fumigador()
        self.BotCM = CajaMusical()
        self.BotCC = CoinCollecter()
        
        self.running_loop = 0
        
        self.pause_time = 0.8
        
    def gardenloop(self):
        while self.running_loop == 1:
            print("-----------------------------------")
            print("-----------------------------------")
            self.BotR.regar()
            self.BotF.fumigar()
            self.BotCM.poner_musica()
            time.sleep(0.3)
            if self.running_loop == 0:
                break
            self.BotCC.collect()
            time.sleep(self.pause_time)
            
            

if __name__ == "__main__":
    Zgb = ZenGardenBot()
    #Zgb.gui.mainloop()


