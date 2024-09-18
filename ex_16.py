# 16 Leia a idade expressa em dias e mostre-as em anos, meses e dias 

idade_dias = int(input('Digite a idade em dias: '))

anos = idade_dias // 365
dias_restantes = idade_dias % 365
meses = dias_restantes // 30
dias = dias_restantes % 30

print('A idade é: {} anos, {} meses, e {} dias'.format(anos,meses,dias))