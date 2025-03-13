#filtrar o arquivo json e retornar um dicionário com os dados filtrados

import json

def filtro_dados():
    with open('db\base_flashscore_temp_atual.json', 'r') as arquivo:
        dados = json.load(arquivo)
        dados_filtrados = {}
        for chave, valor in dados.items():
            if valor['quantidade'] > 100:
                dados_filtrados[chave] = valor
        return dados_filtrados
