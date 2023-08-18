def main():
    menu = """

    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [0] Sair
    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = input(menu)
       
        if opcao == "1":
            valor = float(input("Valor do depósito: "))
            if valor > 0:
                saldo, extrato = depositar(saldo, valor, extrato)
            else:
                print("===> Valor inválido.")

        elif opcao == "2":
            valor = float(input("Valor do saque: "))
            if valor > 0:
                saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,)
            else:
                print("===> Valor inválido.")

        elif opcao == "3":
            listar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            nr_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, nr_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
           listar_contas(contas)
         
        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0":
            break

        else:
            print("\n===> Opção inválida")


def depositar(saldo, valor, extrato, /):
    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    print("\n===> Depósito efetuado com sucesso")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("\n===> Saldo insuficiente.")
    elif excedeu_limite:
        print("\n===> Valor excede o limite.")
    elif excedeu_saques:
        print("\n===> Limite de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n===> Saque realizado com sucesso")
    else:
        print("\n===>Valor inválido.")

    return saldo, extrato


def listar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente número): ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("\n===> Usuário já existe")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (rua, nr - bairro - cidade/uf): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n===> Novo usuário cadastrado")


def buscar_usuario(cpf, usuarios):
    usuarios_localizados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_localizados[0] if usuarios_localizados else None


def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do usuário: ")
    usuario = buscar_usuario(cpf, usuarios)
    if usuario:
        print("\n==> Conta criada com sucesso")
        return {"agencia": agencia, "nr_conta": numero_conta, "usuario": usuario}

    print("\n===> Usuário não encontrado")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            Conta:     {conta['nr_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("--------------------------------")
        print(linha)
    

main()