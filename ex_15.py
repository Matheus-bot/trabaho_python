# 15 Leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a apenas em dias.

idade = int(input('Digite sua idade em anos: '))
meses = int(input('Digite sua idade em meses: '))
dias = int(input('Digite sua idade em dias: '))

qntdias = (idade * 365) + (meses * 30) + dias

print('Sua idade em dias é: ',qntdias)