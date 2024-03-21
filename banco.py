#variaveis globais
cpf = []
inserirCpf = 0
nome = []
inserirNome = ""
numeroConta = []
inserirNumeroConta = 0
saldo = 0
historicoDeDepositos = []
historicoDePix = []

#função para deixar bonitinho
def traco(x = 50):
  for i in range(0, x):
    print("=", end='')
  print("\n")

#função para voltar para o menuprincipal
def voltar():
	menuPrincipal()

#menu inicial para cadastro de conta
#falta percorrer a lista para saber se a conta já foi criada antes
def cadastrarConta():
  traco()
  inserirCpf = int(input('DIGITE O CPF: '))
  cpf.append(inserirCpf)
  inserirNome = input('DIGITE O NOME: ')
  nome.append(inserirNome)
  inserirNumeroConta = int(input('DIGITE A CONTA: '))
  numeroConta.append(inserirNumeroConta) 
  traco()

#menu principal do banco
#falta fazer a função para sair do banco
def menuPrincipal():
	traco()
	opcaoMenuPrincipal = int(input('BEM VINDOS AO BANCO TAL \n'
				'DIGITE A OPÇÃO A SEGUIR\n'
        '1 - ALTERAR/EXCLUSÃO DE CONTA \n'
        '2 - CONSULTAR/FAZER DEPOSITO \n'
        '3 - PIX \n'
				'4 - CONSULTAR EXTRATO \n'
        '5 - SAIR DA CONTA'))
	if opcaoMenuPrincipal == 1:
  	menuAlterarConta()
  elif opcaoMenuPrincipal == 2:
		menuDepositos()
 	elif opcaoMenuPrincipal == 3:
    menuPix()
	elif opcaoMenuPrincipal == 4:
  	menuExtrato()

    
                              
       
#menu para alteração e delete de conta
#falta fazer o processo de alteração e exclusão de conta
def menuAlterarConta():
  traco()
  print('VOCÊ DESEJA ALTERAR OU DELETAR A CONTA? \n'
				'SELECIONE A OPÇÃO A SEGUIR\n'
        '1 - DELETAR A CONTA \n'
        '2 - ALTERAR A CONTA \n')
  print('seu cpf é: ' , cpf[-1] )
  print('O numero da sua conta é: ' , numeroConta[-1])
  print('seu nome é: ' , nome[-1])
  traco()

#menu de depositos  e consulta de saldo
#deve estar faltando alguma coisa, só n lembro agr, analisa direitinho
def menuDepositos():
    traco()
    print('SEU SALDO É: ' , saldo , '\n'
          'O HISTÓRICO DE DEPOSITOS:' , historicoDeDepositos)
    opcaodeposito = int(input('SE DESEJA REALIZAR UM DEPOSITO DIGITE 1 \n'
                              'SE DESEJA VOLTAR PARA O MENU PRINCIPAL DIGITE 2'))
    if opcaodeposito == 1:
        deposito = float(input('DIGITE O VALOR QUE QUER INSERIR'))
        historicoDeDepositos.append(deposito)
        saldo = saldo + deposito
        print('SEU NOVO SALDO É:' ,saldo , '/n')
    elif opcaodeposito == 2:
        voltar()
    traco()
    
#menu de consulta/realização de pix
#deve estar faltando algo tbm, c é mó esquecido
def menuPix():
    traco()
    print('SEU SALDO É: ' , saldo , '\n')
    opcaopix = int(input('DIGITE 1 SE QUISER REALIZAR UM PIX \n'
                         'DIGITE 2 PARA VOLTAR PARA O MENU PRINCIPAL'))
    if opcaopix == 1:
      dia = int(input('DIGITE O DIA QUE QUER REALIZAR O PIX'))
      hora = int(input('DIGITE O HORARIO QUE QUER REALIZAR O PIX'))
      destino = input('DIGITE O DESTINO DO PIX')
      valor = float(input('DIGITE O VALOR DO PIX'))
      if valor > saldo:
          print('SEU SALDO É INSUFICIENTE')
      elif valor < saldo:
          saldo = saldo - valor
          historicoDePix.append(valor)
          saldoDestino = saldoDestino +  valor
          print('SEU NOVO SALDO É: ' , saldo , '\n'
                'O DESTINO ESCOLHIDO FOI: ' ,destino , '\n'
                'O SALDO DO DESTINO FICOU: ' , saldoDestino, '\n')
    if opcaopix == 2:
        voltar()
    traco()

#menu de consulta de extrato 
def menuExtrato():
    traco()
    print('SEU SALDO ATUAL É: ', saldo , '\n')
    opcaoExtrato = int(input('DIGITE 1 SE QUISER CONSULTAR O HISTORICO DE DEPOSITOS \n'
                             'DIGITE 2 SE QUISER CONSULTAR O HISTORICO DE PIX \n'
                             'DIGITE 3 SE QUISER VOLTAR PARA O MENU PRINCIPAL'))
    if opcaoExtrato == 1:
        print('SEU HISTORICO DE DEPOSITOS É: ' , historicoDeDepositos)
    elif opcaoExtrato == 2:
        print('SEU HISTORICO DE PIX É: ' , historicoDePix)
    elif opcaoExtrato == 3:
        voltar()
    traco()
    


cadastrarConta()
