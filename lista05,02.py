nota01 = float(input('Quanto foi a primeira nota?: '))
nota02 = float(input('Quanto foi a segunda nota?: '))
media = (nota01 + nota02) / 2 
if media < 6.0:
    print('Voce foi reprovado')
elif media >= 6.0 and media < 8.0:
    print('Voce foi aprovado!!!')
else:
    print('Voce passou muito bem!!!!')