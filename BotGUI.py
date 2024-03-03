import threading

from customtkinter import *
from MainBot import ZenGardenBot

#define the zengardenbot
ZGB = ZenGardenBot()

#create the class BotWin that is the GUI for the bot (it still uses the console to provide the information)
class BotWin(CTk):
    def __init__(self, mainbot):
        super().__init__()
        self.mainbot = mainbot
        self.options_panel = None
        self.bot_isrunning = False
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.geometry("480x360")
        self.title("Zen Gardener")
        self.icon = r"C:\Users\usuario\Desktop\Thingsss\ZenGardenerBot\images\icon_gui.ico"
        self.config_ico = r"" #useless, can't remember (I think it was the icon for the options panel)
        self.iconbitmap(self.icon)
        
        #frames
        self.intro_Frame = CTkFrame(self)
        self.intro_Frame.pack(side=TOP)
        
        self.intro_buttons_Frame = CTkFrame(self)
        self.intro_buttons_Frame.pack(side=BOTTOM)
        
        #labels
        #You can traduce this if you want but isn't neccesary, i didn't know what to put in the window
        self.instrucciones ='''
Instrucciones:
1_. Este programa se compone de 4 bots:
Regador, Fumigador, CajaMusical y CoinCollecter.
Y se ejecutan en el orden ya escrito. \n
2_. En opciones puedes configurar cosas como:
las oportunidades de CoinCollecter, en cuanto
tiempo quieres que el bot se ejecute, etc. \n
3_. Una vez todo listo, dale a comenzar, con PvZ
ya abierto en el jardin Zen'''
        
        self.intro_label = CTkLabel(self.intro_Frame,text="Zen Gardener",
                                    font=("Arial",32,"bold","underline"),
                                    text_color="light green")
        self.intro_label.pack(pady=10,padx=10,side="top")
        
        self.instrucciones_label = CTkLabel(self.intro_Frame, text=self.instrucciones,
                                            anchor=W,font=("Calibri",16))
        self.instrucciones_label.pack(side=LEFT,pady=7)
        
        #botones, buttons
        self.start_stop_button = CTkButton(self.intro_buttons_Frame,command=self.change_state,
                                           text="Comenzar",fg_color="Green",hover=False)
        self.start_stop_button.pack(side="left",padx=5,pady=10)
        
        self.options_button = CTkButton(self.intro_buttons_Frame,text="Opciones",
                                        command=self.open_options,hover=False)
        self.options_button.pack(side="left",padx=5,pady=10)

    #Starts the loop from MainBot (solution given by chatgpt, didn't know how to do it)
    def start_botloop(self):
        self.botloop_thread = threading.Thread(target=self.mainbot.gardenloop)
        self.botloop_thread.start()
        
    def change_state(self):
        #Convierte bot_isrunning en true si es false y viceversa
        #Convert bot_isrunning to true if false and vice versa
        if self.bot_isrunning == False:
            self.bot_isrunning = True
            
            self.start_stop()
            
        else:
            self.bot_isrunning = False
            
            self.start_stop()
            
        # Si está corriendo, establece el botón a rojo con el texto "Detener"
        # If it is running, set the button to red with the text "Stop"
        if self.bot_isrunning:
            change = lambda: self.start_stop_button.configure(text="Detener",fg_color="Red")
            self.start_stop_button.after(100, change)
            #desactiva el boton de opciones // deactivate the options button
            self.options_button.configure(state="disabled")
        else:
            change = lambda: self.start_stop_button.configure(text="Comenzar",fg_color="Green")
            self.start_stop_button.after(100, change)
            #lo activa si no se ejecuta el bot // activates it if the bot is not running
            self.options_button.configure(state="normal")
    #if bot_isrunning is true it sets to 1 mainbot.running_loop for that loop to start    
    def start_stop(self):
        if self.bot_isrunning == True:
            self.mainbot.running_loop = 1
            self.start_botloop()
        else:
            self.mainbot.running_loop = 0
    #Opens the option panel if the bot isn't running    
    def open_options(self):
        if self.bot_isrunning == False:
            self.options_panel = self.OptionWin(master=self,botcc=self.mainbot.BotCC)
        else:
            pass
    #This exists because before it if you close the main window without stopping the loop it would be still running    
    def on_closing(self):
        self.mainbot.running_loop = 0
        self.destroy()
        sys.exit()
        
    #Creates a class for the options window (didn't know if make this outside the class or as a function)    
    class OptionWin(CTkToplevel):
        #initiates with the parameters master and botcc (coin collecter)
        def __init__(self, master,botcc):
            super().__init__()
            self.botcc = botcc
            
            #ventana // window
            self.title("Opciones")
            self.iconbitmap(master.icon)
        
            #frames
            self.options_frame = CTkFrame(self,width=280,height=180)
            self.options_frame.pack(side=TOP,pady=10)

            #boton de aplicar y cancelar
            #apply and cancel button
        
            self.opt_aplicar = CTkButton(self, text="Aplicar",command=self.aplicar,
                                     fg_color="Green")
            self.opt_aplicar.pack(side=LEFT,pady=5,padx=10)
        
            self.opt_cancelar = CTkButton(self, text="Cancelar",
                                      fg_color="Red",command=self.withdraw)
            self.opt_cancelar.pack(side=LEFT,pady=5,padx=10)
        
            #opciones // options
            
            #oportunidades de CoinCollecter (opr_cc)
            #number of opportunities of CC to find coins on the screen (variable names here are super messy, sorry)
            self.opr_cc_label = CTkLabel(self.options_frame,
                                    text="Oportunidades de Coin Collecter:")
            self.opr_cc_label.grid(row=0,column=0,padx=5,pady=15)
        
            #lista de opciones/oportunidades // opportunities/options list
            self.opr_num = [5,10,15,20]
            self.opr_num_str = ["5","10","15","20"]
            self.opr_var = StringVar(self.options_frame,self.opr_num_str[0])
            #menu para cambiar / menu to change it
            self.opr_cc = CTkOptionMenu(self.options_frame,values=self.opr_num_str,
                                    variable=self.opr_var,fg_color="Grey",
                                    button_color="Black",width=50,height=20)
            self.opr_cc.grid(row=0,column=1,padx=5)
            
        #Funciones // Functions
        #applies the option selected above
        def opr_cc_guardado(self):
            oprn = self.opr_cc.get()
            #don't know how to explain this, it just made sense to me
            for i in self.opr_num:
                if int(oprn) == i:
                    self.botcc.coin_tries = i

        #applies all the changes (only 1 option for now) and closes the options panel
        def aplicar(self):
            self.opr_cc_guardado()
            self.withdraw()

        
        
        
#I read this was a good practice so i write this in every single file i work on 
if __name__ == "__main__":
    root = BotWin(ZGB)
    root.mainloop()
    
    
    
