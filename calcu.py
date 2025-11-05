from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 

class Calculadora (BoxLayout): 
    def __init__ (self,  **kwargs): 
        super(). __init__ (**kwargs) 

    def borrar(self, tipo): 
        if tipo == 'C': 
            self.ids.exp_inp.text = '' 
            self.ids.respuesta.text = '' 
        if tipo == 'CE': 
            self.ids.exp_inp.text = '' 
        if tipo == 'Del': 
            nuevo = self.ids.exp_inp.text[:-1] 
            self.ids.exp_inp.text = nuevo 

    def igual (self): 
        expresion = self.ids.exp_inp.text 
        try: 
            resultado = eval (expresion) 
            self.ids.respuesta.text = str (resultado) 
            self.ids.exp_inp.text = '' 
            self.ids.error.text = '' 
        except: 
            self.ids.error.text = 'error'

    def respuesta (self, resp): 
        self.ids.exp_inp.text = resp 
        self.ids.respuesta.text = '' 

class calcuApp  (App): 
    def build (self): 
        return Calculadora() 

if __name__=='__main__': 
    calcuApp().run()