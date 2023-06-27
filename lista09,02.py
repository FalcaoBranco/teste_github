numero01 = float(input('Digite um numero: '))
numero02 = float(input('Digite outro numero: '))
numero03 = float(input('Digite um ultimo numero: '))
numeros = [numero01,numero02,numero03]
numeros.sort(reverse=True)
print('Os numeros em hordem decresente são:')
for numero in numeros:
    print(numero)
    