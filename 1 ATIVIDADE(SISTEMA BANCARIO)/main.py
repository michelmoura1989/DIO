menu = """
       digite as letras abaixo:
       	
       	[d] = deposito
       	[s] = sacar
       	[e] = extrato
       	[q] = quit
"""
saldo = 0
extrato = []
deposito = 0
cont = 0
cores = {"amarelo": "\033[33m"}

while True:
	opcao = (input( menu))
	if opcao == "d":
		saldo += deposito
		extrato.append(int(input(" digite o deposito:  ")))
		saldo = sum(extrato)
	elif opcao == "s":
		cont += 1
		if cont <4:
			saque = int(input("digite seu saque: "))
			if saldo > saque:
				saldo -= saque
				extrato.append(saldo)
				print(f"{cont}")
			else:
				print("saldo insuficiente")
		else:
			print("Numero de saque excedido")
	elif opcao == "e":
		print(f"Seu historico foi: \033[0;30;41m{extrato}\033[m e seu extrato é {saldo}")	
	elif opcao == "q":
		break
	else:
		print("opção invalida")