# Sistema Bancário

### Objetivo Geral

Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

### Desafio

Fomos contratos por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas três operações: depósito, saque e extrato.

#### Operação de depósito

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com um usuário, dessa forma não precisaremos nos preocuár em identificar qual  é o número da âgencia e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

#### Operação de saque

O sistema deve permitir realizar três saques diários com limite máxio de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

#### Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ XXX.XX, exemplo:
1500.45 = R$ 1500.45

~~~
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
  opcao = input(menu)
  if opcao == 'd':
    print("Depósito")
  elif opcao == 's':
    print("Saque")
  if opcao == 'e':
    print("Extrato")
  if opcao == 'q':
    break
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
print("Obrigado e volte sempre!!")
~~~
