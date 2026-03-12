import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

# ─────────────────────────────────────────────
#  TRADUCCIONES DE LA INTERFAZ
# ─────────────────────────────────────────────
traducciones_ui = {
    "es": {
        "titulo":               "Calculadora de Crafteo - Conquerors Blade",
        "selecciona":           "Selecciona una artillería:",
        "seleccionada_ninguna": "Artillería seleccionada: Ninguna",
        "seleccionada":         "Artillería seleccionada: {}",
        "cantidad":             "Cantidad a fabricar:",
        "calcular":             "Calcular Materiales",
        "resultado":            "Materiales necesarios para\n{} {}(s):",
        "error_seleccion":      "Por favor selecciona una artillería.",
        "error_numero":         "Por favor ingresa un número válido.",
        "idioma":               "Idioma / Language:",
    },
    "en": {
        "titulo":               "Crafting Calculator - Conquerors Blade",
        "selecciona":           "Select an artillery:",
        "seleccionada_ninguna": "Selected artillery: None",
        "seleccionada":         "Selected artillery: {}",
        "cantidad":             "Quantity to craft:",
        "calcular":             "Calculate Materials",
        "resultado":            "Materials needed for\n{} {}(s):",
        "error_seleccion":      "Please select an artillery.",
        "error_numero":         "Please enter a valid number.",
        "idioma":               "Idioma / Language:",
    # }
    # ,
    # "pt": {
    #     "titulo":               "Calculadora de Craft - Conquerors Blade",
    #     "selecciona":           "Selecione uma artilharia:",
    #     "seleccionada_ninguna": "Artilharia selecionada: Nenhuma",
    #     "seleccionada":         "Artilharia selecionada: {}",
    #     "cantidad":             "Quantidade para fabricar:",
    #     "calcular":             "Calcular Materiais",
    #     "resultado":            "Materiais necessários para\n{} {}(s):",
    #     "error_seleccion":      "Por favor selecione uma artilharia.",
    #     "error_numero":         "Por favor insira um número válido.",
    #     "idioma":               "Idioma / Language:",
    # },
    # "fr": {
    #     "titulo":               "Calculateur de Craft - Conquerors Blade",
    #     "selecciona":           "Sélectionnez une artillerie :",
    #     "seleccionada_ninguna": "Artillerie sélectionnée : Aucune",
    #     "seleccionada":         "Artillerie sélectionnée : {}",
    #     "cantidad":             "Quantité à fabriquer :",
    #     "calcular":             "Calculer les Matériaux",
    #     "resultado":            "Matériaux nécessaires pour\n{} {}(s) :",
    #     "error_seleccion":      "Veuillez sélectionner une artillerie.",
    #     "error_numero":         "Veuillez entrer un nombre valide.",
    #     "idioma":               "Idioma / Language:",
    },
}

