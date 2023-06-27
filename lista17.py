import math

# Função para calcular a quantidade de tinta e o preço apenas com latas de 18 litros
def calcular_latas(area):
    litros = area / 6
    latas = math.ceil(litros / 18)
    preco = latas * 80
    return latas, preco

# Função para calcular a quantidade de tinta e o preço apenas com galões de 3,6 litros
def calcular_galoes(area):
    litros = area / 6
    galoes = math.ceil(litros / 3.6)
    preco = galoes * 25
    return galoes, preco

# Função para calcular a quantidade de tinta e o preço misturando latas e galões
def calcular_mistura(area):
    litros = area / 6
    latas = math.ceil(litros / 18)
    galoes = math.ceil((litros - latas * 18) / 3.6)
    preco = latas * 80 + galoes * 25
    return latas, galoes, preco

# Entrada do tamanho da área a ser pintada em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cálculo e exibição da quantidade de tinta e o preço apenas com latas de 18 litros
latas, preco_latas = calcular_latas(area)
print("Quantidade de latas de tinta necessárias (apenas latas):", latas)
print("Preço (apenas latas): R$", preco_latas)

# Cálculo e exibição da quantidade de tinta e o preço apenas com galões de 3,6 litros
galoes, preco_galoes = calcular_galoes(area)
print("Quantidade de galões de tinta necessários (apenas galões):", galoes)
print("Preço (apenas galões): R$", preco_galoes)

# Cálculo e exibição da quantidade de tinta e o preço misturando latas e galões
latas, galoes, preco_mistura = calcular_mistura(area)
print("Quantidade de latas de tinta necessárias (mistura):", latas)
print("Quantidade de galões de tinta necessários (mistura):", galoes)
print("Preço (mistura): R$", preco_mistura)
