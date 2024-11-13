from rich import print

print(f"{'-'*30}[yellow]Sistema PetLover[VGT][/yellow]{'-'*30}")
#Usuários registrados

listUsuarios = []
listTEMP = []
listCliente = []
listPET = []
servicos = [['Tosa', 30],['Banho', 40],['Consulta', 100]]
historicoAtendimento = [[]]

while True:
    login = False
    if listUsuarios.count('A') == 0:
        print("Sem dados registrados, cadastre o administrador: ")
        listTEMP.insert(0, input("Nome do administrador: "))
        listTEMP.insert(1, input("Senha do administrador(Somente números): "))
        listTEMP.insert(2,'A')
        listUsuarios.append(listTEMP.copy())
        tipoAcesso = listUsuarios[0][2]
        print(listUsuarios)
        listTEMP.clear()
        login = True
        break
    else:
        nomeUsuario = input("Insira o nome de usuário: ")
        senhaUsuario = input("Insira a senha: ")
        for i in range(len(listUsuarios)):
            if nomeUsuario == listUsuarios[i][0]:
                if senhaUsuario == listUsuarios[i][1]:
                    print('deu bom')
                    login = True
                    tipoAcesso = listUsuarios[i][2]
                    break
                else:
                    print('Login não encontrado. Insira um nome e uma senha registrados')
    if login == True:
        break
if tipoAcesso == 'A':
    while True:
        print(f"{'-'*30}Qual função deseja acessar?{'-'*30}\n[0] Cadastro de funcionário\n[1] Cadastro para clientes\n[2] Cadastro para pet\n[3] Serviços de petshop\n[4] Atendimento ao pet\n[5] Gerenciamento de usuários\n[6] Saída do sistema")
        funcao = int(input("Insira: "))
        if funcao == 0:
            print("-------Cadastro de funcionário-------")
            nomeFuncionario = input("Nome do funcionário: ")
            senhaFuncionario = input(f"Senha de {nomeFuncionario}: ")
            listTEMP.append(nomeFuncionario)
            listTEMP.append(senhaFuncionario)
            listTEMP.append('F')
            listUsuarios.append(listTEMP.copy())
            listTEMP.clear()
        elif funcao == 1:
            print("-------Cadastro de cliente-------")
            listTEMP.append(input("Nome do cliente: "))
            listTEMP.append(input("CPF: "))
            listTEMP.append(int(input("Número de celular: ")))
            listTEMP.append(input("Email: "))
            listTEMP.append(int(input("CEP: ")))
            listTEMP.append('C')
            listCliente.append(listTEMP.copy())
            listTEMP.clear()
            print(listCliente)
        elif funcao == 2:
            print('Cadastro de [yellow]pets[/yellow]')
            listTEMP.append(input("Nome: "))
            listTEMP.append(input("Categoria(felino, canino, bovino, suíno, etc.): "))
            listTEMP.append(input("Raça: "))
            listTEMP.append(input("CPF do Dono: "))
            listTEMP.append('P')
            listPET.append(listTEMP.copy())
            listTEMP.clear()
        elif funcao == 3:
            print('|Serviços| |Preços|')
            for i in range(len(servicos)):
                print(servicos[i])
        elif funcao == 4:
            print(f"{'-'*30}Atendimento aos [yellow]pets[/yellow]{'-'*30}")
            atendEscolha = int(input('[0] Para conferir histórico de atendimentos\n[1] para consultar histórico de atendimento destinado a um pet específico\n[2] para novo atendimento.\nInsira: '))
            if atendEscolha == 0:
                for i in range(len(historicoAtendimento)):
                    print(historicoAtendimento[i])
            elif atendEscolha == 1:
                nomePet = input('Insira o nome do pet')
                try:
                    atendNum = historicoAtendimento.index(nomepet)
                    print(historicoAtendimento[atendNum])
                except:
                    print('Não encontrado.')
            elif atendEscolha == 2:
                nomepet = input("Nome do pet: ")
                petEncontrado = None 
                for pet in listPET:
                    if pet[0].lower() == nomepet.lower():
                        petEncontrado = pet
                        break
                if petEncontrado:
                    print(f"Pet encontrado: {petEncontrado}")
                    listTEMP.append(nomepet)
                    listTEMP.append(input("Serviço: "))
                    listTEMP.append(input("Data de Atendimento: "))
                    listTEMP.append(input("Agendamento: "))
                    listTEMP.append(input("Situação([C]ancelado, [E]fetivado, [R]emarcado): "))
                    historicoAtendimento.append(listTEMP.copy())
                    listTEMP.clear()
            else:
                print('Nome do pet não encontrado.')
        elif funcao == 5:
            print(f"{'-'*30}Lista de usuários{'-'*30}")
            for i in range(len(listUsuarios)):
                print(listUsuarios[i])
            print('[0] para Apagar usuário\n[1] para atualizar usuário\n[2] para sair')
            funcaoAdm = int(input('Insira: '))
            if funcaoAdm == 0:
                removeNum = int(input('Escolha o usuário a ser apagado pelo seu índice (sua posição contada a partir do 0): '))
                try: 
                    listUsuarios.remove(listUsuarios[removeNum])
                    print(f'Usuário removido.')
                except:
                    print('[red]Erro.[/red]')
            elif funcaoAdm == 1:
                attNum = int(input('Escolha o usuário a ser atualizado pelo seu índice (sua posição contada a partir do 0): '))
                attConfig = int(input('Oque deseja alterar?\n[0] para nome\n[1] para senha\n[2] para seu tipo de usuário.'))
                if attConfig == 0:
                    listUsuarios[attNum].insert(attConfig, input('Novo Nome:'))
                    listUsuarios[attNum].pop(attConfig+1)
                elif attConfig == 1:
                    listUsuarios[attNum].insert(attConfig, input('Nova Senha:'))
                    listUsuarios[attNum].pop(attConfig+1)
                elif attConfig == 2:
                    listUsuarios[attNum].insert(attConfig, input('Tipo[A para administrador ou F para funcionário]:'))
                    listUsuarios[attNum].pop(attConfig+1)
        elif funcao == 6:
            print("[red]Desligando...[/red]")
            break
