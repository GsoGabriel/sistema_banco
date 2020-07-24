from funcoes_usuario_funcionario import Cliente

#agencia=input('Agência: ')
#conta=input('Conta: ')
#senha=input('Senha: ')
cliente=Cliente('0001', '10', '1234')
mais_acoes=True
while mais_acoes==True:
	if cliente.verificar_cliente():
		menu = cliente.menu_usuario()
		if menu=='1':
			cliente.consultar_saldo()
			mais_acoes=cliente.mais_acoes()
		elif menu=='2':
			cliente.consultar_credito()
			mais_acoes=cliente.mais_acoes()
		elif menu=='3':
			cliente.deposito()
			mais_acoes=cliente.mais_acoes()
		elif menu=='4':
			cliente.saque()
			mais_acoes=cliente.mais_acoes()
		else:
			print('Opção inválida')