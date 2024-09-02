
saldo = 0
limite_valor_saque = 500
extrato = []
numero_saques = 0
LIMITE_DIARIO_SAQUES = 3


while True:

    print(""" 
    [D] - Depositar
    [S] - Sacar 
    [E] - Extrato
    [Q] - Sair
    """)

    opcao = input("Escolha umas das opções acima: ").upper()

#=============== DEPOSITAR ===============

    if opcao == "D":
        
        valor_deposito = float(input("Quanto você deseja depositar? "))
        if valor_deposito < 0:
            print("Operação Inválida")
        else:
            saldo += valor_deposito
            print(f"Depósito de R$ {valor_deposito:,.2f} realizado com sucesso !".replace(',', 'X').replace('.', ',').replace('X', '.') )
            descricao_deposito = f"Deposito realizado no valor de R$ {valor_deposito:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            extrato.append(descricao_deposito)

#=============== SACAR ===============              
    elif opcao == "S":

        valor_saque = float(input("Qual valor você deseja sacar? "))

     
        

        if valor_saque > limite_valor_saque or numero_saques >= LIMITE_DIARIO_SAQUES:
            print("Erro na operação! Você ja atingiu o limite de 3 saques por dia ou está sacando acima do limite máximo por saque que é R$ 500,00 !")
        
        elif valor_saque > saldo:
            print(f"Saldo Insuficiente, seu saldo atual é R$ {saldo:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
        
        else:
            saldo -= valor_saque
            print(f"O saque no valor de R$ {valor_saque:,.2f} foi realizado com sucesso !".replace(',', 'X').replace('.', ',').replace('X', '.'))
            descricao_saque = f"Saque realizado no valor de R$ {valor_saque:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            extrato.append(descricao_saque)
            numero_saques += 1

#=============== EXTRATO ===============
    elif opcao == "E":
        print("""=================== EXTRATO ===================""")
        for exibir_extrato in extrato:
        
                print(exibir_extrato)
        print(f"Saldo: R$ {saldo:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))    
    
#=============== SAIR ===============    
    elif opcao == "Q":
        break
    else:
        print("Opção Inválida")