if tipoAcesso == 'F':
    while True:
        print(f"{'-'*30}Qual função deseja acessar?{'-'*30}\n[0] Cadastro para clientes\n[1] Cadastro para pet\n[2] Serviços de petshop\n[3] Atendimento ao pet\n[4] Saída do sistema")
        funcao = int(input("Insira: "))
        if funcao == 0:
            print("-------Cadastro de cliente-------")
            listTEMP.append(input("Nome do cliente: "))
            listTEMP.append(input("CPF: "))
            listTEMP.append(int(input("Número de celular: ")))
            listTEMP.append(input("Email: "))
            listTEMP.append(int(input("CEP: ")))
            listTEMP.append('C')
            listCliente.append(listTEMP.copy())
            listTEMP.clear()
            print(listCliente)
        elif funcao == 1:
            print('Cadastro de [yellow]pets[/yellow]')
            listTEMP.append(input("Nome: "))
            listTEMP.append(input("Categoria(felino, canino, bovino, suíno, etc.): "))
            listTEMP.append(input("Raça: "))
            listTEMP.append(input("CPF do Dono: "))
            listTEMP.append('P')
            listPET.append(listTEMP.copy())
            listTEMP.clear()
        elif funcao == 2:
            print('|Serviços| |Preços|')
            for i in range(len(servicos)):
                print(servicos[i])
        elif funcao == 3:
            print(f"{'-'*30}Atendimento aos [yellow]pets[/yellow]{'-'*30}")
            atendEscolha = int(input('[0] Para conferir histórico de atendimentos\n[1] para consultar histórico de atendimento destinado a um pet específico\n[2] para novo atendimento.\nInsira: '))
            if atendEscolha == 0:
                for i in range(len(historicoAtendimento)):
                    print(historicoAtendimento[i])
            elif atendEscolha == 1:
                nomePet = input('Insira o nome do pet')
                try:
                    atendNum = historicoAtendimento.index(nomepet)
                    print(historicoAtendimento[atendNum])
                except:
                    print('Não encontrado.')
            elif atendEscolha == 2:
                nomepet = input("Nome do pet: ")
                petEncontrado = None 
                for pet in listPET:
                    if pet[0].lower() == nomepet.lower():
                        petEncontrado = pet
                        break
                if petEncontrado:
                    print(f"Pet encontrado: {petEncontrado}")
                    listTEMP.append(nomepet)
                    listTEMP.append(input("Serviço: "))
                    listTEMP.append(input("Data de Atendimento: "))
                    listTEMP.append(input("Agendamento: "))
                    listTEMP.append(input("Situação([C]ancelado, [E]fetivado, [R]emarcado): "))
                    historicoAtendimento.append(listTEMP.copy())
                    listTEMP.clear()
            else:
                print('Nome do pet não encontrado.')
        elif funcao == 4:
            print("[red]Desligando...[/red]")
            break