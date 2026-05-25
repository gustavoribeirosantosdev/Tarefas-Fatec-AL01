import os

n = int(input("Digite um número de 0 á 10 para o adivinhador tentar descobrir: "))
tent = int(input("Digite aqui a quantidade de tentativas que o adivinhador poderá ter: "))

# limpa o terminal
os.system("cls")

vezes = 1

n2 = int(input("Qual o número que seu oponente escolheu entre 1 e 10? "))

while n2 != n:
    vezes = vezes + 1

    if vezes > tent:
        break

    n2 = int(input("Errou, tente novamente. Qual o número que seu oponente escolheu entre 1 e 10? "))

if n2 == n:
    print("Parabéns! Você acertou e precisou de {} tentativas".format(vezes))
else:
    print("Suas tentativas acabaram.")