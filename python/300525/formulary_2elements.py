import tkinter as tk
from multiprocessing.resource_tracker import register
from tkinter import messagebox
import json
import os

class Formulary:
    def __init__(self, root):
        self.root = root
        self.root.title("Sys usuarios")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.users = {}
        self.cargar_usuarios()

        #main screen

        self.crear_main()

    def charge_users(self):
        #Charge users
        if os.path.exists("users.json"):
            with open("usuarios.json", "r") as archivo:
                try:
                    self.users = json.load(archivo)
                except:
                    self.users = {}

    def guardar_usuers(self):
        #save users in archive
        with open("users.json", "w") as archivo:
            json.dump(self.users, archivo)

    def create_main_screen(self):
        #clear screen
        for widget in self.root.winfo_children():
            widget.destroy()

        #frame principal
        frame = tk.Frame(self.root, padx = 20, pady= 20)
        frame.pack(expand=True)

        #title
        title = tk.Label(frame, text = "Bienvenido al sistema", font=("Arial", 16, "bold"))
        title.grid(row = 0, column=0, columnspan=2, pady=20)

        #buttons
        btn_iniciar = tk.Button(frame, text="Iniciar Sesión",
                                command=self.mostrar_login, width=15, height=2)
        btn_iniciar.grid(row=1, column=0, padx=10, pady=10)

        btn_registrar = tk.Button(frame, text="Registrarse",
                                  command=self.mostrar_registro, width=15, height=2)
        btn_registrar.grid(row=1, column=1, padx=1, pady=10)

    def show_login(self):
        #clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        #login frame
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        #title
        title = tk.label(frame, text="Login", font =("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady= 10)

        #Username
        username_label = tk.Label(frame, text="Username:")
        username_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        username_entry = tk.Entry(frame, width=20)
        username_entry.grid(row=1, colum=1, padx=5, pady=5)

        #Password
        password_label = tk.Entry(frame, width=20)
        username_entry.grid(row=2, column=1, padx=5, pady=5)

        #Confirm Password
        confirm_label = tk.Label(frame, text="Confirmar contrast:")
        confirm_label.grid(row=3, column=1, padx=5, pady=5)

        #Register Button
        register_button = tk.Button(frame, text="Register",
                                    command=lambda: self.register_user(username_entry.get(),
                                                                       password_entry.get(),
                                                                       confirm_entry.get()))
        register_button.grid(row=4, column=0, columnspan=2, pady=10)












