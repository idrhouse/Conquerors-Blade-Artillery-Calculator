import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

# Diccionario de artillerías con sus materiales
artillerias = {
    "Metralla verde": {"Hierro en bruto": 200, "Madera seca": 50, "Cobre en bruto": 50, "Piedra en bruto": 50, "Plata": 250},
    "Metralla azul": {"Hierro fundido": 100, "Madera alisada": 50, "Cobre mejorado": 100, "Piedra cortada": 50, "Plata": 500},
    "Metralla morada": {"Hierro fundido": 200, "Madera alisada": 100, "Cobre mejorado": 100, "Piedra cortada": 100, "Plata": 1000},

    "Vacio": {"Cobre en bruto": 0, "Madera seca": 0, "Hierro en bruto": 0, "Piedra en bruto": 0, "Plata": 0},
    "Mortero azul": {"Cobre mejorado": 100, "Hierro fundido": 100, "Piedra cortada": 50, "Madera alisada": 50, "Plata": 500},
    "Mortero morado": {"Cobre mejorado": 200, "Hierro fundido": 200, "Piedra cortada": 100, "Madera alisada": 100, "Plata": 1000},

    "Culebrina verde": {"Cobre en bruto": 200, "Madera seca": 50, "Hierro en bruto": 50, "Piedra en bruto": 50, "Plata": 250},
    "Culebrina azul": {"Cobre mejorado": 100, "Madera alisada": 50, "Hierro fundido": 50, "Piedra cortada": 50, "Plata": 500},
    "Culebrina morada": {"Cobre mejorado": 200, "Madera alisada": 100, "Hierro fundido": 100, "Piedra cortada": 100, "Plata": 1000},
    
    "Balista verde": {"Madera seca": 200, "Hierro en bruto": 100, "Cuero curtido": 50, "Tela aspera": 50, "Plata": 250},
    "Balista azul": {"Madera alisada": 100, "Hierro fundido": 50, "Cuero tratado": 50, "Tela barata": 50, "Plata": 500},
    "Balista morada": {"Madera alisada": 200, "Hierro fundido": 100, "Cuero tratado": 100, "Tela barata": 100, "Plata": 1000},

    "Cañon verde": {"Cobre en bruto": 200, "Madera seca": 50, "Hierro en bruto": 50, "Piedra en bruto": 50, "Plata": 250},
    "Cañon azul": {"Cobre mejorado": 100, "Madera alisada": 50, "Hierro fundido": 50, "Piedra cortada": 50, "Plata": 500},
    "Cañon morado": {"Cobre mejorado": 200, "Madera alisada": 100, "Hierro fundido": 100, "Piedra cortada": 100, "Plata": 1000},
}

# Función para calcular los materiales
def calcular_materiales():
    try:
        cantidad = int(entry_cantidad.get())
        if artilleria_seleccionada:
            materiales_necesarios = {}
            for material, cantidad_base in artillerias[artilleria_seleccionada].items():
                materiales_necesarios[material] = cantidad_base * cantidad
            
            # Limpiar el frame de resultados
            for widget in frame_resultado.winfo_children():
                widget.destroy()
            
            resultado_texto = f"Materiales necesarios para \n{cantidad} {artilleria_seleccionada}(s):"
            label_resultado = tk.Label(frame_resultado, text=resultado_texto, bg="#f0f0f0", font=("Helvetica", 12, "bold"))
            label_resultado.grid(row=0, column=0, columnspan=2, pady=5)
            
            # Mostrar cada material con su imagen y cantidad
            row = 1  # Comenzar en la segunda fila
            for material, total in materiales_necesarios.items():
                # Mostrar texto del material
                label_material = tk.Label(frame_resultado, text=f"{material}: {total}", bg="#f0f0f0", font=("Helvetica", 10))
                label_material.grid(row=row, column=0, pady=2, sticky="w")  # Alinear a la izquierda
                
                # Mostrar imagen del material
                if material in imagenes_materiales:
                    imagen_label = tk.Label(frame_resultado, image=imagenes_materiales[material], bg="#f0f0f0")
                    imagen_label.grid(row=row, column=1, padx=5, pady=2)
                
                row += 1  # Mover a la siguiente fila

        else:
            # Si no se seleccionó ninguna artillería, mostrar un mensaje en el frame de resultado
            for widget in frame_resultado.winfo_children():
                widget.destroy()
            label_error = tk.Label(frame_resultado, text="Por favor selecciona una artillería.", bg="#f0f0f0", fg="red", font=("Helvetica", 10, "italic"))
            label_error.grid(row=0, column=0, columnspan=2, pady=2)

    except ValueError:
        label_error = tk.Label(frame_resultado, text="Por favor ingresa un número válido.", bg="#f0f0f0", fg="red", font=("Helvetica", 10, "italic"))
        label_error.grid(row=0, column=0, columnspan=2, pady=2)

# Función para seleccionar la artillería al hacer clic en la imagen
def seleccionar_artilleria(artilleria):
    global artilleria_seleccionada
    artilleria_seleccionada = artilleria
    label_seleccion.config(text=f"Artillería seleccionada: {artilleria}")
    entry_cantidad.delete(0, tk.END)  # Limpiar el campo de texto
    entry_cantidad.insert(0, "1")     # Insertar valor 1
    
    # Calcular los materiales automáticamente para 1 unidad
    calcular_materiales()

