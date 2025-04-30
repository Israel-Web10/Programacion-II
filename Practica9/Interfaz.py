import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero
    
    @abstractmethod
    def get_precio(self):
        pass
    
    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.get_precio():.1f}"

class Palco(Boleto):
    def get_precio(self):
        return 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion
    
    def get_precio(self):
        return 50.0 if self.dias_anticipacion >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion
    
    def get_precio(self):
        return 25.0 if self.dias_anticipacion >= 10 else 30.0

# Interfaz gráfica
class TeatroMunicipalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Boletos - Teatro Municipal")
        self.root.geometry("500x450")
        
        self.crear_widgets()
        self.boletos_vendidos = []
        self.actualizar_campos()
    
    def crear_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="Teatro Municipal", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(main_frame, text="Tipo de Boleto:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.tipo_boleto = tk.StringVar(value="palco")
        ttk.Radiobutton(main_frame, text="Palco (Bs. 100)", variable=self.tipo_boleto, value="palco").grid(row=1, column=1, sticky=tk.W)
        ttk.Radiobutton(main_frame, text="Platea (Bs. 50-60)", variable=self.tipo_boleto, value="platea").grid(row=2, column=1, sticky=tk.W)
        ttk.Radiobutton(main_frame, text="Galería (Bs. 25-30)", variable=self.tipo_boleto, value="galeria").grid(row=3, column=1, sticky=tk.W)
        
        ttk.Label(main_frame, text="Número de Boleto:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.numero_boleto = ttk.Entry(main_frame)
        self.numero_boleto.grid(row=4, column=1, sticky=tk.EW, pady=5)
        
        self.dias_frame = ttk.Frame(main_frame)
        self.dias_frame.grid(row=5, column=0, columnspan=2, pady=5, sticky=tk.EW)
        ttk.Label(self.dias_frame, text="Días de anticipación:").pack(side=tk.LEFT)
        self.dias_anticipacion = ttk.Entry(self.dias_frame, width=10)
        self.dias_anticipacion.pack(side=tk.LEFT, padx=5)
        
        self.tipo_boleto.trace_add('write', lambda *args: self.actualizar_campos())
        
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        ttk.Button(btn_frame, text="Obtener Boleto", command=self.obtener_boleto).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Mostrar Boletos", command=self.mostrar_boletos).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(main_frame, text="Información del Boleto:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.info_boleto = tk.Text(main_frame, height=8, width=50, state=tk.DISABLED)
        self.info_boleto.grid(row=8, column=0, columnspan=2, sticky=tk.EW)
        
        main_frame.columnconfigure(1, weight=1)
    
    def actualizar_campos(self):
        if self.tipo_boleto.get() == "palco":
            self.dias_frame.grid_remove()
        else:
            self.dias_frame.grid()
    
    def obtener_boleto(self):
        try:
            numero = int(self.numero_boleto.get())
            
            if self.tipo_boleto.get() == "palco":
                boleto = Palco(numero)
            elif self.tipo_boleto.get() == "platea":
                dias = int(self.dias_anticipacion.get())
                boleto = Platea(numero, dias)
            else:
                dias = int(self.dias_anticipacion.get())
                boleto = Galeria(numero, dias)
            
            self.boletos_vendidos.append(boleto)
            self.mostrar_info_boleto(boleto)
            
            self.numero_boleto.delete(0, tk.END)
            if self.tipo_boleto.get() != "palco":
                self.dias_anticipacion.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    
    def mostrar_info_boleto(self, boleto):
        self.info_boleto.config(state=tk.NORMAL)
        self.info_boleto.delete(1.0, tk.END)
        self.info_boleto.insert(tk.END, str(boleto))
        self.info_boleto.config(state=tk.DISABLED)
    
    def mostrar_boletos(self):
        if not self.boletos_vendidos:
            messagebox.showinfo("Boletos", "No hay boletos vendidos aún")
            return
        ventana = tk.Toplevel(self.root)
        ventana.title("Boletos Vendidos")
        ventana.geometry("500x400")
        
        frame = ttk.Frame(ventana)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scroll = ttk.Scrollbar(frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        texto = tk.Text(frame, yscrollcommand=scroll.set, wrap=tk.WORD)
        texto.pack(fill=tk.BOTH, expand=True)
        
        scroll.config(command=texto.yview)
        
        for boleto in self.boletos_vendidos:
            texto.insert(tk.END, f"• {boleto}\n\n")
        
        texto.config(state=tk.DISABLED)
if __name__ == "__main__":
    root = tk.Tk()
    app = TeatroMunicipalApp(root)
    root.mainloop()