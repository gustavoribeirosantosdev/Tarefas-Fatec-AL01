n = int(input("Quantos números serão digitados? "))

maior = float(input("Digite um número: "))

contador = 2

while contador <= n:
    numero = float(input("Digite um número: "))

    if numero > maior:
        maior = numero

    contador = contador + 1

print("O maior número é:", maior)