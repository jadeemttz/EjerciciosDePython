import tkinter as tk
from rangoapp import RangoApp

def main():
    root = tk.Tk()
    root.title("Validación de Número (0-20)")
    app = RangoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
