"""
Escreva um algoritmo que leia 10 números inteiros, ordene-os de forma crescente e imprima-os.
O processamento deverá ser feito por uma função que retorna uma lista.
"""

numeros = []

for i in range(10):
  numeros.append(int(input("Digite um Número: ")))

numeros.sort()
print(numeros)