# ─────────────────────────────────────────────
#  NOMBRES DE ARTILLERÍAS POR IDIOMA
#  Clave interna (es) → nombre visible
# ─────────────────────────────────────────────
nombres_artillerias = {
    "es": {
        "Metralla verde":  "Metralla verde",
        "Metralla azul":   "Metralla azul",
        "Metralla morada": "Metralla morada",
        "Vacio":           "Vacío",
        "Mortero azul":    "Mortero azul",
        "Mortero morado":  "Mortero morado",
        "Culebrina verde": "Culebrina verde",
        "Culebrina azul":  "Culebrina azul",
        "Culebrina morada":"Culebrina morada",
        "Balista verde":   "Balista verde",
        "Balista azul":    "Balista azul",
        "Balista morada":  "Balista morada",
        "Cañon verde":     "Cañón verde",
        "Cañon azul":      "Cañón azul",
        "Cañon morado":    "Cañón morado",
    },
    "en": {
        "Metralla verde":  "Grapeshot Cannon",
        "Metralla azul":   "Well-Made Grapeshot Cannon",
        "Metralla morada": "Optimal Grapeshot Cannon",
        "Vacio":           "Empty",
        "Mortero azul":    "Well-Made Mortar",
        "Mortero morado":  "Optimal Mortar",
        "Culebrina verde": "Culverin",
        "Culebrina azul":  "Well-Made Culverin",
        "Culebrina morada":"Optimal Culverin",
        "Balista verde":   "Ballista",
        "Balista azul":    "Well-Made Ballista",
        "Balista morada":  "Optimal Ballista",
        "Cañon verde":     "Cannon",
        "Cañon azul":      "Well-Made Cannon",
        "Cañon morado":    "Optimal Cannon",
    # },
    # "pt": {
    #     "Metralla verde":  "Metralha Verde",
    #     "Metralla azul":   "Metralha Azul",
    #     "Metralla morada": "Metralha Roxa",
    #     "Vacio":           "Vazio",
    #     "Mortero azul":    "Morteiro Azul",
    #     "Mortero morado":  "Morteiro Roxo",
    #     "Culebrina verde": "Culverina Verde",
    #     "Culebrina azul":  "Culverina Azul",
    #     "Culebrina morada":"Culverina Roxa",
    #     "Balista verde":   "Balista Verde",
    #     "Balista azul":    "Balista Azul",
    #     "Balista morada":  "Balista Roxa",
    #     "Cañon verde":     "Canhão Verde",
    #     "Cañon azul":      "Canhão Azul",
    #     "Cañon morado":    "Canhão Roxo",
    # },
    # "fr": {
    #     "Metralla verde":  "Mitraille Verte",
    #     "Metralla azul":   "Mitraille Bleue",
    #     "Metralla morada": "Mitraille Violette",
    #     "Vacio":           "Vide",
    #     "Mortero azul":    "Mortier Bleu",
    #     "Mortero morado":  "Mortier Violet",
    #     "Culebrina verde": "Couleuvrine Verte",
    #     "Culebrina azul":  "Couleuvrine Bleue",
    #     "Culebrina morada":"Couleuvrine Violette",
    #     "Balista verde":   "Baliste Verte",
    #     "Balista azul":    "Baliste Bleue",
    #     "Balista morada":  "Baliste Violette",
    #     "Cañon verde":     "Canon Vert",
    #     "Cañon azul":      "Canon Bleu",
    #     "Cañon morado":    "Canon Violet",
    },
}

# ─────────────────────────────────────────────
#  NOMBRES DE MATERIALES POR IDIOMA
# ─────────────────────────────────────────────
nombres_materiales = {
    "es": {
        "Hierro en bruto":  "Hierro en bruto",
        "Madera seca":      "Madera seca",
        "Cobre en bruto":   "Cobre en bruto",
        "Piedra en bruto":  "Piedra en bruto",
        "Plata":            "Plata",
        "Hierro fundido":   "Hierro fundido",
        "Madera alisada":   "Madera alisada",
        "Cobre mejorado":   "Cobre mejorado",
        "Piedra cortada":   "Piedra cortada",
        "Cuero curtido":    "Cuero curtido",
        "Tela aspera":      "Tela áspera",
        "Cuero tratado":    "Cuero tratado",
        "Tela barata":      "Tela barata",
    },
    "en": {
        "Hierro en bruto":  "Raw Iron",
        "Madera seca":      "Seasoned Wood",
        "Cobre en bruto":   "Coarse Copper",
        "Piedra en bruto":  "Rough Stone",
        "Plata":            "Silver",
        "Hierro fundido":   "Cast Iron",
        "Madera alisada":   "Planed Wood",
        "Cobre mejorado":   "Improved Copper",
        "Piedra cortada":   "Cut Stone",
        "Cuero curtido":    "Tanned Leather",
        "Tela aspera":      "Rough Fabric",
        "Cuero tratado":    "Treated Leather",
        "Tela barata":      "Cheap Fabric",
    # },
    # "pt": {
    #     "Hierro en bruto":  "Ferro Bruto",
    #     "Madera seca":      "Madeira Seca",
    #     "Cobre en bruto":   "Cobre Bruto",
    #     "Piedra en bruto":  "Pedra Bruta",
    #     "Plata":            "Prata",
    #     "Hierro fundido":   "Ferro Fundido",
    #     "Madera alisada":   "Madeira Alisada",
    #     "Cobre mejorado":   "Cobre Melhorado",
    #     "Piedra cortada":   "Pedra Cortada",
    #     "Cuero curtido":    "Couro Curtido",
    #     "Tela aspera":      "Tecido Áspero",
    #     "Cuero tratado":    "Couro Tratado",
    #     "Tela barata":      "Tecido Barato",
    # },
    # "fr": {
    #     "Hierro en bruto":  "Fer Brut",
    #     "Madera seca":      "Bois Sec",
    #     "Cobre en bruto":   "Cuivre Brut",
    #     "Piedra en bruto":  "Pierre Brute",
    #     "Plata":            "Argent",
    #     "Hierro fundido":   "Fonte",
    #     "Madera alisada":   "Bois Lissé",
    #     "Cobre mejorado":   "Cuivre Amélioré",
    #     "Piedra cortada":   "Pierre Taillée",
    #     "Cuero curtido":    "Cuir Tanné",
    #     "Tela aspera":      "Tissu Grossier",
    #     "Cuero tratado":    "Cuir Traité",
    #     "Tela barata":      "Tissu Bon Marché",
    },
}

