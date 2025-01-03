import gender_guesser.detector as gender
from faker import Faker
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