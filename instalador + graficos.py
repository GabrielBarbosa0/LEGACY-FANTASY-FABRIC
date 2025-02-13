import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

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
items_to_move = ["mods", "config", "resourcepacks", "shaderpacks"]
backup_path = os.path.join(minecraft_path, "BACKUP-MODPACK")

# Criar pasta de backup se não existir
if not os.path.exists(backup_path):
    os.makedirs(backup_path)

# Função para criar um nome único para o backup do options.txt
def get_unique_backup_name(base_path):
    count = 1
    new_name = f"{base_path}_OLD"
    while os.path.exists(new_name):
        new_name = f"{base_path}_OLD_{count}"
        count += 1
    return new_name

# 1️⃣ MOVER OS ARQUIVOS ORIGINAIS PARA O BACKUP (Se já existir, renomear ou excluir)
for item in items_to_move + ["options.txt"]:
    source = os.path.join(minecraft_path, item)
    destination = os.path.join(backup_path, item)

    if os.path.exists(source):
        if os.path.exists(destination):
            # Se for um arquivo, renomeia para um nome único
            if os.path.isfile(destination):
                new_backup_name = get_unique_backup_name(destination)
                os.rename(destination, new_backup_name)
            # Se for uma pasta, remove ela primeiro
            elif os.path.isdir(destination):
                shutil.rmtree(destination)

        shutil.move(source, destination)

# 2️⃣ COPIAR OS NOVOS ARQUIVOS DO MODPACK PARA A PASTA .MINECRAFT
for item in items_to_move:
    source = os.path.join(modpack_source, item)
    destination = os.path.join(minecraft_path, item)

    if os.path.exists(source):
        if os.path.isdir(source):
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(source, destination)

# 3️⃣ PERGUNTAR SOBRE A QUALIDADE GRÁFICA
while True:
    graphic_option = simpledialog.askstring("Configuração Gráfica", "Escolha a qualidade gráfica (Alto ou Baixo):", parent=root)
    
    if graphic_option:
        graphic_option = graphic_option.strip().lower()  # Normaliza a entrada para evitar erros
        
        if graphic_option in ["alto", "baixo"]:
            options_file = f"options_{graphic_option}.txt"  # ✅ Corrigido o erro da vírgula
            break  # Sai do loop se a entrada for válida
        else:
            messagebox.showwarning("Opção Inválida", "Digite 'Alto' ou 'Baixo' corretamente.")

# Copiar o arquivo correto para "options.txt"
source_options = os.path.join(modpack_source, options_file)
destination_options = os.path.join(minecraft_path, "options.txt")

if os.path.exists(source_options):
    shutil.copy2(source_options, destination_options)
    messagebox.showinfo("Configuração Aplicada", f"Gráficos {graphic_option.capitalize()} aplicados com sucesso!")
else:
    messagebox.showerror("Erro", f"Arquivo '{options_file}' não encontrado. Verifique se ele está na pasta do modpack.")

messagebox.showinfo("Instalação Concluída", "Modpack instalado com sucesso!")
