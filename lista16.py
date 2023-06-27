
metros_quadrados = float(input('Digite a Area em metros quadrados: '))
litro = 3*metros_quadrados
quantidade_de_latas = litro / 18
custo_total = 80 * quantidade_de_latas
print(f'A quantidade de litros que vão ser gastas é {quantidade_de_latas}')
print(f'E vai custar um total de R$:{custo_total}')