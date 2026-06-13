import os
import json
from datetime import datetime


def criar_gitkeep(caminho):
    gitkeep = os.path.join(caminho, ".gitkeep")

    if not os.path.exists(gitkeep):
        open(gitkeep, "w").close()
        return gitkeep

    return None


def remover_gitkeep(caminho):
    gitkeep = os.path.join(caminho, ".gitkeep")

    if os.path.exists(gitkeep):
        os.remove(gitkeep)
        return gitkeep

    return None


def salvar_log(criados, removidos):

    os.makedirs("logs", exist_ok=True)

    arquivo_log = os.path.join("logs", "log.json")

    registro = {
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "gitkeep_criados": criados,
        "gitkeep_removidos": removidos
    }

    logs = []

    if os.path.exists(arquivo_log):
        try:
            with open(arquivo_log, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(registro)

    with open(arquivo_log, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4, ensure_ascii=False)


def processar_repositorio():

    criados = []
    removidos = []

    for raiz, diretorios, arquivos in os.walk("."):

        if "logs" in diretorios:
            diretorios.remove("logs")

        arquivos_reais = [
            arquivo
            for arquivo in arquivos
            if arquivo != ".gitkeep"
        ]

        pasta_vazia = (
            len(arquivos_reais) == 0
            and len(diretorios) == 0
        )

        if pasta_vazia:

            criado = criar_gitkeep(raiz)

            if criado:
                criados.append(criado)

        else:

            removido = remover_gitkeep(raiz)

            if removido:
                removidos.append(removido)

    salvar_log(criados, removidos)

    print("\nExecução concluída!")

    print("\nGitkeep criados:")
    for item in criados:
        print(item)

    print("\nGitkeep removidos:")
    for item in removidos:
        print(item)


if __name__ == "__main__":
    processar_repositorio()
