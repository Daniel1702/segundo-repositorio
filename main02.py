__author__ = "Daniel de Andrade"
print("----Aumento De Salário----")

salario = float(input("Digite o valor do Salário: ").replace(',','.'))
porcent = float(input("Digite a porcentagem do aumento: ").replace(',','.'))

calc = salario * (porcent/100)
novoS = salario + calc

print("O Valor do Salário com o aumento é de R$%.2f"%novoS)