# Banderas / etiquetas para el selector
opciones_idioma = [
    ("Español", "es"),
    ("English", "en")
    #,
    #("🇧🇷 Português", "pt"),
    #("🇫🇷 Français", "fr"),
]

# ─────────────────────────────────────────────
#  RECETAS (claves internas en español)
# ─────────────────────────────────────────────
artillerias = {
    "Metralla verde":  {"Hierro en bruto": 200, "Cobre en bruto": 50, "Madera seca": 50,  "Piedra en bruto": 50, "Plata": 250},
    "Metralla azul":   {"Hierro fundido": 100, "Cobre mejorado": 100, "Madera alisada": 50, "Piedra cortada": 50, "Plata": 500},
    "Metralla morada": {"Hierro fundido": 200, "Cobre mejorado": 100, "Madera alisada": 100,  "Piedra cortada": 100, "Plata": 1000},

    "Vacio":           {"Hierro en bruto": 0, "Cobre en bruto": 0, "Madera seca": 0,  "Piedra en bruto": 0, "Plata": 0},
    "Mortero azul":    {"Hierro fundido": 100, "Cobre mejorado": 100, "Madera alisada": 50, "Piedra cortada": 50,  "Plata": 500},
    "Mortero morado":  {"Hierro fundido": 200, "Cobre mejorado": 200, "Madera alisada": 100, "Piedra cortada": 100,  "Plata": 1000},

    "Culebrina verde": {"Hierro en bruto": 50, "Cobre en bruto": 200, "Madera seca": 50,  "Piedra en bruto": 50, "Plata": 250},
    "Culebrina azul":  {"Hierro fundido": 50, "Cobre mejorado": 100, "Madera alisada": 50,  "Piedra cortada": 50, "Plata": 500},
    "Culebrina morada":{"Hierro fundido": 100, "Cobre mejorado": 200, "Madera alisada": 100,  "Piedra cortada": 100, "Plata": 1000},

    "Balista verde":   {"Hierro en bruto": 100, "Madera seca": 200,  "Cuero curtido": 50, "Tela aspera": 50, "Plata": 250},
    "Balista azul":    {"Hierro fundido": 50, "Madera alisada": 100,  "Cuero tratado": 50, "Tela barata": 50, "Plata": 500},
    "Balista morada":  {"Hierro fundido": 100, "Madera alisada": 200,  "Cuero tratado": 100, "Tela barata": 100, "Plata": 1000},

    "Cañon verde":     {"Hierro en bruto": 50, "Cobre en bruto": 200, "Madera seca": 50,  "Piedra en bruto": 50, "Plata": 250},
    "Cañon azul":      {"Hierro fundido": 50, "Cobre mejorado": 100, "Madera alisada": 50,  "Piedra cortada": 50, "Plata": 500},
    "Cañon morado":    {"Hierro fundido": 100, "Cobre mejorado": 200, "Madera alisada": 100,  "Piedra cortada": 100, "Plata": 1000},
}

