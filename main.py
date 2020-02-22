from tkinter import *
from tkinter import ttk

#mainApp hereda de la clase Tk. Así tengo mi propia pantalla.
#no es una pantalla de "Tk", es una "mia"
class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    def __init__(self):
        #tenemos que llamar al constructor de la clase padre
        Tk.__init__(self)
        
        
        self.title("Termómetro")
        self.geometry("210x150")
        self.configure(bg="#ECECEC")
        self.resizable(0,0)
        
        self.temperatura = StringVar(value="")
        self.temperatura.trace("w", self.validateTemperature)
        self.tipoUnidad = StringVar(value="F")
        
        self.createLayout()
    #interesa que los metodos hagan una sola cosa.
    #así diferenciamos las cualidades de la ventana con el
    #contenido de la ventana
    def createLayout(self):
        #creamos el cuadrado de entrada de texto
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
        self.lblUnidad = ttk.Label(self, text="Grados:").place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable =self.tipoUnidad, value="F").place (x=20, y=70)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable =self.tipoUnidad, value="C").place(x=20, y=95)
        
    def start(self):
        self.mainloop()
        
    def validateTemperature(self, *args):
        print(self.temperatura.get())
        


if __name__ == '__main__':
    app = mainApp()
    app.start()

