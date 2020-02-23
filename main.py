from tkinter import *
from tkinter import ttk

#mainApp hereda de la clase Tk. Así tengo mi propia pantalla.
#no es una pantalla de "Tk", es una "mia"
class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    #para guardar la temperatura previa
    __temperaturaAnt = ""
    
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
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable =self.tipoUnidad, value="F", command=self.selected).place (x=20, y=70)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable =self.tipoUnidad, value="C", command=self.selected).place(x=20, y=95)
        
    def start(self):
        self.mainloop()
        
    def validateTemperature(self, *args):
        nuevoValor = self.temperatura.get()
        print("nuevo valor: ", nuevoValor)
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
            print("fija valor anterior a: ", self.__temperaturaAnt)
        except:
            self.temperatura.set(self.__temperaturaAnt)
            print("recupera valor anterior: ", self.__temperaturaAnt)
            
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados-32) * 5/9
        else:
            resultado = grados
        
        self.temperatura.set(resultado)


if __name__ == '__main__':
    app = mainApp()
    app.start()

