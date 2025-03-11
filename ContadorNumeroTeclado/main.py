import tkinter as tk
from contadorapp import ContadorApp

def main():
    root = tk.Tk()
    root.title("Contador de Intentos")
    
    app = ContadorApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
