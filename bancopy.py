from datetime import date
contas = []
depositos = []
pixs = []


def traco(x=50):
    for i in range(0, x):
        print("=", end='')
    print("\n")

def menuExtrato():
    traco()
    id = int(input('DIGITE O CPF QUE IRÁ CONSULTAR: '))
    for conta in contas:
        if id == conta[0]:
            print('DIGITE 1 PARA VER O HISTORICO DE PIX \n',
                  'DIGITE 2 PARA VER O HISTORICO DE DEPOSITOS \n',
                  'DIGITE 3 PARA VOLTAR AO MENU PRINCIPAL')
            escolhas = ('DIGITE O NUMERO: ')
            if escolhas == 1:
                for deposito in depositos:
                    if id == deposito[0]:
                        print('ESSE É SEU HISTORICO DE DEPOSITOS: \n' ,
                              deposito)
            if escolhas == 2:
                for pix in pixs:
                    if id == pix[0]:
                        print('ESSE É O SEU HISTORICO DE PIX: \n',
                              pix)
            if escolhas == 3:
                menuPrincipal()
        elif id != conta[0]:
            print('NÃO EXISTE ESSE CPF, ADICIONE-O')
            menuCadastro()
    traco()
    menuPrincipal()

def menuDepositos():
    traco()
    for conta in contas:
        id = int(input('DIGITE O CPF QUE QUER FAZER UM DEPOSITO: '))
        if id == conta[0]:
            deposito = float(input('DIGITE O SEU DEPOSITO: '))
            conta[3] += deposito
            depositos.append([id, deposito])
            print(conta[3])
        elif id != conta[0]:
            print('NÃO EXISTE ESSE CPF, ADICIONE-O')
            menuCadastro()

    menuPrincipal()
    traco()

def menuPix():
    traco()
    for conta in (contas):
        id = int(input('DIGITE O CPF QUE IRÁ FAZER O PIX: '))
        if id == conta[0]:
            pix = int(input('DIGITE O VALOR DO PIX'))
            saldoorigem = conta[3] - pix
            conta[3] = saldoorigem
            recebe = int(input('DIGITE O CPF QUE IRÁ RECEBER O PIX: '))
            recibimento(recebe, pix)
            pixs.append([id, pix, date.today(), recebe])
        elif id != conta[0]:
            print('NÃO EXISTE ESSE CPF, ADICIONE-O')
            menuCadastro()

    traco()
    menuPrincipal()
            
def recibimento(recebidor, valor):
    for conta in contas:
        if recebidor == conta[0]:
            conta[3] += valor


def menuPrincipal():
    traco()
    print('BEM VINDOS AO BANCO TAL \n',
          'DIGITE A OPÇÃO A SEGUIR\n',
          '1 - CADASTRAR CONTA \n',
          '2 - ALTERAR/EXCLUSÃO DE CONTA \n',
          '3 - FAZER DEPOSITO \n',
          '4 - PIX \n',
          '5 - CONSULTAR EXTRATO \n',
          '6 - SAIR DA CONTA DO SISTEMA')

    escolha = int(input('DIGITE O NUMERO: '))

    if escolha == 1:
        menuCadastro()
    elif escolha == 2:
        menuAlterar()
    elif escolha == 3:
        menuDepositos() 
    elif escolha == 4:
        menuPix()
    elif escolha == 5:
        menuExtrato()
    elif escolha == 6:
        certeza = int(input('VOCÊ TEM CERTEZA QUE QUER FINALIZAR OS PROCESSOS? DIGITE 1 PARA SIM E 2 PARA VOLTAR'))
        if certeza == 1:
            quit()
        elif certeza == 2:
            menuPrincipal()
    traco()

def menuCadastro():
    traco()
    cpf = int(input("DIGITE O CPF: "))
    for conta in contas:
        #if cpf != conta[0]:
        #    continue
        if cpf == conta[0]:
            numconta = conta[1]
            nome = conta[2]
            saldo = conta[3]
            print("SEU CPF É: ", cpf, '\n',
                  "NUMERO DA CONTA: ", numconta, '\n',
                  "NOME: ", nome)
            menuPrincipal()

    print('NÃO EXISTE ESSE CPF, ADICIONE-O')
    print("CPF NÃO ESTÁ CADASTRADO")
    nome = input("DIGITE O NOME: ")
    numconta = input("DIGITE O NUMERO DA CONTA: ")
    saldo = 0
    contas.append([cpf, numconta, nome, saldo])
    print("CONTA ADICIONADA")
    menuPrincipal() 
    traco()


def menuAlterar():
    traco()
    print('VOCÊ DESEJA ALTERAR OU DELETAR A CONTA? \n'
          'SELECIONE A OPÇÃO A SEGUIR\n'
          '1 - DELETAR A CONTA \n'
          '2 - ALTERAR A CONTA \n')
    
    escolhaalt = int(input('DIGITE O NUMERO: '))
    if escolhaalt == 1:
        for conta in contas:
            cpf_deletado = int(input('DIGITE O CPF QUE A CONTA SERÁ DELETADA: '))
            if cpf_deletado == conta[0]:
                contas.remove(conta)
                print(contas)

    elif escolhaalt == 2:
        cpf_mudado = int(input('DIGITE O CPF QUE VAI SER MODIFICADO: '))
        for i, conta in enumerate(contas):
            if cpf_mudado == conta[0]:
                print('DIGITE OS NOVOS DADOS')
                novo_nome = input('DIGITE O NOVO NOME: ')
                novo_cpf = int(input('DIGITE O NOVO CPF: '))
                novo_numconta = input('DIGITE O NOVO NUMERO: ')
                mudancas = [novo_cpf, novo_numconta, novo_nome]
                contas[i] = mudancas
                print("A CONTA FOI MODIFICADA")
                print(contas)
    traco()
    menuPrincipal()



    
menuPrincipal()