import os
import json
from datetime import datetime


# Cria um arquivo .gitkeep em uma pasta vazia
def criar_gitkeep(caminho):
    gitkeep = os.path.join(caminho, ".gitkeep")

    if not os.path.exists(gitkeep):
        open(gitkeep, "w").close()
        return gitkeep

    return None


# Remove o .gitkeep caso a pasta não esteja mais vazia
def remover_gitkeep(caminho):
    gitkeep = os.path.join(caminho, ".gitkeep")

    if os.path.exists(gitkeep):
        os.remove(gitkeep)
        return gitkeep

    return None


# Salva um histórico das alterações em um arquivo JSON
def salvar_log(criados, removidos):

    # Garante que a pasta de logs exista
    os.makedirs("logs", exist_ok=True)

    arquivo_log = os.path.join("logs", "log.json")

    # Cria um registro com data, hora e alterações realizadas
    registro = {
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "gitkeep_criados": criados,
        "gitkeep_removidos": removidos
    }

    logs = []

    # Carrega os logs antigos do JSON
    if os.path.exists(arquivo_log):
        try:
            with open(arquivo_log, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except:
            logs = []

    # Adiciona o novo registro à lista
    logs.append(registro)

    # Salva a lista atualizada no JSON
    with open(arquivo_log, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4, ensure_ascii=False)


# Percorre todas as pastas do repositório
def processar_repositorio():

    criados = []
    removidos = []

    for raiz, diretorios, arquivos in os.walk("."):

        # Ignora a pasta de logs
        if "logs" in diretorios:
            diretorios.remove("logs")

        # Lista apenas arquivos reais (ignora .gitkeep)
        arquivos_reais = [
            arquivo
            for arquivo in arquivos
            if arquivo != ".gitkeep"
        ]

        # Verifica se a pasta está vazia
        pasta_vazia = (
            len(arquivos_reais) == 0
            and len(diretorios) == 0
        )

        if pasta_vazia:

            # Cria .gitkeep em pastas vazias
            criado = criar_gitkeep(raiz)

            if criado:
                criados.append(criado)

        else:

            # Remove .gitkeep de pastas que possuem conteúdo
            removido = remover_gitkeep(raiz)

            if removido:
                removidos.append(removido)

    # Registra todas as alterações no log
    salvar_log(criados, removidos)

    # Exibe um resumo da execução
    print("\nExecução concluída!")

    print("\nGitkeep criados:")
    for item in criados:
        print(item)

    print("\nGitkeep removidos:")
    for item in removidos:
        print(item)


# Inicia a execução do programa
if __name__ == "__main__":
    processar_repositorio()