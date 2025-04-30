import tkinter as tk
from tkinter import ttk, messagebox
from Palco import Palco
from Galeria import Galeria
from Platea import Platea

class TeatroMunicipalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")

        tk.Label(root, text="Datos del Boleto", font=("Arial", 14)).pack(pady=10)
        
        self.ticket_type = tk.StringVar(value="Palco")
        tk.Radiobutton(root, text="Palco", variable=self.ticket_type, value="Palco").pack()
        tk.Radiobutton(root, text="Platea", variable=self.ticket_type, value="Platea").pack()
        tk.Radiobutton(root, text="Galeria", variable=self.ticket_type, value="Galeria").pack()

        tk.Label(root, text="Numero:").pack()
        self.numero_entry = tk.Entry(root)
        self.numero_entry.pack()
        self.numero_entry.insert(0, "1")

        tk.Label(root, text="Cant. Dias para el evento:").pack()
        self.dias_entry = tk.Entry(root)
        self.dias_entry.pack()
        self.dias_entry.insert(0, "0")

        tk.Button(root, text="Vende", command=self.vender).pack(pady=5)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

        tk.Label(root, text="INFORMACION", font=("Arial", 12)).pack(pady=10)
        self.info_label = tk.Label(root, text="")
        self.info_label.pack()

    def vender(self):
        try:
            numero = int(self.numero_entry.get())
            dias = int(self.dias_entry.get())
            ticket_type = self.ticket_type.get()
            
            if ticket_type == "Palco":
                boleto = Palco(numero)
            elif ticket_type == "Platea":
                boleto = Platea(numero, dias)
            else:
                boleto = Galeria(numero, dias)
                
            self.info_label.config(text=boleto.toString())
        except ValueError:
            messagebox.showerror("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = TeatroMunicipalApp(root)
    root.mainloop()
