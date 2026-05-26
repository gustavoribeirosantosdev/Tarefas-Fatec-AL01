import os

while True:
    try:
        n = int(input("Digite um número de 1 á 10 para o adivinhador tentar descobrir: "))
        if 1 <= n <= 10:
            break
        else:
            print("Número inválido!")
    except:
        print("Número inválido!")

tent = int(input("Digite aqui a quantidade de tentativas que o adivinhador poderá ter: "))

os.system("cls" if os.name == "nt" else "clear")

vezes = 1

while True:
    try:
        n2 = int(input("Qual o número que seu oponente escolheu entre 1 e 10? "))
        if 1 <= n2 <= 10:
            break
        else:
            print("Número inválido!")
    except:
        print("Número inválido!")

while n2 != n:
    vezes = vezes + 1
    if vezes > tent:
        break

    while True:
        try:
            n2 = int(input("Errou, tente novamente. Qual o número que seu oponente escolheu entre 1 e 10? "))
            if 1 <= n2 <= 10:
                break
            else:
                print("Número inválido!")
        except:
            print("Número inválido!")

if n2 == n:
    print("Parabéns! Você acertou e precisou de {} tentativas".format(vezes))
else:
    print("Suas tentativas acabaram.")   