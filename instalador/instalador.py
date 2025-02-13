import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Caminho padrão do Minecraft no Windows
default_minecraft_path = os.path.join(os.getenv('APPDATA'), ".minecraft")

# Criar janela para o usuário selecionar a pasta .minecraft
root = tk.Tk()
root.withdraw()
minecraft_path = filedialog.askdirectory(title="Selecione a pasta .minecraft", initialdir=default_minecraft_path)

# Se o usuário cancelar a instalação
if not minecraft_path:
    messagebox.showwarning("Instalação Cancelada", "Nenhum diretório selecionado. A instalação foi cancelada.")
    exit()

# Caminho onde estão os arquivos do modpack (pasta do script + caminho do modpack)
script_dir = os.path.dirname(os.path.abspath(__file__))
modpack_source = os.path.join(script_dir, "(abra essa pasta e copie tudo para .minecraft)")

# Pastas e arquivos do modpack
items_to_move = ["mods", "config", "resourcepacks", "shaderpacks", "options.txt"]
backup_path = os.path.join(minecraft_path, "BACKUP-MODPACK")

# Criar pasta de backup se não existir
if not os.path.exists(backup_path):
    os.makedirs(backup_path)

# 1️⃣ MOVER OS ARQUIVOS ORIGINAIS PARA O BACKUP
for item in items_to_move:
    source = os.path.join(minecraft_path, item)
    destination = os.path.join(backup_path, item)
    
    if os.path.exists(source):
        shutil.move(source, destination)

# 2️⃣ COPIAR OS NOVOS ARQUIVOS DO MODPACK PARA A PASTA .MINECRAFT
for item in items_to_move:
    source = os.path.join(modpack_source, item)
    destination = os.path.join(minecraft_path, item)

    if os.path.exists(source):
        if os.path.isdir(source):
            # Copiar pastas inteiras
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            # Copiar arquivos individuais
            shutil.copy2(source, destination)

messagebox.showinfo("Instalação Concluída", "Modpack instalado com sucesso!")
