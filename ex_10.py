# 10 Entrar via teclado com o valor de cinco produtos. Após as entradas, digitar um valor referente ao pagamento da somatória destes valores. Calcular e exibir o troco que deverá ser devolvido.

p1 = float(input('Valor do primeiro produto: '))
p2 = float(input('Valor do segundo produto: '))
p3 = float(input('Valor do terceiro produto: '))
p4 = float(input('Valor do quarto produto: '))
p5 = float(input('Valor do quinto produto: '))

vtotal=  p1 + p2 + p3 + p4 + p5

vpago = float(input('Valor pago: '))

troco = vpago - vtotal

print('O seu troco é R${:.2f} ' .format(troco))