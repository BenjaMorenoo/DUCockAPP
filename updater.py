import requests
import json
import webbrowser
from tkinter import messagebox

version_actual = "1.0.0"
version_file_url = "https://github.com/BenjaMorenoo/DUCockAPP/raw/main/version.json"

def verificar_actualizacion():
    try:
        response = requests.get(version_file_url)
        if response.status_code == 200:
            datos = response.json()
            ultima_version = datos["latest_version"]
            changelog = datos["changelog"]
            download_url = datos["download_url"]

            if ultima_version != version_actual:
                resultado = messagebox.askyesno("Actualización Disponible",
                                                f"Nueva versión disponible: {ultima_version}\n\nCambios:\n{changelog}\n\n¿Deseas actualizar ahora?")
                if resultado:
                    webbrowser.open(download_url)
            else:
                messagebox.showinfo("Sin Actualizaciones", "Ya tienes la última versión.")
        else:
            raise Exception("No se pudo verificar la actualización.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_changelog():
    try:
        response = requests.get(version_file_url)
        if response.status_code == 200:
            datos = response.json()
            changelog = datos["changelog"]
            messagebox.showinfo("Cambios de Versión", changelog)
        else:
            raise Exception("No se pudo cargar el changelog.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
