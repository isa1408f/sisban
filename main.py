def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    lista_opcoes = ['d', 's', 'e', 'q']

    menu = """

    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair

    Escolha uma Opção:
    => """

    while True:
        opcao = str(input(menu)).lower()
        if not opcao in lista_opcoes:
            print("Opção Inválida")
            continue
        if opcao == "d" or opcao == "s":
            valor = float(input("Informe valor: "))
            if valor > 0:
                if opcao == "d":
                    saldo += valor
                    extrato += f'Deposito: R$ {valor: .2f}\n'
                if opcao == "s":
                    if numero_saques >= LIMITE_SAQUES:
                        print("Limite de Saques excedido")
                    elif valor > saldo:
                        print("Saldo insuficiente")
                    elif valor > limite:
                        print("Limite de saque excedido")
                    else:
                        saldo -= valor
                        extrato += f'Saque: R$ {valor: .2f}\n'
                        numero_saques += 1
            else:
                print("Valor Invalido")
        if opcao =="e":
            print("\n=============EXTRATO==============")
            print("Sem Movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo: .2f}")
            print("==================================")   

        if opcao == "q":
            break

main()
    

    
               
        





