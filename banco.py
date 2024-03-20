mudanca = 0
cpf = []
nome = []
numeroConta = []
def traco(x = 50):
  for i in range(0, x):
    print("=", end='')
  print("\n")
  
    
def voltar():
	menuPrincipal()

def menuPrincipal():
	traco()
	print('BEM VINDOS AO BANCO TAL \n'
				'SELECIONE A OPÇÃO A SEGUIR\n'
        '1 - INSERIR CONTA \n'
        '2 - CONSULTAR CONTA \n'
        '3 - EXCLUIR CONTA/ALTERAR CONTA \n'
				'0 - SAIR \n')
	traco()
  mudanca = int(input("DIGITE O NÚMERO: "))
	return mudanca
    
def cadastrarConta():
     traco()
     cpf = int(input('DIGITE O CPF'))
     nome = input('DIGITE O NOME')
     numeroConta = int(input('DIGITE A CONTA'))
     
def menuConta():
    traco()
    print('BEM VINDOS MENU DE CONSULTORIA \n'
				'SELECIONE A OPÇÃO A SEGUIR\n'
        '1 - CONSULTA DE PIX \n'
        '2 - INSERIR PIX \n'
        '3 - CONSULTAR DEPOSITOS \n'
        '4 - INSERIR DEPOSITOS \n'
        '5 - CONSULTAR EXTRATO \n'
        '6 - DESEJO VOLTAR PARA O MENU PRINCIPAL')
    traco()
    

def menuAlterarConta():
    traco()
    print('VOCÊ DESEJA ALTERAR OU DELETAR A CONTA? \n'
				'SELECIONE A OPÇÃO A SEGUIR\n'
        '1 - DELETAR A CONTA \n'
        '2 - ALTERAR A CONTA \n')
    traco()

opcao = 100
while opcao != 0:
    opcao = menuPrincipal()
    if opcao == 1:
        opcao = menuConta()
        if opcao == 1:
          cadastrar_conta()
        elif opcao == 2:
        	consultar_conta()
        elif opcao == 3

'''
if mudanca == 1:
  menuConta()
elif mudanca == 3:
  menuAlterarConta()
elif mudanca == 6:
    voltar()
mudanca = int(input("DIGITE O NÚMERO: "))
'''