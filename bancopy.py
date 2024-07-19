from datetime import date
contas = []
depositos = []
pixs = []

def adicionadeposito(id, deposito):
    for hdepo in depositos:
        for i in range(len(hdepo)):
            if id == hdepo[0]:
                hdepo.append(deposito)

def adicionarpix(id, pix, recebe):
    for hpix in pixs:
        for i in range(len(hpix)):
            if id == hpix[0]:
                hpix.append(pix)
                hpix.append(date.today())
                hpix.append(recebe)

def traco(x=50):
    for i in range(0, x):
        print("=", end='')
    print("\n")

def menuExtrato():
    traco()
    id = int(input('DIGITE O CPF QUE IRÁ CONSULTAR: '))
    for conta in contas:
        for i in range(len(conta)):
            if id == conta[0]:
                print('SEU SALDO É:', conta[3])
                print('DIGITE 1 PARA VER O HISTORICO DE DEPOSITOS \n',
                    'DIGITE 2 PARA VER O HISTORICO DE PIX \n',
                    'DIGITE 3 PARA VOLTAR AO MENU PRINCIPAL')
                escolhas = int(input('DIGITE O NUMERO: '))
                if escolhas == 1:
                    for Hdeposito in depositos:
                        for i in range(len(Hdeposito)):
                            if id == Hdeposito[0]:
                                print('ESSE É SEU HISTORICO DE DEPOSITOS: \n' ,
                                    Hdeposito)
                                menuPrincipal()
                elif escolhas == 2:
                    for Hpix in pixs:
                        for i in range(len(Hpix)):
                            if id == Hpix[0]:
                                print('ESSE É O SEU HISTORICO DE PIX: \n',
                                    Hpix)
                                menuPrincipal()
                elif escolhas == 3:
                    menuPrincipal()
        #elif id != conta[0]:
    print('NÃO EXISTE ESSE CPF, ADICIONE-O')
    menuCadastro()

    traco()
    menuPrincipal()

def menuDepositos():
    traco()
    id = int(input('DIGITE O CPF QUE QUER FAZER UM DEPOSITO: '))
    for conta in contas:
        for i in range(len(conta)):
            if id == conta[0]:
                print('SEU SALDO É: ', conta[3])
                deposito = float(input('DIGITE O SEU DEPOSITO: '))
                conta[3] += deposito
                adicionadeposito(id, deposito)
                print(conta[3])
                menuPrincipal()
        
    print('NÃO EXISTE ESSE CPF, ADICIONE-O')
    menuCadastro()

    traco()

def menuPix():
    traco()
    id = int(input('DIGITE O CPF QUE IRÁ FAZER O PIX: '))
    for conta in contas:
        for i in range(len(conta)):
            if id == conta[0]:
                print('SEU SALDO É:' , conta[3])
                pix = int(input('DIGITE O VALOR DO PIX: '))
                if pix < conta[3]:
                    saldoorigem = conta[3] - pix
                    conta[3] = saldoorigem
                    recebe = int(input('DIGITE O CPF QUE IRÁ RECEBER O PIX: '))
                    for conta in contas:
                        for i in range(len(conta)):
                            if recebe == conta[0]:
                                recibimento(recebe, pix)
                                adicionarpix(id, pix, recebe)
                                menuPrincipal()
                    print('O CPF QUE ESTá RECEBENDO NÃO EXISTE')
                    menuPrincipal() 
                elif pix > conta[3]:
                    print('SALDO INSUFICIENTE')
                    menuPrincipal()
        #elif id != conta[0]:
    print('NÃO EXISTE ESSE CPF, ADICIONE-O')
    menuCadastro()

    traco()
    menuPrincipal()
            
def recibimento(recebidor, valor):
    for conta in contas:
        for i in range(len(conta)):
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
    depositos.append([cpf])
    pixs.append([cpf])
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
                conta[1] = novo_nome
                conta[0] = novo_cpf
                conta[2] = novo_numconta
    traco()
    menuPrincipal()



    
menuPrincipal()
