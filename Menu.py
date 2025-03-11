import tkinter as tk
import subprocess
import os

def ejecutar_ejercicio(carpeta):
    ruta = os.path.join("C:\\Users\\Jade\\Documents\\EjerciciosDePython", carpeta, "main.py")
    if os.path.exists(ruta):
        print(f"Ejecutando: {ruta}")
        subprocess.run(["python", ruta])
    else:
        print(f"Error: No se encontró el archivo {ruta}")

def crear_boton(root, texto, carpeta):

    boton = tk.Button(root, text=texto, command=lambda: ejecutar_ejercicio(carpeta),
                      font=("Arial", 12, "bold"), fg="white", bg="#9854c2", activebackground="#C5A3E1", 
                      relief="flat", padx=20, pady=10, width=20)
    boton.pack(pady=10)  

def main():
    root = tk.Tk()
    root.title("Menu de Ejercicios")
    root.geometry("400x900")
    root.config(bg="#f2ebf3")  
    

    titulo = tk.Label(root, text="Seleccione el ejercicio", font=("Arial", 16, "bold"), fg="#333")
    titulo.pack(pady=20)


    ejercicios = [
        "AumentoTrabajador", "MontoTrabajador", "DescuentoMenores", 
        "DescuentoTotal", "NumeroMenor10", "Rango20", 
        "ContadorNumeroTeclado", "SumaNNumeros", "SumaHasta0", "SumaHasta100"
    ]
    
    for ejercicio in ejercicios:
        crear_boton(root, f"Ejercicio {ejercicio}", ejercicio)

    root.mainloop()

if __name__ == "__main__":
    main()