# ─────────────────────────────────────────────
#  RECETAS DE MATERIALES PROCESADOS → CRUDOS
#  Cuántos materiales crudos necesita 1 unidad del procesado
# ─────────────────────────────────────────────
recetas_crudos = {
    "Hierro fundido":   {"Hematita": 7,  "Calamina": 1},
    "Cobre mejorado":   {"Cuprita":  7,  "Estaño":  1},
    "Madera alisada":   {"Madera de cedro":  7,  "Tendones":   1},
    "Piedra cortada":   {"Granito": 7,  "Goma laca":  1},
    "Cuero tratado":    {"Piel de vaca":   7,  "Goma laca":   1},
    "Tela barata":      {"Algodón morado": 7,  "Lino":    1},
}

# Traducción de los materiales crudos extra (los que no estaban antes)
nombres_materiales_extra = {
    "es": {
        "Calamina":    "Calamina",
        "Estaño":     "Estaño",
        "Tendones":      "Tendones",
        "Goma laca":     "Goma laca",
        "Lino":      "Lino",
        "Hematita":       "Hematita",
        "Cuprita": "Cuprita",
        "Madera de cedro":  "Madera de cedro",
        "Granito":     "Granito",
        "Piel de vaca": "Piel de vaca",
        "Algodón morado":   "Algodón morado",
    },
    "en": {
        "Calamina":    "Calamine",
        "Estaño":     "Tin",
        "Tendones":      "Sinews",
        "Goma laca":     "Shellac",
        "Lino":      "Flax",
        "Hematita":       "Haematite",
        "Cuprita": "Cuprite",
        "Madera de cedro":  "Cedar Timber",
        "Granito":     "Granite",
        "Piel de vaca": "Cow Hide",
        "Algodón morado":   "Fine Cotton",
    # },
    # "pt": {
    #     "Calamine":    "Calamina",
    #     "Cuprite":     "Cuprite",
    #     "Resina":      "Resina",
    #     "Shellac":     "Shellac",
    #     "Tanino":      "Tanino",
    #     "Tinte":       "Tinta",
    #     "Hierro en bruto": "Ferro Bruto",
    #     "Cobre en bruto":  "Cobre Bruto",
    #     "Madera seca":     "Madeira Seca",
    #     "Piedra en bruto": "Pedra Bruta",
    #     "Cuero curtido":   "Couro Curtido",
    #     "Tela aspera":     "Tecido Áspero",
    # },
    # "fr": {
    #     "Calamine":    "Calamine",
    #     "Cuprite":     "Cuprite",
    #     "Resina":      "Résine",
    #     "Shellac":     "Shellac",
    #     "Tanino":      "Tannin",
    #     "Tinte":       "Teinture",
    #     "Hierro en bruto": "Fer Brut",
    #     "Cobre en bruto":  "Cuivre Brut",
    #     "Madera seca":     "Bois Sec",
    #     "Piedra en bruto": "Pierre Brute",
    #     "Cuero curtido":   "Cuir Tanné",
    #     "Tela aspera":     "Tissu Grossier",
    },
}

# ─────────────────────────────────────────────
#  ESTADO GLOBAL
# ─────────────────────────────────────────────
artilleria_seleccionada = None   # clave interna (español)
idioma_actual = "es"


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def ui(clave):
    """Devuelve el texto de interfaz en el idioma actual."""
    return traducciones_ui[idioma_actual][clave]


def nombre_artilleria(clave_interna):
    return nombres_artillerias[idioma_actual].get(clave_interna, clave_interna)


def nombre_material(clave_interna):
    # Busca primero en el diccionario principal, luego en el de extras
    lang = idioma_actual if idioma_actual in nombres_materiales else "es"
    resultado = nombres_materiales[lang].get(clave_interna)
    if resultado is None:
        resultado = nombres_materiales_extra.get(lang, {}).get(clave_interna, clave_interna)
    return resultado


