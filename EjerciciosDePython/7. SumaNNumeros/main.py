import tkinter as tk
from sumannumapp import SumaApp

def main():
    root = tk.Tk()
    root.title("Suma de N números")
    
    app = SumaApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
