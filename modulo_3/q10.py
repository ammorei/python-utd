"""
Escreva um algoritmo que recebe uma frase como valor de entrada do usuário e imprima somente os índices das posições ocupadas por vogais.
A impressão deverá ser feita por procedimento que recebe parâmetros.
"""

lista = list(input("Digite Texto: "))

for v in lista:
  if v.lower() in 'aeiou':
    x = lista.index(v)
    print("A vogal: " + str(v) + " está na posição " + str(x))
