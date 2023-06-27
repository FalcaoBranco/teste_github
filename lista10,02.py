turno = input('Em qual turno voce trabalha digite M para matutino V para vespertino e N para noturno')
if turno == 'm' or turno == 'M':
    print('Bom dia')
elif turno == 'v' or turno == 'V':
    print('Boa tarde')
elif turno == 'n' or turno == 'N':
    print('Boa noite')
else:
    print('Voce digitou algo que não estava na lista erro')