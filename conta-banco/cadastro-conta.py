def cadastrar_conta():
    print("==== Criação de Conta ====")

    nome = input("Digite o nome do titular da conta: ")
    agencia = input("Digite o número da agencia da conta: ")
    conta = input("Digite o número da conta: ")

    while True:
        saldo_str = input("Digite o saldo inicial: R$ ")
        try:
            saldo = float(saldo_str)
            break

        except ValueError:
            print("Saldo inválido. Por favor, digite um número válido.")

    print("\nConta criada com sucesso!")
    print("--------------------------")
    print(f"Titular: {nome}")
    print(f"Agência: {agencia}")
    print(f"Conta: {conta}")
    print(f"Saldo inicial: R$ {saldo:.2f}")
    print("--------------------------")

cadastrar_conta()
