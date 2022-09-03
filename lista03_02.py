#10) Crie o seguinte programa Python no arquivo lista03_02.py: Colete o nome da pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. Depois você irá mostrar os dados coletados em linhas diferentes. E também, deverá informar quantos anos a pessoa terá no ano 2030
nome = str(input("Escreva seu nome completo?"))
cidade_nascimento = str(input("Digite o nome da cidade que você nasceu: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade= 2030-ano_nascimento

print(""" - Nome completo: {}
- Cidade de nascimento: {}
- Ano do nascimento: {}
Em 2030, terá {} anos.""".format(nome,cidade_nascimento,ano_nascimento,idade))