# ─────────────────────────────────────────────
#  LÓGICA PRINCIPAL
# ─────────────────────────────────────────────
def calcular_materiales():
    try:
        cantidad = int(entry_cantidad.get())
        if artilleria_seleccionada:
            materiales_necesarios = {
                mat: cant_base * cantidad
                for mat, cant_base in artillerias[artilleria_seleccionada].items()
            }

            for widget in frame_resultado.winfo_children():
                widget.destroy()

            nombre_visible = nombre_artilleria(artilleria_seleccionada)
            resultado_texto = ui("resultado").format(cantidad, nombre_visible)
            tk.Label(frame_resultado, text=resultado_texto, bg="#f0f0f0",
                     font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=5)

            row = 1
            for material, total in materiales_necesarios.items():
                nombre_vis = nombre_material(material)

                # Imagen del material procesado
                if material in imagenes_materiales:
                    tk.Label(frame_resultado, image=imagenes_materiales[material],
                             bg="#f0f0f0").grid(row=row, column=0, padx=(0, 4), pady=2)

                # Nombre y cantidad del material procesado
                tk.Label(frame_resultado, text=f"{nombre_vis}  x{total}", bg="#f0f0f0",
                         font=("Helvetica", 10, "bold")).grid(row=row, column=1, columnspan=2, pady=2, sticky="w")
                row += 1

                # Sub-materiales crudos si aplica
                if material in recetas_crudos:
                    crudos_lista = list(recetas_crudos[material].items())
                    for i, (crudo, cant_por_uno) in enumerate(crudos_lista):
                        total_crudo = cant_por_uno * total
                        nombre_crudo = nombre_material(crudo)
                        es_ultimo = (i == len(crudos_lista) - 1)
                        prefijo = "  └─ " if es_ultimo else "  ├─ "
                        tk.Label(frame_resultado,
                                 text=f"{prefijo}{nombre_crudo}  x{total_crudo}",
                                 bg="#f0f0f0", fg="#444444",
                                 font=("Courier", 9)).grid(row=row, column=1, columnspan=2, pady=0, sticky="w")
                        row += 1

        else:
            for widget in frame_resultado.winfo_children():
                widget.destroy()
            tk.Label(frame_resultado, text=ui("error_seleccion"), bg="#f0f0f0",
                     fg="red", font=("Helvetica", 10, "italic")).grid(row=0, column=0, columnspan=3, pady=2)

    except ValueError:
        for widget in frame_resultado.winfo_children():
            widget.destroy()
        tk.Label(frame_resultado, text=ui("error_numero"), bg="#f0f0f0",
                 fg="red", font=("Helvetica", 10, "italic")).grid(row=0, column=0, columnspan=3, pady=2)


def seleccionar_artilleria(artilleria):
    global artilleria_seleccionada
    artilleria_seleccionada = artilleria
    label_seleccion.config(text=ui("seleccionada").format(nombre_artilleria(artilleria)))
    entry_cantidad.delete(0, tk.END)
    entry_cantidad.insert(0, "1")

    # Resaltar botón activo, resetear los demás
    for nombre, btn in botones_artillerias.items():
        if nombre == artilleria:
            btn.config(bg="#FFD700", bd=4, relief="sunken")   # dorado + hundido
        else:
            btn.config(bg="#4CAF50", bd=2, relief="raised")

    calcular_materiales()


