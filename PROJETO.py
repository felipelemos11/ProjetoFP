def menu():         # Função Menu
    while True:         # Estrutura de repetição
        print("\nMENU DE PETS -> Escolha uma opção:")
        print("1 - Adicionar pet\n2 - Listar pets\n3 - Editar pet\n4 - Excluir pet\n5 - Menu eventos\n0 - Voltar ao Menu Principal")

        opcao = input()         # Escolha de funcionalidade

        if opcao == '1':
            adicionar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            editar()
        elif opcao == '4':
            excluir()
        elif opcao == '5':
            menu_eventos()
        elif opcao == '0':
            break           # Terminar codigo
        else:
            print("Escolha uma opção válida")

def adicionar():           # Função Cadastrar pets
    nome = input("Nome do pet: ") 
    especie = input("Espécie: ")
    raca = input("Raça: ")
    data_nascimento = input("Data de nascimento (Dia/Mês/Ano): ")
    peso = input("Peso em Kg: ")

    try:            # Tratamento de Erro
        arquivo = open("Cadastro.txt", "a")         # Abrindo o arquivo de cadastro com "a" para ficar salvo
        arquivo.write(f"{nome} | {especie} | {raca} | {data_nascimento} | {peso}\n")            #adicionando pet
        arquivo.close()         #Fechando arquivo
        print("Pet Adicionado com sucesso!!")
    except:
        print("Erro ao adicionar pet")

def listar():           # Função listagem de pets
    print("\nLISTA DE PETS") 
    try:            # Tratamento de erro
        arquivo = open("Cadastro.txt","r")          # Abertura do arquivo usando o "r" para leitura
        pets = arquivo.readlines()          # Usando o readlines para separar os pets em indices
        arquivo.close()           # Fechando arquivo

        if not pets:            # Se não houver pets pra ele printar que não há pets
            print("Não há pets cadastrados!")
        for i,linha in enumerate(pets):
            dados = linha.strip().split(' | ')          # Separando os dados dos pets em linhas atribuindo a cada dado um index
            print(f"{i +1} -> Nome: {dados[0]} | Espécie: {dados[1]} | Raça: {dados[2]} | Data de Nascimento: {dados[3]} | Peso: {dados[4]} Kg")
    except FileNotFoundError:           # Tratamento de erro caso o arquivo não seja encontrado
        print("O arquivo de pets não foi encontrado")

def editar():           # Função edição de pets
    listar()            # Pedindo para listar os pets utilizando a função listar permitindo que o usuário escolha qual pet deseja editar
    try:            # Tratamento Erro
        arquivo = open("Cadastro.txt", "r")         # Abrindo arquivo com "r" para leitura do arquivo
        pets = arquivo.readlines()            # Utilizando o readlines para separar os pets em indices
        arquivo.close()             # Fechando o arquivo

        if not pets:
            print("Nao é possivel editar pets pois não há pets cadastrados\n")
        else:
            indice = int(input("Digite o número do pet que você deseja editar: "))          # Escolhendo o Pet que será editado por meio do indice 
            indice -= 1         # Ajuste do indice baseado em 0 

            if 0 <= indice < len(pets):         # Condicional para edicao de pet existente
                nome = input("Novo nome: ")
                especie = input("Nova especie: ")
                raca = input("Nova Raça: ")
                data_nascimento = input("Nova data de nascimento (Dia/Mês/Ano): ")
                peso = input("Novo peso em Kg: ")
                
                pets[indice] = f"{nome} | {especie} | {raca} | {data_nascimento} | {peso}\n"            # Conclusão da edicãao 

                arquivo = open("Cadastro.txt", "w")         # Abrindo arquivo com "w"
                arquivo.writelines(pets)            # Usando o .writelines para escrever mais de uma linha
                arquivo.close()         # Fechando arquivo
                print("Pet editado com sucesso!!")
            else:
                print("Pet não existente")          
    except ValueError:          # Tratamento Erro          
        print("Digite um número válido")
    except Exception as e:          # Tratamento Erro: guarda o erro na variável "e" e printa
        print("Erro ao editar pet: ", e)

def excluir():          # Função exclusãao de pets
    listar()            # Listando pets permitindo o usuario escolher o pet que sera excluido           
    try:
        arquivo = open("Cadastro.txt", "r")         # Abrindo o arquivo com "r" para leitura
        pets = arquivo.readlines()          # Separando os pets em indices com .readlines
        arquivo.close()         # Fechando arquivo
        if not pets:
            print("Nao é possivel remover pets pois não há pets cadastrados\n")
        else:

            indice = int(input("Digite o numero do pet que voce deseja remover: "))         # Escolhendo pet que sera excluido 
            indice -= 1         # Ajuste do indice baseado em 0 

            if 0 <= indice < len(pets):         # Condicional para exclusao de pet existente
                del pets[indice]            # Exclusao do pet escolhido

                arquivo = open("Cadastro.txt", "w")         # Abertura do arquivo com "w"
                arquivo.writelines(pets)            # Reescricao de todas as linhas dos pets menos a removida
                arquivo.close()         # Fechando o arquivo
                print("Pet excluido com sucesso")           #################################               
            else:
                print("Pet inexistente")
    except Exception as e:
        print("Erro ao remover pet: ", e)

