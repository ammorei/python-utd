"""
Escreva um algoritmo que recebe do usuário os seguintes dados: matricula, nome, primeira nota e segunda nota.
Após a leitura, o algoritmo deverá calcular a média das duas notas e testar se o usuário foi aprovado ou não.
Efetuado o processamento anterior, o algoritmo deverá guardar a seguinte informação em um arquivo chamado alunos.txt:

– matricula
– nome
– primeira nota
– segunda nota
– media
– situação (aprovado ou reprovado)

Ao final, o algoritmo deverá ler o arquivo e mostrar informações apenas dos alunos aprovados.
Use função para processamento que retorna dicionário e considere 6.0 como média.
"""

matricula = input("Digite a Matrícula do Aluno: ")
aluno = input("Digite o Nome do Aluno: ")
nota1 = float(input("Digite a Primeira Nota do Aluno: "))
nota2 = float(input("Digite a Segunda Nota do Aluno: "))

media = (nota1 + nota2) / 2

if (media >= 6):
  situacao = "Aprovado"
else:
  situacao = "Reprovado"

cadastro = {}
cadastro['matricula'] = matricula
cadastro['aluno'] = aluno
cadastro['n1'] = nota1
cadastro['n2'] = nota2
cadastro['media'] = media
cadastro['sit'] = situacao

#print("\nO " + aluno + " ficou com a média: " + str(media) + "\nSua situação é: " + situacao)

#Cadastrar Alunos
arquivo = open("colegio.txt", "a")
arquivo.write(str(cadastro))
arquivo.write("\n")
arquivo.close()

#Alunos Cadastrados
arquivo = open("colegio.txt", "r")
conteudo = arquivo.readlines()
qtd = len(conteudo)
arquivo.seek(0)

print("Alunos Cadastrados:\n")

for a in range(0, qtd):
  dicAluno = {}
  dicAluno = eval(arquivo.readline())
  print("Matrícula: " + dicAluno['matricula'] + "| Aluno: " + dicAluno['aluno'])

arquivo.close()

#Alunos Aprovados
arquivo = open("colegio.txt", "r")
conteudo = arquivo.readlines()
qtd = len(conteudo)
arquivo.seek(0)

print("Alunos Aprovadoss:\n")

for a in range(0, qtd):
  dicAluno = {}
  dicAluno = eval(arquivo.readline())
  if dicAluno["media"] >= 6:
    print("Aluno: " + str(dicAluno["aluno"]) + ", Nota 1: " + str(dicAluno["n1"]) + ", Nota 2: " + str(dicAluno["n2"]) + ", Média: " + str(dicAluno["media"]))

arquivo.close()
