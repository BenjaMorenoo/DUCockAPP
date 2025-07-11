import customtkinter as ctk
from mods_downloader import descargar_mods, descargar_neoforge
from updater import verificar_actualizacion, mostrar_changelog
from PIL import Image  # Importamos Pillow para manejar imágenes

# Configuración inicial
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class DUCockLauncherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DUCock Launcher")
        self.geometry("600x400")
        self.resizable(False, False)

        # Cargar la imagen con Pillow
        image = Image.open("assets/background.png")

        # Fondo con imagen
        self.background_image = ctk.CTkImage(light_image=image, size=(600, 400))
        self.bg_label = ctk.CTkLabel(self, image=self.background_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Botones principales
        self.descargar_mods_btn = ctk.CTkButton(self, text="Descargar Mods", command=descargar_mods)
        self.descargar_mods_btn.place(relx=0.5, rely=0.3, anchor="center")

        self.descargar_neoforge_btn = ctk.CTkButton(self, text="Descargar NeoForge", command=descargar_neoforge)
        self.descargar_neoforge_btn.place(relx=0.5, rely=0.4, anchor="center")

        self.actualizar_btn = ctk.CTkButton(self, text="Buscar Actualizaciones", command=verificar_actualizacion)
        self.actualizar_btn.place(relx=0.5, rely=0.5, anchor="center")

        self.changelog_btn = ctk.CTkButton(self, text="Ver Cambios", command=mostrar_changelog)
        self.changelog_btn.place(relx=0.5, rely=0.6, anchor="center")


if __name__ == "__main__":
    app = DUCockLauncherApp()
    app.mainloop()
