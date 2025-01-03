# Gerador de dados fictícios com Python

Este repositório contém um sistema criado em Python para gerar dados fictícios de maneira personalizada e eficiente, ideal para uso em projetos que necessitam de informações simuladas para testes ou protótipos.

## Visão Geral

A ideia para este projeto surgiu da dificuldade em encontrar dados fictícios que atendessem às necessidades específicas do meu projeto. Após pesquisar diversas soluções online – incluindo sites pagos e com limitações de tamanho ou dados em outros idiomas – decidi desenvolver uma solução própria utilizando Python.

O resultado é um pequeno sistema que:

- Gera arquivos JSON altamente personalizáveis.
- Possui uma estrutura simples, fácil de consumir e adaptar.
- Oferece liberdade para ajustar o tamanho e o conteúdo dos dados conforme necessário.

## Tecnologias Utilizadas

- **[Faker](https://faker.readthedocs.io/)**: Biblioteca poderosa para a geração de dados fictícios, como nomes, endereços, números de telefone, entre outros. É possível criar provedores dinâmicos instanciando classes que herdam os atributos da classe pai `BaseProvider`, permitindo um nível elevado de personalização.
- **Random**: Utilizada para gerar dados pseudoaleatórios e complementar a funcionalidade da biblioteca Faker.

## Funcionalidades

- **Personalização Total**: Permite a geração de dados com campos, formatos e tamanhos ajustáveis.
- **Fácil Integração**: Os arquivos JSON gerados podem ser consumidos facilmente em diferentes aplicações.
- **Escalabilidade**: O sistema pode ser facilmente ajustado para adicionar ou modificar tipos de dados conforme as necessidades do projeto.

---

Feito com ❤️ por [Mateus](https://github.com/MTito2).
