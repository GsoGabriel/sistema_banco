# sistema de um banco
import sys

def teste():
	isso= int(input('tudo'))


def verificar_acesso():
	verificar=0
	while verificar != 1 or verificar != 2:
		#try:
			verificar=int(input('1 - Cliente \n2 - Funcionário\nVocê é um cliente ou funcionário? Digite o número associado.'))
			if verificar == 1 or verificar == 2:
				login_cliente()
				break
		#except:
			#print('deu algum erro')
			#pass

def login_cliente():
	agencia=input('Agência: ')
	conta=input('Conta: ')
	senha=input('Senha: ')
	verificar_cliente(agencia, conta, senha)

def verificar_cliente(agencia, conta, senha):
	arquivo_agencia = open('registro_contas_'+agencia+'.cvs', 'r')
	arquivo_agencia = arquivo_agencia.read()
	arquivo_agencia = arquivo_agencia.split('\n')
	for x in arquivo_agencia:
		cliente = x.split(', ')
		if cliente[0]==conta and cliente[1]==senha:
			print('Seja bem-vindo {}'.format(cliente[3]))
			menu_usuario=input('1 - Consultar Saldo em conta corrente\n2 - Consultar cartão de crédito\n3 - Depósito em conta corrente\n4 - Saque\nEscolha uma das opções ')
			print('\n')
			if menu_usuario=='1':
				consultar_saldo(agencia, conta, senha)
			elif menu_usuario=='2':
				consultar_credito(agencia, conta, senha)
			elif menu_usuario=='3':
				deposito(agencia, conta, senha)
			elif menu_usuario=='4':
				saque(agencia, conta, senha)
			else:
				print('opcao invalida')

def consultar_saldo(agencia, conta, senha):
	arquivo_saldo = open('registro_saldo_'+agencia+'.cvs', 'r')
	arquivo_saldo = arquivo_saldo.read()
	arquivo_saldo = arquivo_saldo.split('\n')
	for x in arquivo_saldo:
		saldo = x.split(', ')
		if saldo[0]==conta:
			print('Seu saldo é de R${}'.format(saldo[1]))
	mais_acoes(agencia, conta, senha)
	
def consultar_credito(agencia, conta, senha):
	arquivo_credito = open('registro_credito_'+agencia+'.cvs', 'r')
	arquivo_credito = arquivo_credito.read()
	arquivo_credito = arquivo_credito.split('\n')
	for x in arquivo_credito:
		credito = x.split(', ')
		limite_atual=int(credito[1])-int(credito[2])
		if credito[0]==conta:
			print('Seu limite total é de R${}\nVocê já utilizou do seu limite R${}\nSeu limite restante é de R${}'.format(credito[1],credito[2],limite_atual))
	mais_acoes(agencia, conta, senha)

def deposito(agencia, conta, senha):
	arquivo_saldo = open('registro_saldo_'+agencia+'.cvs', 'r')
	arquivo_saldo = arquivo_saldo.read()
	arquivo_saldo = arquivo_saldo.split('\n')
	for x in arquivo_saldo:
		saldo = x.split(', ')
		if saldo[0]==conta:
			deposito=int(input('Quanto deseja depositar? ') )
			confirmar_dados(agencia, conta, senha)
			saldo[1]=int(saldo[1]) + deposito
			
	mais_acoes(agencia, conta, senha)

def confirmar_dados(agencia, conta, senha):
	arquivo_agencia = open('registro_contas_'+agencia+'.cvs', 'r')
	arquivo_agencia = arquivo_agencia.read()
	arquivo_agencia = arquivo_agencia.split('\n')
	for x in arquivo_agencia:
		cliente = x.split(', ')
		confirmar_tel=input('Para sua segurança, confirme seu telefone (com DDD e apenas números): ')
		confirmar_cpf=input('Para sua segurança, confirme seu CPF (apenas números): ')
		if confirmar_tel!=cliente[4] or confirmar_cpf!=cliente[2]:
			print('Dados incompatíveis. Encerrando aplicação.')
			sys.exit()
		else:
			print('Dados compatíveis.')
			break
	

def mais_acoes(agencia, conta, senha):
	mais_acoes= input('Deseja realizar mais alguma ação?\n1 - Sim\n2 - Não')
	if mais_acoes=='1':
		verificar_cliente(agencia, conta, senha)
	else:
		pass

agencia='0001'
conta='10'
senha='1234'
verificar_cliente(agencia, conta, senha)
#verificar_acesso()
