n = int(input("Quantos números serão digitados? "))
menor = float(input("Digite um número: "))

contador = 2

while contador <= n:
    numero = float(input("Digite um número: "))

    if numero < menor:
        menor = numero
    contador = contador + 1

print("O menor número é:", menor)