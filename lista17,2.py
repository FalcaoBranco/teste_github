import math

# Função para calcular a quantidade de latas e galões de tinta necessários
def calcular_tinta(area):
    # Cálculo da quantidade de litros necessários
    litros = area / 6
    
    # Cálculo da quantidade de latas de tinta
    latas = math.ceil(litros / 18)
    
    # Cálculo da quantidade de galões de tinta
    galoes = math.ceil(litros / 3.6)
    
    return latas, galoes

# Função para calcular o custo total
def calcular_custo(latas, galoes):
    # Cálculo do custo total em latas de tinta
    custo_latas = latas * 80
    
    # Cálculo do custo total em galões de tinta
    custo_galoes = galoes * 25
    
    return custo_latas, custo_galoes

# Entrada do tamanho da área a ser pintada em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cálculo da quantidade de latas e galões de tinta necessários
latas, galoes = calcular_tinta(area)

# Cálculo do custo total
custo_latas, custo_galoes = calcular_custo(latas, galoes)

# Exibição dos resultados
print("Quantidade de latas de tinta necessárias:", latas)
print("Quantidade de galões de tinta necessários:", galoes)
print("Custo total em latas de tinta: R$", custo_latas)
print("Custo total em galões de tinta: R$", custo_galoes)