def resource_path(relative_path):
    """Obtiene la ruta del recurso ya sea en desarrollo o en el ejecutable"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Crafteo con Imágenes de Conquerors Blade")
ventana.geometry("720x620")

# Agregar imagen de fondo
imagen_fondo = Image.open(resource_path("./extras/fondo2.png"))
imagen_fondo = imagen_fondo.resize((720,620))  # Ajustar tamaño
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
label_fondo = tk.Label(ventana, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Frame para contener las artillerías y resultados
frame_principal = tk.Frame(ventana, bg="#f0f0f0")
frame_principal.pack(pady=2)

# Frame para las artillerías
frame_artillerias = tk.Frame(frame_principal, bg="#f0f0f0")
frame_artillerias.grid(row=0, column=0, padx=10)

# Frame para los resultados
frame_resultado = tk.Frame(frame_principal, bg="#f0f0f0")
frame_resultado.grid(row=0, column=1, padx=5)

# Widgets para la cantidad
label_cantidad = tk.Label(ventana, text="Cantidad a fabricar:", bg="#f0f0f0", font=("Helvetica", 12))
label_cantidad.pack(pady=10)

entry_cantidad = tk.Entry(ventana, font=("Helvetica", 12))
entry_cantidad.pack(pady=5)

# Cargar imágenes de las artillerías
label_instrucciones = tk.Label(frame_artillerias, text="Selecciona una artillería:", bg="#f0f0f0", font=("Helvetica", 12))
label_instrucciones.grid(row=0, column=0, pady=2, columnspan=3)

# Cargar las imágenes de artillerías
imagenes_artillerias = {}
for artilleria in artillerias.keys():
    imagen = Image.open(resource_path(f"./artillerias/{artilleria.lower()}.png"))  # Asegurarse que el nombre de archivo es correcto
    imagen = imagen.resize((75, 75))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagenes_artillerias[artilleria] = imagen_tk

# Botones con imágenes para seleccionar artillerías
fila, columna = 1, 0
for artilleria, imagen_tk in imagenes_artillerias.items():
    boton = tk.Button(frame_artillerias, image=imagen_tk, command=lambda a=artilleria: seleccionar_artilleria(a), bg="#4CAF50", fg="white", bd=2, relief="raised")
    boton.grid(row=fila, column=columna, padx=2, pady=2)

    columna += 1
    if columna == 3:
        columna = 0
        fila += 1

# Mostrar la artillería seleccionada
label_seleccion = tk.Label(frame_artillerias, text="Artillería seleccionada: Ninguna", bg="#f0f0f0", font=("Helvetica", 12), width=30)
label_seleccion.grid(row=fila, column=0, columnspan=3, pady=2)

# Frame para mostrar resultados de materiales
frame_materiales = tk.Frame(frame_resultado, bg="#f0f0f0")
frame_materiales.grid(row=0, column=0)

# Botón para calcular los materiales
boton_calcular = tk.Button(ventana, text="Calcular Materiales", command=calcular_materiales, bg="#008CBA", fg="white", font=("Helvetica", 12))
boton_calcular.pack(pady=2)

# Cargar imágenes de materiales
imagenes_materiales = {
    "Hierro en bruto": ImageTk.PhotoImage(Image.open(resource_path("./materiales/hierro_bruto.png")).resize((50, 50))),
    "Cobre en bruto": ImageTk.PhotoImage(Image.open(resource_path("./materiales/cobre_bruto.png")).resize((50, 50))),
    "Madera seca": ImageTk.PhotoImage(Image.open(resource_path("./materiales/madera_seca.png")).resize((50, 50))),
    "Piedra en bruto": ImageTk.PhotoImage(Image.open(resource_path("./materiales/piedra_bruto.png")).resize((50, 50))),
    "Tela aspera": ImageTk.PhotoImage(Image.open(resource_path("./materiales/tela_aspera.png")).resize((50, 50))),
    "Cuero curtido": ImageTk.PhotoImage(Image.open(resource_path("./materiales/cuero_curtido.png")).resize((50, 50))),

    "Hierro fundido": ImageTk.PhotoImage(Image.open(resource_path("./materiales/hierro_fundido.png")).resize((50, 50))),
    "Cobre mejorado": ImageTk.PhotoImage(Image.open(resource_path("./materiales/cobre_azul.png")).resize((50, 50))),
    "Madera alisada": ImageTk.PhotoImage(Image.open(resource_path("./materiales/madera_alisada.png")).resize((50, 50))),
    "Piedra cortada": ImageTk.PhotoImage(Image.open(resource_path("./materiales/piedra_cortada.png")).resize((50, 50))),
    "Tela barata": ImageTk.PhotoImage(Image.open(resource_path("./materiales/tela_barata.png")).resize((50, 50))),
    "Cuero tratado": ImageTk.PhotoImage(Image.open(resource_path("./materiales/cuero_tratado.png")).resize((50, 50))),
}

# Iniciar la aplicación
ventana.mainloop()
