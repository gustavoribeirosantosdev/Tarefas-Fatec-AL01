numero = int(input("Digite um número inteiro positivo: "))

fatorial = 1
contador = 1

while contador <= numero:
    fatorial = fatorial * contador
    contador = contador + 1

print("O fatorial é:", fatorial)