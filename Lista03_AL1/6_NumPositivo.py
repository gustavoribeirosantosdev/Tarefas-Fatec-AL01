n = int(input("Quantos números serão digitados? "))

contador = 1
positivos = 0

while contador <= n:
    numero = float(input("Digite um número: "))

    if numero > 0:
        positivos = positivos + 1
    contador = contador + 1

print("Quantidade de números positivos:", positivos)