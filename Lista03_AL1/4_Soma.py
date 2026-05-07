n = int(input("Quantos números serão digitados? "))

soma = 0
contador = 1

while contador <= n:
    numero = float(input("Digite um número: "))

    soma = soma + numero
    contador = contador + 1
print("A soma dos valores é:", soma)