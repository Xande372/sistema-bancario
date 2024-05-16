menu = '''
----- Sistema Bancário -----

[1] Depositar
[2] Sacar
[3] Extrato
[4] Saldo Disponível
[0] Finalizar Sessão

Selecione a operação desejada: 
----------------------------
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        
        valor = float(input('Informe o valor que deseja depositar:'))
        if valor > 0:
            saldo += valor
            extrato += (f'Depósito de R${valor:.2f}\n')
            print('Depósito realizado com sucesso!')
        else:
            print('O valor desejado não atende ao requisitos.')
    
    elif opcao == '2':
        
        valor = float(input('Informe o valor que deseja sacar:'))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print('Saldo insuficiente!')
        
        elif excedeu_limite:
            print('Operação falhou! Limite insuficiente.')

        elif excedeu_saques:
            print('Operação falhou! Limite de saques diários atingido.')
        
        elif valor > 0:
            saldo -= valor
            extrato += (f'Saque de R${valor:.2f}\n')
            numero_saques += 1
            print('Saque realizado com sucesso!')

        else:
            print('Operação falhou! o valor informado é inválido.')

    
    elif opcao == '3':
        print(f'----- Extrato -----')
        print(f'Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'-------------------')
                
    
    elif opcao == '4':
        print(f'----- Saldo -----')
        print(f'R${saldo:.2f}')
        print(f'-----------------')

    elif opcao == '0':
        break

    else:
        print('Operação inválida, selecione o correto número da operação desejada.')