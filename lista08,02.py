produto01 = float(input('Qual o preço do primeiro produto: '))
produto02 = float(input('Qual o preço do segundo produto: '))
produto03 = float(input('Qual o preço do ultimo produto: '))
mais_barato = min(produto01,produto02,produto03)
print(F'O produto que voce deve comprar é pois ele é o mais barato custando somente R$:{mais_barato}')