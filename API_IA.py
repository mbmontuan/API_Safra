from datetime import datetime
import requests
import json
class apiIA():

    def getCodEmpresa(self, nome):
        url = 'http://localhost:3030/empresas'
        r = requests.get(url)
        retorno = ''
        for x in r.json()["empresas"]:
            if x["nome"] == nome:
                retorno = x["codigo"]
                break
        return retorno

    def getSentimento(self, codEmpresa,dataIni, dataFim):
        url = 'http://localhost:3030/sentimento/data/' + codEmpresa
        payload = {'dataInicio': dataIni, 'dataFim': dataFim}
        r = requests.get(url, data=payload)
        return r.json()["sentimento"]

codEmpresa = apiIA().getCodEmpresa("Santander")   #se nçao achar a empresa na busca, chatbot deve avisar que nçao encontrou pesquisas sobre a empresa
print("Codigo da empresa: " + codEmpresa)
print(apiIA().getSentimento(codEmpresa ,"05-06-2020", "12-06-2020"))
