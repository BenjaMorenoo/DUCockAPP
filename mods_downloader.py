import requests
import os
from pathlib import Path
from tkinter import messagebox

mods = [
    "FarmersDelight-1.21.1-1.2.7.jar",
    "Patchouli-1.21-88-NEOFORGE.jar",
    "XaerosWorldMap_1.39.2_NeoForge_1.21.jar",
    "Xaeros_Minimap_25.1.0_NeoForge_1.21.jar",
    "badpackets-neo-0.8.2.jar",
    "balm-neoforge-1.21.1-21.0.30.jar",
    "butcher-3.0.1-neoforge-1.21.1.jar",
    "cookingforblockheads-neoforge-1.21.1-21.1.11.jar",
    "etiquetas-1.0.0-neoforge-1.21.1.jar",
    "framework-neoforge-1.21.1-0.9.4.jar",
    "geckolib-neoforge-1.21.1-4.7.3.jar",
    "iris-neoforge-1.8.8+mc1.21.1.jar",
    "jei-1.21.1-neoforge-19.21.0.247.jar",
    "mcw-doors-1.1.2-mc1.21.1neoforge.jar",
    "mcw-stairs-1.0.1-1.21.1neoforge.jar",
    "moredelight-25.01.13a-1.21-neoforge.jar",
    "multibeds-neoforge-1.21.1-0.1.jar",
    "refurbished_furniture-neoforge-1.21.1-1.0.9.jar",
    "serversleep-mod.jar",
    "shetiphiancore-neoforge-1.21.1-0.3.jar",
    "sodium-neoforge-0.6.9+mc1.21.1.jar",
    "storagedelight-24.12.15-1.21-neoforge.jar",
    "u_team_core-neoforge-1.21.1-5.6.2.354.jar",
    "useful_backpacks-neoforge-1.21.1-3.0.2.128.jar",
    "wthit-neo-12.5.1.jar"
]

base_url = "https://github.com/BenjaMorenoo/DUCockAPP/raw/main/"
mods_url = "https://github.com/BenjaMorenoo/DUCockAPP/tree/main/mods"

def descargar_mods():
    try:
        user = os.getlogin()
        mods_dir = Path(f"C:/Users/{user}/AppData/Roaming/.minecraft/mods")
        mods_dir.mkdir(parents=True, exist_ok=True)

        for mod in mods:
            print(f"Descargando {mod}...")
            response = requests.get(mods_url + mod)
            if response.status_code == 200:
                with open(mods_dir / mod, 'wb') as f:
                    f.write(response.content)
            else:
                raise Exception(f"Error al descargar {mod}")
        messagebox.showinfo("Descarga Completada", "¡Todos los mods fueron descargados correctamente!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def descargar_neoforge():
    try:
        user = os.getlogin()
        downloads_dir = Path(f"C:/Users/{user}/Downloads")
        neoforge_installer = "neoforge-21.1.121-installer.jar"
        response = requests.get(base_url + neoforge_installer)

        if response.status_code == 200:
            with open(downloads_dir / neoforge_installer, 'wb') as f:
                f.write(response.content)
            messagebox.showinfo("Descarga Completa", f"NeoForge descargado en {downloads_dir}")
        else:
            raise Exception("No se pudo descargar NeoForge.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
