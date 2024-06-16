import os

def renomear_arquivos(pasta, estilo):
    # Caminho completo para a pasta "files"
    pasta_files = os.path.join(pasta, "files")
    
    # Verifica se a pasta "files" existe
    if not os.path.exists(pasta_files):
        print("Pasta 'files' não encontrada.")
        return
    
    # Lista todos os arquivos na pasta "files"
    arquivos = os.listdir(pasta_files)
    
    # Loop pelos arquivos na pasta "files"
    for arquivo in arquivos:
        # Verifica se é um arquivo (ignora subpastas)
        if os.path.isfile(os.path.join(pasta_files, arquivo)):
            # Escolha do estilo de formatação
            if estilo == "minusculas":
                novo_nome = os.path.join(pasta_files, arquivo.lower())
            elif estilo == "maiusculas":
                novo_nome = os.path.join(pasta_files, arquivo.upper())
            elif estilo == "titulo":
                novo_nome = os.path.join(pasta_files, arquivo.title())
            else:
                print("Estilo de formatação não reconhecido.")
                return
            
            # Renomeia o arquivo
            os.rename(os.path.join(pasta_files, arquivo), novo_nome)
            
            print(f"Arquivo renomeado: {arquivo} -> {novo_nome}")

def menu():
    print("Escolha um estilo de formatação:")
    print("1. Minúsculas")
    print("2. Maiúsculas")
    print("3. Título")
    opcao = input("Digite o número correspondente: ")
    
    if opcao == "1":
        return "minusculas"
    elif opcao == "2":
        return "maiusculas"
    elif opcao == "3":
        return "titulo"
    else:
        print("Opção inválida.")
        return None

# Caminho da pasta onde o script está localizado
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Chama o menu e obtém o estilo de formatação escolhido
estilo = menu()

if estilo:
    # Chama a função para renomear os arquivos na pasta "files"
    renomear_arquivos(diretorio_script, estilo)
