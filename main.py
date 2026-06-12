#importações da bibliotecas
import os
from datetime import datetime as dt
import json

#Anira eu aceito
def salvarLog(criado, removido):
    os.makedirs("log", exist_ok=True)
    log_file ="log/log.json"
    registro = {
        "data_hora" : dt.now().strftime("%Y/%m/%d %H:%M%S"), "criados" : criado, "removidos" : removido
    }
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as F:
            try:
                logs = json.load(F)
            except json.JSONDecodeError:
                logs =[]
    else:
        logs =[]
    logs.append(registro)
    with open(log_file, "w", encoding="utf-8") as F:
        json.dump(logs, F, indent=4, unsure_ascii = False) 
    
