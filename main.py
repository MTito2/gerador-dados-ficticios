import json
import config as c

dados = []

for i in range(100):
    
    nome_completo = c.nome_completo()
    sexo = c.descobrir_genero(nome_completo)
    cargo = c.definir_cargos()
    data_admissao = c.data_admissao()
    data_desligamento = c.data_desligamento(data_admissao)
    status = c.status(data_desligamento)
    salario, plano_saude, cartao_alimentacao = c.beneficios()
    endereco_estado = c.estado()
    pontualidade, trabalho_equipe,  cumprimento_metas = c.pontuacao_da_avaliacao() 
    data_avaliacao = c.data_avalicao(data_admissao)

    dados_pessoa = {
        "nome": nome_completo,
        "sexo": sexo,
        "cargo": cargo,
        "data_admissao": data_admissao,
        "data_desligamento": data_desligamento,
        "status": status,
        "salario": salario,
        "plano_saude": plano_saude,
        "cartao_alimentacao": cartao_alimentacao,
        "endereco_estado": endereco_estado,
        "pontualidade": pontualidade,
        "trabalho_equipe": trabalho_equipe,
        "cumprimento_metas": cumprimento_metas,
        "data_avaliacao": data_avaliacao
    }

    dados.append(dados_pessoa)

with open("dados_gerados.json", "w", encoding= "utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
