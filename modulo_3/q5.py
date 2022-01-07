"""
Escreva um algoritmo que pergunte ao usuário, quanto ele ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, o algoritmo deverá calcular os descontos e o salário líquido, e mostrar conforme a tabela abaixo:

+ Salário Bruto: R$
- IR (11%): R$
- INSS (8%): R$
- Sindicato (5%): R$
= Salário Líquido: R$
"""

valor_hora = float(input("Digite o valor que você ganha por hora: "))
qt_horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = qt_horas_trabalhadas * valor_hora

ir = (11/100) * salario_bruto
inss = (8/100) * salario_bruto
sindicato = (5/100) * salario_bruto

salario_liquido = salario_bruto - (ir + inss + sindicato)

print("")
print("+ Salário Bruto: R$", salario_bruto)
print("- IR (11%): R$", ir)
print("- INSS (8%): R$", inss)
print("- Sindicato (5%): R$", sindicato)
print("= Salário Líquido: R$", salario_liquido)
