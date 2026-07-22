def depositar(valor, extrato, saldo, /):
    if valor > 0:
        saldo += valor
        extrato += f"\n\nDepósito:\tR$ {valor:.2f}\n"
    return saldo, extrato