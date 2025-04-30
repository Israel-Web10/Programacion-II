import tkinter as tk
from tkinter import ttk, messagebox
from sistema_boletos import Boleto, Palco, Platea, Galeria  # Importamos las clases del sistema anterior

class TeatroMunicipalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Boletos - Teatro Municipal")
        self.root.geometry("500x400")
        
        self.crear_widgets()
        self.boletos_vendidos = []
    
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="Teatro Municipal", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Tipo de boleto
        ttk.Label(main_frame, text="Tipo de Boleto:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.tipo_boleto = tk.StringVar(value="palco")
        ttk.Radiobutton(main_frame, text="Palco", variable=self.tipo_boleto, value="palco").grid(row=1, column=1, sticky=tk.W)
        ttk.Radiobutton(main_frame, text="Platea", variable=self.tipo_boleto, value="platea").grid(row=2, column=1, sticky=tk.W)
        ttk.Radiobutton(main_frame, text="Galería", variable=self.tipo_boleto, value="galeria").grid(row=3, column=1, sticky=tk.W)
        
        # Número de boleto
        ttk.Label(main_frame, text="Número de Boleto:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.numero_boleto = ttk.Entry(main_frame)
        self.numero_boleto.grid(row=4, column=1, sticky=tk.EW, pady=5)
        
        # Días de anticipación (solo para platea y galería)
        self.dias_frame = ttk.Frame(main_frame)
        self.dias_frame.grid(row=5, column=0, columnspan=2, pady=5, sticky=tk.EW)
        ttk.Label(self.dias_frame, text="Días de anticipación:").pack(side=tk.LEFT)
        self.dias_anticipacion = ttk.Entry(self.dias_frame, width=10)
        self.dias_anticipacion.pack(side=tk.LEFT, padx=5)
        
        # Actualizar visibilidad de días de anticipación
        self.tipo_boleto.trace_add('write', self.actualizar_campos)
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        ttk.Button(btn_frame, text="Obtener Boleto", command=self.obtener_boleto).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Mostrar Boletos", command=self.mostrar_boletos).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
        # Área de información
        ttk.Label(main_frame, text="Información del Boleto:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.info_boleto = tk.Text(main_frame, height=5, width=40, state=tk.DISABLED)
        self.info_boleto.grid(row=8, column=0, columnspan=2, sticky=tk.EW)
        
        # Configurar grid
        main_frame.columnconfigure(1, weight=1)
    
    def actualizar_campos(self, *args):
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
            else:  # galeria
                dias = int(self.dias_anticipacion.get())
                boleto = Galeria(numero, dias)
            
            self.boletos_vendidos.append(boleto)
            self.mostrar_info_boleto(boleto)
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")
    
    def mostrar_info_boleto(self, boleto):
        self.info_boleto.config(state=tk.NORMAL)
        self.info_boleto.delete(1.0, tk.END)
        self.info_boleto.insert(tk.END, str(boleto))
        self.info_boleto.config(state=tk.DISABLED)
    
    def mostrar_boletos(self):
        if not self.boletos_vendidos:
            messagebox.showinfo("Boletos", "No hay boletos vendidos aún")
            return
        
        ventana_boletos = tk.Toplevel(self.root)
        ventana_boletos.title("Boletos Vendidos")
        
        texto = tk.Text(ventana_boletos, width=50, height=15)
        scroll = ttk.Scrollbar(ventana_boletos, command=texto.yview)
        texto.configure(yscrollcommand=scroll.set)
        
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        texto.pack(fill=tk.BOTH, expand=True)
        
        for boleto in self.boletos_vendidos:
            texto.insert(tk.END, str(boleto) + "\n")
        
        texto.config(state=tk.DISABLED)

if __name__ == "_main_":
    root = tk.Tk()
    app = TeatroMunicipalApp(root)
    root.mainloop()