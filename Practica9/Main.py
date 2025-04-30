import tkinter as tk
from tkinter import ttk
import random
from Cuadrado import Cuadrado
from Circulo import Circulo
from Coloreado import Coloreado

class FigurasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Objetos Coloreados")
        tk.Button(root, text="Generar Figuras", command=self.generar_figuras).pack(pady=10)
        self.resultados = tk.Text(root, height=15, width=50)
        self.resultados.pack(pady=10)

        tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

    def generar_figuras(self):
        self.resultados.delete(1.0, tk.END)  

        figuras = [None] * 5
        for i in range(len(figuras)):
            tipo = random.randint(1, 2) 
            valor = random.uniform(1, 11) 
            if tipo == 1:
                figuras[i] = Cuadrado(valor)
            else:
                figuras[i] = Circulo(valor)

            figuras[i].setColor(f"Color{i + 1}")
        for figura in figuras:
            self.resultados.insert(tk.END, f"{figura.toString()}\n")
            self.resultados.insert(tk.END, f"Area: {figura.area():.3f}\n")
            self.resultados.insert(tk.END, f"Perimetro: {figura.perimetro():.3f}\n")
            if isinstance(figura, Coloreado):
                self.resultados.insert(tk.END, f"Como colorear: {figura.comoColorear()}\n")
            self.resultados.insert(tk.END, "\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = FigurasApp(root)
    root.mainloop()