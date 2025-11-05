            BoxLayout:
               orientation: 'lr'
               TextInput:
                   id: exp_inp
                   size_hint_x: None #Le decimos que no use size_hint para el ancho
                   width: root.width - 100
            # un ancho fijo o calculado, por ejemplo, el ancho total menos 100x
                   # ... otras propiedades
                Button:
                   id: respuesta
                   size_hint_x: 0.2
            # ocupa el 20% del ancho disponible
                   # ... otras propiedades           
           
           

             Button: 
            id: respuesta 
            size_hint_y: .15 
            background_normal: '' 
            background_color: hex('#faf7f7ff') 
            font_size: 25 
            text_size: self.size 
            halign: 'right' 
            color: 0,0,0,1 
            on_release: root.respuesta(self.text) 
        TextInput: 
            id: exp_inp 
            multiline: False 
            font_size: 25 
            size_hint_y: .25 
            on_text_validate: root.igual() 
           
 Button: 
            id: respuesta 
            size_hint_y: .15 
            background_normal: '' 
            background_color: hex('#faf7f7ff') 
            font_size: 25 
            text_size: self.size 
            halign: 'right' 
            color: 0,0,0,1 
            on_release: root.respuesta(self.text) 
        TextInput: 
            id: exp_inp 
            multiline: False 
            font_size: 25 
            size_hint_y: .25 
            on_text_validate: root.igual() 




           
            Button: 
                id: clear 
                text: 'C' 
                on_release: root.borrar(self.text) 
            Button: 
                id: clear_entry 
                text: 'CE' 
                on_release: root.borrar(self.text) 
            Button: 
                id: delate 
                text: 'Del' 
                on_release: root.borrar(self.text) 
            Button: 
                id: dividir 
                text: '/' 
                on_release: root.ids.exp_inp.insert_text(self.text) 



            Button: 
                id: sumar 
                text: '+' 
                on_release: root.ids.exp_inp.insert_text(self.text) 