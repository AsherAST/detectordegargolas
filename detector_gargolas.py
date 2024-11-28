import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk
import os

class DetectorGargolas:
    def __init__(self):
        # Inicializar la ventana principal
        self.root = tk.Tk()
        self.root.title("Detector de Gárgolas")
        self.root.geometry("400x400")
        
        # Obtener la ruta del directorio actual
        self.directorio = os.path.dirname(os.path.abspath(__file__))
        
        # Inicializar pygame para el sonido
        pygame.mixer.init()
        
        # Crear el título
        titulo = tk.Label(self.root, 
                         text="DETECTOR DE GÁRGOLAS", 
                         font=('Arial', 20, 'bold'))  # Fuente más grande y negrita
        titulo.pack(pady=20)
        
        # Crear el botón inicial
        self.btn_iniciar = tk.Button(self.root, 
                                   text="Iniciar", 
                                   font=('Arial', 12),  # Fuente más grande para el botón
                                   width=10,  # Ancho del botón
                                   height=1)  # Alto del botón
        self.btn_iniciar.config(command=self.primera_pregunta)
        self.btn_iniciar.pack(pady=20)
        
        try:
            # Preparar las imágenes usando rutas relativas
            ruta_gargola = os.path.join(self.directorio, "gargola.jpg")
            ruta_no_gargola = os.path.join(self.directorio, "no_gargola.jpg")
            
            self.img_gargola = ImageTk.PhotoImage(Image.open(ruta_gargola).resize((300, 300)))
            self.img_no_gargola = ImageTk.PhotoImage(Image.open(ruta_no_gargola).resize((300, 300)))
            
        except Exception as e:
            messagebox.showerror("Error", f"No se encontraron las imágenes. Asegúrate de que 'gargola.jpg' y 'no_gargola.jpg' estén en la misma carpeta que el programa.\nError: {str(e)}")
            self.root.destroy()
            return
        
        # Crear label para mostrar imágenes
        self.lbl_imagen = tk.Label(self.root)
        self.lbl_imagen.pack(pady=10)
        
    def primera_pregunta(self):
        respuesta = messagebox.askyesno("Primera Pregunta", "¿Te encanta salir de noche?")
        if respuesta:
            self.segunda_pregunta()
        else:
            self.mostrar_no_gargola()
    
    def segunda_pregunta(self):
        respuesta = messagebox.askyesno("Segunda Pregunta", "¿Le temes a la oscuridad?")
        if not respuesta:
            self.mostrar_gargola()
        else:
            self.mostrar_no_gargola()
    
    def mostrar_gargola(self):
        self.lbl_imagen.configure(image=self.img_gargola)
        try:
            pygame.mixer.music.load(os.path.join(self.directorio, "sonido_gargola.mp3"))
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", "No se encontró el archivo de sonido 'sonido_gargola.mp3'")
        messagebox.showinfo("Resultado", "¡Eres una gárgola!")
    
    def mostrar_no_gargola(self):
        self.lbl_imagen.configure(image=self.img_no_gargola)
        messagebox.showinfo("Resultado", "No eres una gárgola")
    
    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DetectorGargolas()
    app.iniciar()