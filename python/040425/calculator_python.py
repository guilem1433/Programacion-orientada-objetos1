from tkinter import *
from math import *
import math


# VISUALIZAR LA OPERACIÓN EN LA PANTALLA
def btnClik(num):
    global operador
    operador = operador + str(num)
    input_text.set(operador)


# CÁLCULO Y MUESTRA DE RESULTADOS.
def resultado():
    global operador
    try:
        # Replace symbols with their corresponding Python functions
        opera = operador.replace("%", "/100")
        opera = opera.replace("√", "math.sqrt")
        opera = opera.replace("ln", "math.log")
        opera = opera.replace("EXP", "math.exp")
        opera = opera.replace("pi", str(math.pi))
        opera = opera.replace("^", "**")
        opera = str(eval(opera, {"math": math}))
        input_text.set(opera)
    except Exception as e:
        input_text.set("ERROR")
    operador = ""


# LIMPIEZA DE PANTALLA.
def clear():
    global operador
    operador = ""
    input_text.set("0")


# ELIMINAR EL ÚLTIMO CARÁCTER.
def delete():
    global operador
    operador = operador[:-1]
    input_text.set(operador)


ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("600x800")  # Increased window size
ventana.configure(background="SkyBlue4")
color_boton = "gray77"
ancho_boton = 5  # Button width
alto_boton = 2  # Button height
input_text = StringVar()
operador = ""

# Display field
Salida = Entry(ventana, font=('arial', 30, 'bold'), width=28,
               textvariable=input_text, bd=20, insertwidth=4, bg="powder blue", justify="right")
Salida.grid(row=0, column=0, columnspan=4, pady=20)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
    ("(", 5, 0), (")", 5, 1), ("%", 5, 2), ("=", 5, 3),
    ("√", 6, 0), ("π", 6, 1), ("EXP", 6, 2), ("ln", 6, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    Button(ventana, text=text, bg=color_boton, width=ancho_boton, height=alto_boton,
           font=('arial', 18), command=lambda t=text: btnClik(t) if t != "=" else resultado()).grid(row=row, column=col,
                                                                                                    padx=10, pady=10)

# Clear button functionality
Button(ventana, text="C", bg=color_boton, width=ancho_boton, height=alto_boton,
       font=('arial', 18), command=clear).grid(row=4, column=0, padx=10, pady=10)

# Delete button functionality
Button(ventana, text="DEL", bg=color_boton, width=ancho_boton, height=alto_boton,
       font=('arial', 18), command=delete).grid(row=4, column=1, padx=10, pady=10)

clear()
ventana.mainloop()