def menu_eventos():
    print("\nMENU EVENTOS -> Escolha uma opção")
    print("1 - Adicionar evento\n2 - Listar eventos\n3 - Excluir eventos\n0 - Voltar ao menu principal")
    opcao = input()

    if opcao == '1':
        add_evento()
    elif opcao == '2':
        listar_eventos()
    elif opcao == '3':
        excluir_eventos()
    elif opcao == '0':
        menu()
    else:
        print("Opção inválida, tente novamente!")

def add_evento():
    try:
        arquivo = open("Cadastro.txt", "r")
        pets = arquivo.readlines()
        arquivo.close()

        if not pets:
            print("Não há pets cadastrados. Cadastre um pet antes de adicionar um evento.")
            return

        print("Escolha o pet para vincular ao evento:")
        for i, linha in enumerate(pets):
            dados = linha.strip().split(' | ')
            print(f"{i + 1} -> Nome: {dados[0]} | Espécie: {dados[1]} | Raça: {dados[2]}") 
    
        indice = int(input("Digite o numero do pet que voce deseja registrar um evento: "))
        indice -= 1

        if 0 <= indice <len(pets):
            nomePet = pets[indice].strip().split(" | ")[0]
            
            escolha = int(input("Escolha o evento que você deseja registrar:\n1 - Vacinas\n2 - Consulta veterinária\n3 - Aplicacao de medicamentos\n"))         ######################
            
            if escolha == 1:
                evento = 'Vacina'
            elif escolha == 2:
                evento = 'Consulta veterinária'
            elif escolha == 3:
                evento = 'Aplicacao de medicamentos'            ###########################
            else: 
                print("Escolha invalida, tente novamente")
                

            
            data = input("Data do Evento (Dia/Mês/Ano): ")
            obs = int(input("Você deseja adicionar alguma observacao?\n1 - Sim    2 - Nao\n"))         ###########################

            if obs == 1:
                observacao = input("Adicione a observacao: ")           ########################
            else:
                observacao = '...'
                print("Sem observacoes\n")            ###############
                
            arquivo_eventos = open("Eventos.txt", "a")
            arquivo_eventos.write(f"{nomePet}: {evento} | {data} | {observacao}\n")
            arquivo_eventos.close()

            print("Evento adicionado!!")
            

        else:
            print("Numero pet invalido")            ######################
    except FileNotFoundError:
        print("Arquivo de pets nao encontrado. Antes de adicionar um evento, cadastre um pet")          ################
    except ValueError:
        print("Entrada invalida. Digite um numero valido")              #######################
    except Exception as e:
        print("Erro ao adicionar evento: ", e)

def listar_eventos():
    print("\nLISTA DE EVENTOS")
    try:
        arquivo = open("Eventos.txt", "r")
        eventos = arquivo.readlines()
        arquivo.close()     

        if not eventos:
            print("Nao não há eventos cadastrados\n")  

        for i, evento in enumerate(eventos):
            print(f"{i+1} -> {evento.strip()}")

    except FileNotFoundError:
        print("Arquivo de eventos nao encontrado")
    except Exception as e:
        print("erro ao listar eventos: ", e)

def excluir_eventos():
    listar_eventos()            # Listando eventos permitindo o usuario escolher o evento que sera excluido           
    try:
        arquivo = open("Eventos.txt", "r")         # Abrindo o arquivo com "r" para leitura
        eventos = arquivo.readlines()          # Separando os eventos em indices com .readlines
        arquivo.close()         # Fechando arquivo
        if not eventos:
            print("Nao é possivel remover eventos pois não há eventos cadastrados\n")
        else:

            indice = int(input("Digite o numero do evento que voce deseja remover: "))         # Escolhendo evento que sera excluido 
            indice -= 1         # Ajuste do indice baseado em 0 

            if 0 <= indice < len(eventos):         # Condicional para exclusao de evento existente
                del eventos[indice]            # Exclusao do evento escolhido

                arquivo = open("Eventos.txt", "w")         # Abertura do arquivo com "w"
                arquivo.writelines(eventos)            # Reescricao de todas as linhas dos eventos menos a removida
                arquivo.close()         # Fechando o arquivo
                print("Evento excluido com sucesso")           #################################               
            else:
                print("Evento inexistente")
    except Exception as e:
        print("Erro ao remover evento: ", e)



menu()            

   

#with open("Eventos.txt", "w") as a:
    #pass  
#with open("Cadastro.txt", "w") as a:
    #pass  
















