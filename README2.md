# Otiizando o Sistema Bancário com Funções Python

## Objetivo Geral
Separar as finções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadstrar conta bancária.

### Desafio
Precisamos deixar nosso código mais modularizado,para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)

#### Separação em funções
Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, podem ser definida por você da forma que achar melhor.

#### Saque
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques. Sugestão de retorno: saldo e extrato.

#### Depositar
A função depósito deve receber os argumentos apenas por posição (position only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retrono: saldo e extrato.

#### Extrato
A função extrato deve receber os argumentos por posição e nome (positiononly e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

### Novas funções
Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

#### Criar Usuário
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma string com o formato: logradourom numero - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuáriios com o mesmo CPF.

#### Criar conta corrente
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, inicando em 1. O número da agência é fixo: '0001'. O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

 ## Dica
> Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

