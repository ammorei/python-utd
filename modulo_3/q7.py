"""
Escreva um algoritmo que leia 8 números inteiros, conte os números primos e imprima a quantidade de números primos digitados.
Use procedimento para processar e função para impressão.
"""

numeros = []

for num in range(8):
  numeros.append(int(input("Digite um Número: ")))

numeros.sort()
#n_i = numeros[0]
#n_f = numeros[-1]
#print(n_i)
#print(n_f)
primos = []

#for n in range(n_i, n_f + 1):
for n in numeros:
  cont = 0
  for i in range(1, n + 1):
    if n % i == 0:
      cont = cont + 1
  if cont == 2:
    primos.append(n)

primos_str = str(primos)[1:-1]
print("Os números PRIMOS são: " + primos_str)
