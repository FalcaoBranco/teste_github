Tamanho_arquivo = float(input('Qual é o tamanho do arquivo em MB? : '))
Velocidade_internet = float(input('Qual é a velocidade da internet? : '))

tamanho_bits = Tamanho_arquivo * 8 * 1024 * 1024
tempo_segundos = tamanho_bits / (Velocidade_internet * 1000000)
tempo_minutos = tempo_segundos / 60

print(f'O tempo aprocimado do dawnload é de {tempo_minutos} Minutos')
