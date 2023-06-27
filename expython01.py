d = int(input('Quantos dias o carro ficou alugado? :'))
km = int(input('Quantos kilometros foram rodados? :'))
custoD = d * 60
custoKM = km * (15/100)
custototal = custoD + custoKM
print(f'o Custo total a pagar é R${custototal:,.2f}')