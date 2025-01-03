import gender_guesser.detector as gender
from faker import Faker

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