def cambiar_idioma(nuevo_idioma):
    """Actualiza todos los textos de la interfaz al nuevo idioma."""
    global idioma_actual
    idioma_actual = nuevo_idioma

    # Actualizar textos estáticos
    ventana.title(ui("titulo"))
    label_instrucciones.config(text=ui("selecciona"))
    label_cantidad.config(text=ui("cantidad"))
    boton_calcular.config(text=ui("calcular"))
    label_idioma_titulo.config(text=ui("idioma"))

    if artilleria_seleccionada:
        label_seleccion.config(text=ui("seleccionada").format(nombre_artilleria(artilleria_seleccionada)))
    else:
        label_seleccion.config(text=ui("seleccionada_ninguna"))

    # Resaltar botón activo
    for codigo, boton in botones_idioma.items():
        boton.config(relief="sunken" if codigo == idioma_actual else "raised",
                     bg="#005f8a" if codigo == idioma_actual else "#008CBA")

    # Recalcular si hay artillería seleccionada
    if artilleria_seleccionada:
        calcular_materiales()
    else:
        for widget in frame_resultado.winfo_children():
            widget.destroy()


# ─────────────────────────────────────────────
#  VENTANA PRINCIPAL
# ─────────────────────────────────────────────
ventana = tk.Tk()
ventana.title(ui("titulo"))
ventana.geometry("720x645")
ventana.resizable(False, False)

# Fondo
imagen_fondo = Image.open(resource_path("./extras/fondo3.png")).resize((720, 645))
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
tk.Label(ventana, image=imagen_fondo_tk).place(x=0, y=0, relwidth=1, relheight=1)

# Frame principal
frame_principal = tk.Frame(ventana, bg="#f0f0f0")
frame_principal.pack(pady=2)

frame_artillerias = tk.Frame(frame_principal, bg="#f0f0f0")
frame_artillerias.grid(row=0, column=0, padx=10)

frame_resultado = tk.Frame(frame_principal, bg="#f0f0f0")
frame_resultado.grid(row=0, column=1, padx=5)

# Cantidad
label_cantidad = tk.Label(ventana, text=ui("cantidad"), bg="#f0f0f0", font=("Helvetica", 12))
label_cantidad.pack(pady=10)

frame_cantidad = tk.Frame(ventana, bg="#f0f0f0")
frame_cantidad.pack(pady=5)

def restar_cantidad():
    try:
        val = int(entry_cantidad.get())
        if val > 1:
            entry_cantidad.delete(0, tk.END)
            entry_cantidad.insert(0, str(val - 1))
            calcular_materiales()
    except ValueError:
        pass

def sumar_cantidad():
    try:
        val = int(entry_cantidad.get())
        entry_cantidad.delete(0, tk.END)
        entry_cantidad.insert(0, str(val + 1))
        calcular_materiales()
    except ValueError:
        pass

tk.Button(frame_cantidad, text=" − ", command=restar_cantidad,
          bg="#c0392b", fg="white", font=("Helvetica", 12, "bold"),
          relief="raised", bd=2).pack(side="left", padx=4)

entry_cantidad = tk.Entry(frame_cantidad, font=("Helvetica", 12), width=5, justify="center")
entry_cantidad.pack(side="left")

tk.Button(frame_cantidad, text=" + ", command=sumar_cantidad,
          bg="#27ae60", fg="white", font=("Helvetica", 12, "bold"),
          relief="raised", bd=2).pack(side="left", padx=4)

# Instrucciones artillerías
label_instrucciones = tk.Label(frame_artillerias, text=ui("selecciona"), bg="#f0f0f0", font=("Helvetica", 12))
label_instrucciones.grid(row=0, column=0, pady=2, columnspan=3)

# Cargar imágenes de artillerías
imagenes_artillerias = {}
for artilleria in artillerias.keys():
    imagen = Image.open(resource_path(f"./artillerias/{artilleria.lower()}.png")).resize((75, 75))
    imagenes_artillerias[artilleria] = ImageTk.PhotoImage(imagen)

# Botones de artillerías
botones_artillerias = {}
fila, columna = 1, 0
for artilleria, imagen_tk in imagenes_artillerias.items():
    btn = tk.Button(frame_artillerias, image=imagen_tk,
                    command=lambda a=artilleria: seleccionar_artilleria(a),
                    bg="#4CAF50", fg="white", bd=2, relief="raised")
    btn.grid(row=fila, column=columna, padx=2, pady=2)
    botones_artillerias[artilleria] = btn
    columna += 1
    if columna == 3:
        columna = 0
        fila += 1

