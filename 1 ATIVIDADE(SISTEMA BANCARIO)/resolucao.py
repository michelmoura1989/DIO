menu = """
       digite as letras abaixo:
       	
       	[d] = deposito
       	[s] = sacar
       	[e] = extrato
       	[q] = quit
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n" 
            
        else:
            print("Operação falhou! O valor informado é inválido")
    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação falhou! voce não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excedeu o limite.")
        elif excedeu_saque:
            print("Operação falhou! O numero maximo de saque excedido.")       
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            extrato  
    elif opcao == "e":
        print("-="*15)
        print("           EXTRATO     ")
        print(" ")
        print(extrato)
        print(f"Seu saldo total: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("digito invalido")
            

        