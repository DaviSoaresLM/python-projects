def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


def multi(a, b):
    return a * b


def divi(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


print("Olá! Seja bem-vindo(a) à calculadora simples.")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = int(input("Digite sua escolha (1 a 4): "))

if escolha == 1:
    print(soma(valor1, valor2))

elif escolha == 2:
    print(sub(valor1, valor2))

elif escolha == 3:
    print(multi(valor1, valor2))

elif escolha == 4:
    print(divi(valor1, valor2))
else:
    print("Valor inválido, tente novamente com alguma das opções citadas anteriormente.")
