from tkinter import *
from math import *

ventana = Tk()
ventana.title("PAPU CALCULADORA")
ventana.geometry("400x600")
ventana.configure(background="SkyBlue4")
color_boton = "gray77"

input_text = StringVar()
operador = ""

# Set the display to show 0 initially
input_text.set("0")

# Function for handling button clicks
def btnClik(num):
    global operador
    operador += str(num)
    input_text.set(operador)

# Function to calculate the result
def resultado():
    global operador
    try:
        # Evaluate the expression
        opera = str(eval(operador.replace("pi", str(pi)).replace("√", "sqrt").replace("ln", "log")))
        input_text.set(opera)
        operador = opera
    except Exception as e:
        input_text.set("ERROR")
        operador = ""


# Function to clear the display
def clear():
    global operador
    operador = ""
    input_text.set("0")

# Function to delete the last character
def delete():
    global operador
    operador = operador[:-1]
    input_text.set(operador if operador else "0")

# Function to handle square root
def root():
    global operador
    try:
        # Calculate square root of the current input
        opera = str(sqrt(float(operador)))
        input_text.set(opera)
        operador = opera
    except Exception as e:
        input_text.set("ERROR")
        operador = ""

# Function to handle natural logarithm
def log_natural():
    global operador
    try:
        # Calculate natural logarithm of the current input
        opera = str(log(float(operador)))
        input_text.set(opera)
        operador = opera
    except Exception as e:
        input_text.set("ERROR")
        operador = ""


# Function to handle percentage operation
def percentage():
    global operador
    try:
        # Convert the current input to a percentage
        opera = str(float(operador) / 100)
        input_text.set(opera)
        operador = opera
    except Exception as e:
        input_text.set("ERROR")
        operador = ""

# Function to handle exponentiation
def exponent():
    global operador
    operador += "**"
    input_text.set(operador)

# Entry widget for the calculator's display
Salida = Entry(
    ventana,
    font=("arial", 20, "bold"),
    width=22,
    textvariable=input_text,
    bd=20,
    insertwidth=4,
    bg="powder blue",
    justify="right",
)
Salida.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ("0", 4, 0), ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("7", 1, 0),
    ("8", 1, 1), ("9", 1, 2), ("π", 1, 3), (".", 4, 1),
    ("+", 4, 2), ("-", 3, 3), ("*", 2, 3), ("/", 4, 3),
    ("√", 5, 0), ("(", 5, 1), (")", 5, 2), ("%", 5, 3),
    ("ln", 6, 0), ("C", 6, 1), ("EXP", 6, 2), ("=", 6, 3),
    ("DEL", 7, 0),
]

# Create buttons dynamically and add them to the grid
for (text, row, col) in buttons:
    if text == "=":
        action = resultado
    elif text == "C":
        action = clear
    elif text == "DEL":
        action = delete
    elif text == "√":
        action = root
    elif text == "ln":
        action = log_natural
    elif text == "%":
        action = percentage
    elif text == "EXP":
        action = exponent
    else:
        action = lambda t=text: btnClik(t)

    Button(
        ventana,
        text=text,
        bg=color_boton,
        width=8,
        height=2,
        font=("arial", 14),
        command=action,
    ).grid(row=row, column=col, padx=5, pady=5)

clear()

ventana.mainloop()