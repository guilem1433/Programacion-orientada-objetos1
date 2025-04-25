from tkinter import *
from math import *
import math
import re

# Variables globales
operador = ""
input_text = None

# Función para mostrar los números o símbolos presionados
def btnClik(num):
    global operador
    operador += str(num)
    input_text.set(operador)

# Función para mostrar el resultado
def resultado():
    global operador
    try:
        # Reemplaza los porcentajes: "25%" → "(25/100)"
        expresion = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', operador)

        # Evalúa de forma segura usando funciones de math
        resultado_eval = str(eval(expresion, {"_builtins_": None}, vars(math)))
        input_text.set(resultado_eval)
    except:
        input_text.set("ERROR")
    operador = ""

# Función para limpiar la pantalla
def clear():
    global operador
    operador = ""
    input_text.set("0")

# Crear ventana principal
ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")
ventana.configure(background="SkyBlue4")

# Variables de estilo
color_boton = "gray77"
ancho_boton = 9
alto_boton = 3
input_text = StringVar()

# Pantalla
Salida = Entry(ventana, font=('arial', 20, 'bold'), width=22,
               textvariable=input_text, bd=20, insertwidth=4,
               bg="powder blue", justify="right")
Salida.place(x=10, y=20)

# Lista de botones organizados (texto, comando, posición x, y)
botones = [
    ("7", lambda: btnClik(7), 17, 100), ("8", lambda: btnClik(8), 107, 100),
    ("9", lambda: btnClik(9), 197, 100), ("/", lambda: btnClik("/"), 287, 100),

    ("4", lambda: btnClik(4), 17, 160), ("5", lambda: btnClik(5), 107, 160),
    ("6", lambda: btnClik(6), 197, 160), ("*", lambda: btnClik("*"), 287, 160),

    ("1", lambda: btnClik(1), 17, 220), ("2", lambda: btnClik(2), 107, 220),
    ("3", lambda: btnClik(3), 197, 220), ("-", lambda: btnClik("-"), 287, 220),

    ("0", lambda: btnClik(0), 17, 280), (".", lambda: btnClik("."), 107, 280),
    ("=", resultado, 197, 280), ("+", lambda: btnClik("+"), 287, 280),

    ("(", lambda: btnClik("("), 17, 340), (")", lambda: btnClik(")"), 107, 340),
    ("%", lambda: btnClik("%"), 197, 340), ("√", lambda: btnClik("sqrt("), 287, 340),

    ("EXP", lambda: btnClik("**"), 17, 400), ("ln", lambda: btnClik("log("), 107, 400),
    ("π", lambda: btnClik("pi"), 197, 400), ("C", clear, 287, 400),
]

# Crear botones
for (texto, comando, x, y) in botones:
    Button(ventana, text=texto, bg=color_boton, width=ancho_boton,
           height=alto_boton, command=comando).place(x=x, y=y)

# Inicializa pantalla con 0
clear()

# Ejecutar interfaz
ventana.mainloop()