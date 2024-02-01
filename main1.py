menu = """
===============MENU===============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lu] Listar Usuários
    [q] Sair
==================================
=>"""

print(menu)

def depositar(valor, extrato, saldo, /): #tudo que está antes do / significa que os argumentos tem que ser passados por posição
    if valor > 0:
        saldo += valor
        extrato += f"\n\nDepósito:\tR$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso! ==")
    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeros_saques, limite_saques):# todos os parâmetros após * terão que ser passado nomeado
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques >= LIMITE_SAQUE

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo sificiente. @@@")

    elif excedeu_limite:
        print('\n@@@ Operação falhou! O valor do saque excede o limite. @@@')

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numeros_saques += 1
        print("\n=== Saque realizado com sucesso ! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ Extrato ================")
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input('Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('=== Usuário criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Tutular:\t{conta['usuario']['nome']}
        """
        print("=" *100)
        print(linha)

    return None

# Constantes
LIMITE_SAQUE = 3
NUMERO_AGENCIA = '0001'

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor a ser depositado: R$ "))
        depositar(valor, extrato, saldo)
    elif opcao == 's':
        valor = float(input("Informe o valor do saque: R$ "))
        sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, limite_saques=LIMITE_SAQUE, numeros_saques=numeros_saques)

    elif opcao == 'e':
      exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'nu':
        criar_usuario(usuarios)

    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta(NUMERO_AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == 'lc':
        listar_contas(contas)

    elif opcao == 'q':
        break
    else:
        print('Operação inválida, por favor selecione novamentea operação desejada.')
print("Obrigado por usar o nosso sistema. Volte Sempre")