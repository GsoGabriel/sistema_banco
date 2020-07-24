# sistema de um banco
import sys
import csv

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

class Cliente():
	def __init__(self, agencia, conta, senha):
		self.agencia=agencia
		self.conta=conta
		self.senha=senha
	
	def verificar_cliente(self):
		arquivo_agencia = open('registro_contas_'+self.agencia+'.csv', 'r')
		arquivo_agencia = arquivo_agencia.read()
		arquivo_agencia = arquivo_agencia.split('\n')
		for x in arquivo_agencia:
			cliente = x.split(';')
			if cliente[0]==self.conta and cliente[1]==self.senha:
				print('Seja bem-vindo {}'.format(cliente[3]))
				return True

	def menu_usuario(self):
		menu=input('1 - Consultar Saldo em conta corrente\n2 - Consultar cartão de crédito\n3 - Depósito em conta corrente\n4 - Saque\nEscolha uma das opções ')
		return menu
	
	def consultar_saldo(self):
		with open('registro_saldo_'+self.agencia+'.csv', 'r+') as arquivo_saldo:
			reader = csv.reader(arquivo_saldo, delimiter=';')
			for saldo in reader:
				if saldo[0]==self.conta:
					print('Seu saldo é de R${}'.format(saldo[1]))
		
	def consultar_credito(self):
		with open('registro_credito_'+self.agencia+'.csv', 'r+') as arquivo_credito:
			reader = csv.reader(arquivo_credito, delimiter='\n')
			for x in reader:
				credito = x[0].split(';')
				limite_atual=int(credito[1])-int(credito[2])
				if credito[0]==self.conta:
					print('Seu limite total é de R${}\nVocê já utilizou do seu limite R${}\nSeu limite restante é de R${}'.format(credito[1],credito[2],limite_atual))

	def deposito(self):
		with open('registro_saldo_'+self.agencia+'.csv', 'r') as arquivo_saldo:
			ler_arquivo = csv.reader(arquivo_saldo, delimiter=';')
			dados = list(ler_arquivo)
			with open('registro_saldo_'+self.agencia+'.csv', 'w') as arquivo_saldo:
				writer = csv.writer(arquivo_saldo, delimiter=';')
				identificador = None
				for line in dados:
					conta, saldo = line
					if conta != self.conta:
						writer.writerow(line)
					else:
						deposito=input("Quanto deseja depositar? ")
						Cliente.confirmar_dados(self)
						confirmar_deposito = input("Pressione enter após colocar o dinheiro no local indicado.")
						saldo_novo = int(saldo) + int(deposito)
						new_line=[conta, saldo_novo]
						writer.writerow(new_line)
						print('Deposito realizado com sucesso! Seu saldo atual é de {}'.format(saldo_novo))
						

	def saque(self):
		with open('registro_saldo_'+self.agencia+'.csv', 'r') as arquivo_saldo:
			ler_arquivo = csv.reader(arquivo_saldo, delimiter=';')
			dados = list(ler_arquivo)
			with open('registro_saldo_'+self.agencia+'.csv', 'w') as arquivo_saldo:
				writer = csv.writer(arquivo_saldo, delimiter=';')
				identificador = None
				for line in dados:
					conta, saldo = line
					if conta != self.conta:
						writer.writerow(line)
					else:
						saque = int(input("Quanto deseja sacar? "))
						while saque>int(saldo):
							print('Valor maior que o saldo.')
							saque = int(input("Quanto deseja sacar? "))
						Cliente.confirmar_dados(self)
						saldo_novo = int(saldo) - int(saque)
						new_line=[conta, saldo_novo]
						writer.writerow(new_line)
						print('Saque realizado com sucesso! Seu saldo atual é de {}'.format(saldo_novo))
	
	def confirmar_dados(self):
		arquivo_agencia = open('registro_contas_'+self.agencia+'.csv', 'r')
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
	
	def mais_acoes(self):
		mais_acoes= input('Deseja realizar mais alguma ação?\n1 - Sim\n2 - Não')
		if mais_acoes=='1':
			return True
		else:
			return False

if __name__=='__main__':
	agencia=input('Agência: ')
	conta=input('Conta: ')
	senha=input('Senha: ')
	login=Cliente(agencia, conta, senha)
	print(login.agencia)
	#agencia='0001'
	#conta='10'
	#senha='1234'
	#verificar_cliente(agencia, conta, senha)
	#verificar_acesso()
	