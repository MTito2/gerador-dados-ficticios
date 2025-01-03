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