# Label artillería seleccionada
label_seleccion = tk.Label(frame_artillerias, text=ui("seleccionada_ninguna"),
                            bg="#f0f0f0", font=("Helvetica", 12), width=30)
label_seleccion.grid(row=fila, column=0, columnspan=3, pady=2)

# Botón calcular
boton_calcular = tk.Button(ventana, text=ui("calcular"), command=calcular_materiales,
                            bg="#008CBA", fg="white", font=("Helvetica", 12))
boton_calcular.pack(pady=2)

# Espaciador para empujar el selector de idioma hacia abajo
frame_espaciador = tk.Frame(ventana, bg="#f0f0f0", height=2)
frame_espaciador.pack()

# Imágenes de materiales
imagenes_materiales = {
    "Hierro en bruto": ImageTk.PhotoImage(Image.open(resource_path("./materiales/hierro_bruto.png")).resize((50, 50))),
    "Cobre en bruto":  ImageTk.PhotoImage(Image.open(resource_path("./materiales/cobre_bruto.png")).resize((50, 50))),
    "Madera seca":     ImageTk.PhotoImage(Image.open(resource_path("./materiales/madera_seca.png")).resize((50, 50))),
    "Piedra en bruto": ImageTk.PhotoImage(Image.open(resource_path("./materiales/piedra_bruto.png")).resize((50, 50))),
    "Tela aspera":     ImageTk.PhotoImage(Image.open(resource_path("./materiales/tela_aspera.png")).resize((50, 50))),
    "Cuero curtido":   ImageTk.PhotoImage(Image.open(resource_path("./materiales/cuero_curtido.png")).resize((50, 50))),
    "Hierro fundido":  ImageTk.PhotoImage(Image.open(resource_path("./materiales/hierro_fundido.png")).resize((50, 50))),
    "Cobre mejorado":  ImageTk.PhotoImage(Image.open(resource_path("./materiales/cobre_azul.png")).resize((50, 50))),
    "Madera alisada":  ImageTk.PhotoImage(Image.open(resource_path("./materiales/madera_alisada.png")).resize((50, 50))),
    "Piedra cortada":  ImageTk.PhotoImage(Image.open(resource_path("./materiales/piedra_cortada.png")).resize((50, 50))),
    "Tela barata":     ImageTk.PhotoImage(Image.open(resource_path("./materiales/tela_barata.png")).resize((50, 50))),
    "Cuero tratado":   ImageTk.PhotoImage(Image.open(resource_path("./materiales/cuero_tratado.png")).resize((50, 50))),
}

# ─────────────────────────────────────────────
#  SELECTOR DE IDIOMA  (abajo a la izquierda, fondo transparente)
#  Usamos un color clave (#010101) que wm_attributes vuelve invisible.
#  Solo el fondo desaparece; los botones conservan su color normal.
# ─────────────────────────────────────────────
frame_fila_inferior = tk.Frame(ventana, bg="#f0f0f0")
frame_fila_inferior.pack(side="bottom", anchor="w", padx=8, pady=4)

frame_idioma = tk.Frame(frame_fila_inferior, bg="#f0f0f0", bd=1, relief="groove")
frame_idioma.pack(side="left")

label_idioma_titulo = tk.Label(frame_idioma, text=ui("idioma"),
                                bg="#f0f0f0", font=("Helvetica", 9, "bold"))
label_idioma_titulo.pack(side="left", padx=(4, 2))

botones_idioma = {}
for etiqueta, codigo in opciones_idioma:
    relieve = "sunken" if codigo == idioma_actual else "raised"
    color   = "#005f8a" if codigo == idioma_actual else "#008CBA"
    btn = tk.Button(frame_idioma, text=etiqueta,
                    command=lambda c=codigo: cambiar_idioma(c),
                    bg=color, fg="white",
                    font=("Helvetica", 9), relief=relieve,
                    padx=4, pady=2)
    btn.pack(side="left", padx=2, pady=3)
    botones_idioma[codigo] = btn

ventana.mainloop()