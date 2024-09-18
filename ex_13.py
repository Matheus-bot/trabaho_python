# 13 Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento. Exiba quantos litros o mesmo conseguiu colocar no tanque.

gasolina = 4.89
valor = float(input('Quantos Reais de gasolina você quer colocar? '))

total = valor/gasolina 

print('A quantidade de litros de gasolina por esse valor é de: {:.2f}'.format(total) , ' litros')