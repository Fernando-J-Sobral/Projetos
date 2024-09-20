# Sistema bancário simulado

usuarios = []
contas = []
numero_conta = 1

def criar_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    cpf = ''.join(filter(str.isdigit, cpf))  # Armazenar somente números do CPF
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado.")
        return None
    usuario = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso.")
    return usuario

def criar_conta(usuario):
    global numero_conta
    conta = {'agencia': "0001", 'numero_conta': numero_conta, 'usuario': usuario}
    contas.append(conta)
    numero_conta += 1
    print(f"Conta número {conta['numero_conta']} criada com sucesso para {usuario['nome']}.")

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, extrato
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, extrato
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    global saldo, extrato, numero_saques
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    print("Bem-vindo ao sistema bancário!")

    while True:
        print("\n=== Menu ===")
        print("[1] Criar Usuário")
        print("[2] Criar Conta Corrente")
        print("[3] Depositar")
        print("[4] Sacar")
        print("[5] Exibir Extrato")
        print("[6] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Informe o nome do usuário: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Informe o CPF: ")
            endereco = input("Informe o endereço (rua, bairro, numero, cidade, estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "2":
            cpf = input("Informe o CPF do usuário: ")
            usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
            if usuario:
                criar_conta(usuario)
            else:
                print("Usuário não encontrado.")

        elif opcao == "3":
            if not contas:
                print("Você precisa criar uma conta antes de depositar.")
                continue
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "4":
            if not contas:
                print("Você precisa criar uma conta antes de sacar.")
                continue
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                   numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "5":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida, por favor selecione novamente.")

if __name__ == "__main__":
    main()

