from operacoes import depositar, formatar_extrato, sacar

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
        saldo_anterior = saldo
        saldo, extrato = depositar(valor, extrato, saldo)
        if saldo > saldo_anterior:
            print("Depósito realizado com sucesso!")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    elif opcao == 's':
        valor = float(input("Informe o valor do saque: R$ "))
        saldo, extrato, numeros_saques, mensagem = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            limite_saques=LIMITE_SAQUE,
            numeros_saques=numeros_saques
        )
        print(mensagem)
    elif opcao == 'e':
        texto_extrato = formatar_extrato(saldo=saldo, extrato=extrato)
        print(texto_extrato)
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