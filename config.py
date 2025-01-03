import gender_guesser.detector as gender
from faker import Faker
from datetime import datetime, date
import random

fake = Faker("pt-PT")

def nome_completo():
    abreviacoes = ("Dr. ", "Sra. ", "Srta. ", "Dra. ", "Sr. ")
    nome = fake.unique.name()
    
    for abreviacao in abreviacoes:
        if abreviacao in nome:
            nome = nome.replace(abreviacao, "")
        
    return nome

def descobrir_genero(nome_completo):
    nome = nome_completo.split(" ")
    nome = nome[0]

    detector_genero = gender.Detector()
    genero = "M" if detector_genero.get_gender(nome) in ("male", "mostly_male", "andy") else "F"
    return genero

def definir_cargos():
    cargos = [
        "CEO",
        "Desenvolvedor de Software Júnior",
        "Desenvolvedor de Software Pleno",
        "Desenvolvedor de Software Sênior",
        "Engenheiro de DevOps",
        "Product Manager",
        "Designer de UX/UI",
        "Especialista em Marketing Digital",
        "Analista de dados",
        "Especialista em Segurança da Informação",
        "Gestor de Vendas",
        "Auxiliar de serviços gerais",
        "Assitente de TI (Suporte Técnico)",
        "Gerente de TI",
        "Coordenador de Atendimento ao Cliente"
    ]

    peso = [1, 40, 20, 2, 2, 10, 2, 2, 20, 2, 40, 35, 2, 15, 2, 10, 20, 30, 2, 2]
    cargo = random.choices(cargos, weights=peso, k=1)

    return cargo

def data_admissao():
    return fake.date_between_dates(date_start=date(2012, 1, 1))

def data_desligamento(data_inicio):
    data_admissao = datetime.strptime(data_inicio, "%Y/%m/%d")

    campo = [""]
    peso = [10, 1]
    data = fake.date_between_dates(date_start=data_admissao).strftime("%Y/%m/%d")
    campo.append(data)
    campo_final = random.choices(campo, weights=peso, k=1)

    return str(campo_final[0])

def status(data_desligamento):
    if data_desligamento == "":
        status = "Ativo"
    else:
        status = "Inativo"

    return status

def beneficios():
    salario = round(random.uniform(1500, 5000), 2)
    plano_saude = round(random.uniform(200, 500), 2)
    cartao_alimentacao = round(random.uniform(500, 1200), 2)

    return salario, plano_saude, cartao_alimentacao

def estado():
    return fake.estado_sigla()

def pontuacao_da_avaliacao():
    pontualidade = random.randint(5, 10)
    trabalho_em_equipe = random.randint(5, 10)
    cumprimento_metas = random.randint(5, 10)

    return pontualidade, trabalho_em_equipe, cumprimento_metas

def data_avalicao(data_inicio):
    data_admissao = datetime.strptime(data_inicio, "%Y/%m/%d")
    return fake.date_between_dates(date_start=data_admissao).strftime("%Y/%m/%d")