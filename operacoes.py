def depositar(valor, extrato, saldo, /):
    if valor > 0:
        saldo += valor
        extrato += f"\n\nDepósito:\tR$ {valor:.2f}\n"
    return saldo, extrato


def sacar(
    *,
    saldo,
    valor,
    extrato,
    limite,
    numeros_saques,
    limite_saques,
):
    # todos os parâmetros após * terão que ser passado nomeado
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques >= limite_saques

    if excedeu_saldo:
        mensagem = "\n@@@ Operação falhou! Você não tem saldo suficiente. @@@"

    elif excedeu_limite:
        mensagem = '\n@@@ Operação falhou! O valor do saque excede o limite. @@@'

    elif excedeu_saques:
        mensagem = "\n@@@ Operação falhou! Número máximo de saques excedido. @@@"

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numeros_saques += 1
        mensagem = "\n=== Saque realizado com sucesso ! ==="

    else:
        mensagem = "\n@@@ Operação falhou! O valor informado é inválido. @@@"

    return saldo, extrato, numeros_saques, mensagem


def formatar_extrato(
    *,
    saldo,
    extrato,
):
    movimentacoes = extrato.strip() or "Não foram realizadas movimentações."

    return (
        "\n================ Extrato ================\n"
        f"{movimentacoes}"
        f"\n\nSaldo: R$ {saldo:.2f}\n"
        "============================================"
    )
