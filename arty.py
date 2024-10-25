import tkinter as tk
from PIL import Image, ImageTk

# Diccionario de artillerías con sus materiales
artillerias = {
    "Metralla verde": {"Hierro en bruto": 200, "Madera seca": 50, "Cobre en bruto": 50, "Piedra en bruto": 50, "Plata": 250},
    "Metralla azul": {"Hierro en bruto": 200, "Madera seca": 50, "Cobre en bruto": 50, "Piedra en bruto": 50, "Plata": 250},
    "Metralla morada": {"Hierro en bruto": 200, "Madera seca": 50, "Cobre en bruto": 50, "Piedra en bruto": 50, "Plata": 250},

    "Balista verde": {"Madera seca": 200, "Hierro en bruto": 100, "Cuero curtido": 50, "Tela aspera": 50,"Plata": 250},
    "Balista azul": {"Madera seca": 200, "Hierro en bruto": 100, "Cuero curtido": 50, "Tela aspera": 50,"Plata": 250},
    "Balista morada": {"Madera seca": 200, "Hierro en bruto": 100, "Cuero curtido": 50, "Tela aspera": 50,"Plata": 250},

    "Culebrina verde": {"Cobre en bruto": 160, "Madera seca": 40, "Hierro en bruto": 40, "Piedra en bruto": 40,"Plata": 250},
    "Culebrina azul": {"Cobre en bruto": 160, "Madera seca": 40, "Hierro en bruto": 40, "Piedra en bruto": 40,"Plata": 250},
    "Culebrina morada": {"Cobre en bruto": 160, "Madera seca": 40, "Hierro en bruto": 40, "Piedra en bruto": 40,"Plata": 250},

    "Mortero azul": {"Cobre mejorado": 80, "Hierro fundido": 80, "Piedra cortada": 40, "Madera alisada": 40,"Plata": 500},
    "Mortero morado": {"Cobre en bruto": 160, "Madera seca": 40, "Hierro en bruto": 40, "Piedra en bruto": 40,"Plata": 250},
}

# Función para calcular los materiales
def calcular_materiales():
    cantidad = int(entry_cantidad.get())
    
    if artilleria_seleccionada:
        materiales_necesarios = {}
        for material, cantidad_base in artillerias[artilleria_seleccionada].items():
            materiales_necesarios[material] = cantidad_base * cantidad
        
        # Limpiar el frame de resultados
        for widget in frame_resultado.winfo_children():
            widget.destroy()
        
        resultado_texto = f"Materiales necesarios para crear {cantidad} {artilleria_seleccionada}(s):"
        label_resultado = tk.Label(frame_resultado, text=resultado_texto)
        label_resultado.pack()
        
        # Mostrar cada material con su imagen y cantidad
        for material, total in materiales_necesarios.items():
            # Mostrar texto del material
            label_material = tk.Label(frame_resultado, text=f"{material}: {total}")
            label_material.pack()
            
            # Mostrar imagen del material
            if material in imagenes_materiales:
                imagen_label = tk.Label(frame_resultado, image=imagenes_materiales[material])
                imagen_label.pack()

    else:
        # Si no se seleccionó ninguna artillería, mostrar un mensaje en el frame de resultado
        for widget in frame_resultado.winfo_children():
            widget.destroy()
        label_error = tk.Label(frame_resultado, text="Por favor selecciona una artillería.")
        label_error.pack()

# Función para seleccionar la artillería al hacer clic en la imagen
def seleccionar_artilleria(artilleria):
    global artilleria_seleccionada
    artilleria_seleccionada = artilleria
    label_seleccion.config(text=f"Artillería seleccionada: {artilleria}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Crafteo con Imágenes")
artilleria_seleccionada = None

# Widgets para la cantidad
label_cantidad = tk.Label(ventana, text="Cantidad a fabricar:")
label_cantidad.pack()

entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

# Cargar imágenes de las artillerías
label_instrucciones = tk.Label(ventana, text="Selecciona una artillería:")
label_instrucciones.pack()

frame_imagenes = tk.Frame(ventana)
frame_imagenes.pack()

# Cargar las imágenes de artillerías
imagenes_artillerias = {}
for artilleria in artillerias.keys():
    imagen = Image.open(f"{artilleria.lower()}.png")
    imagen = imagen.resize((100, 100))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagenes_artillerias[artilleria] = imagen_tk

# Botones con imágenes para seleccionar artillerías (colocar en una cuadrícula de 3 por fila)
fila, columna = 0, 0
for artilleria, imagen_tk in imagenes_artillerias.items():
    boton = tk.Button(frame_imagenes, image=imagen_tk, command=lambda a=artilleria: seleccionar_artilleria(a))
    boton.grid(row=fila, column=columna, padx=10, pady=10)  # Colocar con grid en la fila y columna actual

    # Ajustar el contador de columna, y si llega a 3, mover a la siguiente fila
    columna += 1
    if columna == 3:
        columna = 0
        fila += 1

# Mostrar la artillería seleccionada
label_seleccion = tk.Label(ventana, text="Artillería seleccionada: Ninguna")
label_seleccion.pack()

# Botón para calcular los materiales
boton_calcular = tk.Button(ventana, text="Calcular Materiales", command=calcular_materiales)
boton_calcular.pack()

# Frame donde se mostrarán los resultados (texto e imágenes de los materiales)
frame_resultado = tk.Frame(ventana)
frame_resultado.pack()

# Cargar imágenes de materiales
imagenes_materiales = {
    "Hierro en bruto": ImageTk.PhotoImage(Image.open("hierro_bruto.png").resize((50, 50))),
    "Cobre en bruto": ImageTk.PhotoImage(Image.open("cobre_bruto.png").resize((50, 50))),
    "Madera seca": ImageTk.PhotoImage(Image.open("madera_seca.png").resize((50, 50))),
    "Piedra en bruto": ImageTk.PhotoImage(Image.open("piedra_bruto.png").resize((50, 50))),
    "Tela aspera": ImageTk.PhotoImage(Image.open("tela_aspera.png").resize((50, 50))),
    "Cuero curtido": ImageTk.PhotoImage(Image.open("cuero_curtido.png").resize((50, 50))),

    "Hierro fundido": ImageTk.PhotoImage(Image.open("hierro_fundido.png").resize((50, 50))),
    "Cobre mejorado": ImageTk.PhotoImage(Image.open("cobre_morado.png").resize((50, 50))),
    "Madera alisada": ImageTk.PhotoImage(Image.open("madera_alisada.png").resize((50, 50))),
    "Piedra cortada": ImageTk.PhotoImage(Image.open("piedra_cortada.png").resize((50, 50))),
}

# Iniciar la aplicación
ventana.mainloop()