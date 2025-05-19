metas_concluidas = []

def menu():       
    while True:         
        print("\nMENU DE PETS -> Escolha uma opção:")
        print("1 - Adicionar pet\n2 - Listar pets\n3 - Editar pet\n4 - Excluir pet\n5 - Menu eventos\n6 - Menu de Metas\n7 - Sugestões e Cuidados\n8 - Visão Geral de Pet\n0 - Voltar ao Menu Principal")

        opcao = input()         

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
        elif opcao == '6':
            menu_metas()
        elif opcao == '7':
            sugestoes_cuidados()
        elif opcao == '8':
            visao_geral_do_pet()
        elif opcao == '0':
            break           
        else:
            print("Escolha uma opção válida")

def adicionar():          
    nome = input("Nome do pet: ") 
    especie = input("Espécie: ")
    raca = input("Raça: ")
    data_nascimento = input("Data de nascimento (Dia/Mês/Ano): ")
    peso = input("Peso em Kg: ")

    try:           
        arquivo = open("Cadastro.txt", "a")         
        arquivo.write(f"{nome} | {especie} | {raca} | {data_nascimento} | {peso}\n")           
        arquivo.close()         
        print("\nPet Adicionado com sucesso!!")
    except:
        print("Erro ao adicionar pet")

def listar():          
    print("\nLISTA DE PETS") 
    try:            
        arquivo = open("Cadastro.txt","r")          
        pets = arquivo.readlines()         
        arquivo.close()           

        if not pets:            
            print("Não há pets cadastrados!")
        for i,linha in enumerate(pets):
            dados = linha.strip().split(' | ')          
            print(f"{i +1} -> Nome: {dados[0]} | Espécie: {dados[1]} | Raça: {dados[2]} | Data de Nascimento: {dados[3]} | Peso: {dados[4]} Kg")
    except FileNotFoundError:           
        print("O arquivo de pets não foi encontrado")

def editar():           
    listar()           
    try:           
        arquivo = open("Cadastro.txt", "r")         
        pets = arquivo.readlines()           
        arquivo.close()            

        if not pets:
            print("\nNão é possivel editar pets pois não há pets cadastrados\n")
        else:
            indice = int(input("\nDigite o número do pet que você deseja editar: "))          
            indice -= 1         

            if 0 <= indice < len(pets):        
                nome = input("Novo nome: ")
                especie = input("Nova especie: ")
                raca = input("Nova Raça: ")
                data_nascimento = input("Nova data de nascimento (Dia/Mês/Ano): ")
                peso = input("Novo peso em Kg: ")
                
                pets[indice] = f"{nome} | {especie} | {raca} | {data_nascimento} | {peso}\n"           

                arquivo = open("Cadastro.txt", "w")         
                arquivo.writelines(pets)           
                arquivo.close()        
                print("\nPet editado com sucesso!!")
            else:
                print("Pet não existente")          
    except ValueError:                   
        print("Digite um número válido")
    except Exception as e:          
        print("Erro ao editar pet: ", e)

def excluir():          
    listar()                     
    try:
        arquivo = open("Cadastro.txt", "r")         
        pets = arquivo.readlines()          
        arquivo.close()        
        if not pets:
            print("\nNão é possivel remover pets pois não há pets cadastrados\n")
        else:
            indice = int(input("\nDigite o número do pet que você deseja remover: "))     
            indice -= 1        

            if 0 <= indice < len(pets):         
                nome_pet_removido = pets[indice].strip().split(" | ")[0]  # <-- Nome do pet a ser removido

                del pets[indice]           

                # Atualiza o arquivo Cadastro.txt
                with open("Cadastro.txt", "w") as arquivo:
                    arquivo.writelines(pets)

                # Remoção dos eventos do pet
                try:
                    with open("Eventos.txt", "r") as arquivo_eventos:
                        eventos = arquivo_eventos.readlines()
                    with open("Eventos.txt", "w") as arquivo_eventos:
                        for evento in eventos:
                            if not evento.lower().startswith(nome_pet_removido.lower() + ":"):
                                arquivo_eventos.write(evento)
                except FileNotFoundError:
                    pass

                # Remoção das metas do pet
                try:
                    with open("Metas.txt", "r") as arquivo_metas:
                        metas = arquivo_metas.readlines()
                    with open("Metas.txt", "w") as arquivo_metas:
                        for meta in metas:
                            if not meta.lower().startswith(nome_pet_removido.lower() + ":"):
                                arquivo_metas.write(meta)
                except FileNotFoundError:
                    pass

                # Remoção das metas concluídas do pet
                global metas_concluidas
                metas_concluidas = [meta for meta in metas_concluidas if not meta.lower().startswith(nome_pet_removido.lower() + ":")]

                print("Pet e dados associados excluídos com sucesso")                          

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

        print("\nEscolha o pet para vincular ao evento:")
        for i, linha in enumerate(pets):
            dados = linha.strip().split(' | ')
            print(f"{i + 1} -> Nome: {dados[0]} | Espécie: {dados[1]} | Raça: {dados[2]}") 
    
        indice = int(input("\nDigite o número do pet que você deseja registrar um evento: "))
        indice -= 1

        if 0 <= indice <len(pets):
            nomePet = pets[indice].strip().split(" | ")[0]
            
            escolha = int(input("\nEscolha o evento que você deseja registrar:\n1 - Vacinas\n2 - Consulta veterinária\n3 - Aplicação de medicamentos\n"))         
            
            if escolha == 1:
                evento = 'Vacina'
            elif escolha == 2:
                evento = 'Consulta veterinária'
            elif escolha == 3:
                evento = 'Aplicação de medicamentos'            
            else: 
                print("Escolha inválida, tente novamente")
                return

            data = input("Data do Evento (Dia/Mês/Ano): ")
            obs = int(input("Você deseja adicionar alguma observação?\n1 - Sim    2 - Não\n"))         

            if obs == 1:
                observacao = input("Adicione a observação: ")         
            else:
                observacao = '...'
                print("Sem observações\n")            
                
            arquivo_eventos = open("Eventos.txt", "a")
            arquivo_eventos.write(f"{nomePet}: {evento} | {data} | {observacao}\n")
            arquivo_eventos.close()

            print("Evento adicionado!!")
        else:
            print("Número do pet inválido")            
    except FileNotFoundError:
        print("Arquivo de pets não encontrado. Antes de adicionar um evento, cadastre um pet")          
    except ValueError:
        print("Entrada inválida. Digite um número válido")              
    except Exception as e:
        print("Erro ao adicionar evento: ", e)

def listar_eventos():
    print("\nLISTA DE EVENTOS")
    try:
        arquivo = open("Eventos.txt", "r")
        eventos = arquivo.readlines()
        arquivo.close()     

        if not eventos:
            print("Não há eventos cadastrados\n")  
            return

        for i, evento in enumerate(eventos):
            print(f"{i+1} -> {evento.strip()}")
    except FileNotFoundError:
        print("Arquivo de eventos não encontrado")
    except Exception as e:
        print("Erro ao listar eventos: ", e)

def excluir_eventos():
    listar_eventos()                   
    try:
        arquivo = open("Eventos.txt", "r")       
        eventos = arquivo.readlines()        
        arquivo.close()         
        if not eventos:
            print("\nNão é possível remover eventos pois não há eventos cadastrados\n")
        else:
            indice = int(input("\nDigite o número do evento que você deseja remover: "))          
            indice -= 1         

            if 0 <= indice < len(eventos):         
                del eventos[indice]           
                arquivo = open("Eventos.txt", "w")        
                arquivo.writelines(eventos)            
                arquivo.close()         
                print("Evento excluído com sucesso")                        
            else:
                print("Evento inexistente")
    except Exception as e:
        print("Erro ao remover evento: ", e)

def menu_metas():
    while True:
        print("\nMENU METAS -> Escolha uma opção")
        print("1 - Adicionar meta\n2 - Listar metas\n3 - Concluir metas\n0 - Voltar ao menu principal")
        opcao = input()

        if opcao == '1':
            adicionar_meta()
        elif opcao == '2':
            listar_metas()
        elif opcao == '3':
            concluir_metas()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

def adicionar_meta():
    try:
        arquivo = open("Cadastro.txt", "r")
        pets = arquivo.readlines()
        arquivo.close()

        if not pets:
            print("Cadastre um pet antes de adicionar metas.")
            return

        print("\nEscolha o pet para vincular a meta:")
        for i, linha in enumerate(pets):
            dados = linha.strip().split(" | ")
            print(f"{i+1} - {dados[0]}")

        indice = int(input("\nDigite o número do pet: ")) - 1
        if 0 <= indice < len(pets):
            nomePet = pets[indice].strip().split(" | ")[0]
            meta = input("Descreva a meta (ex: Levar ao veterinário a cada 6 meses): ")
            arquivo_metas = open("Metas.txt", "a")
            arquivo_metas.write(f"{nomePet}: {meta}\n")
            arquivo_metas.close()
            print("Meta adicionada!")
        else:
            print("Pet inválido.")
    except Exception as e:
        print("Erro ao adicionar meta:", e)

def listar_metas():
    print("\nLISTA DE METAS")
    try:
        arquivo = open("Metas.txt", "r")
        metas = arquivo.readlines()
        arquivo.close()

        if not metas:
            print("Não há metas cadastradas.")
        for i, meta in enumerate(metas):
            print(f"{i+1} -> {meta.strip()}")
    except FileNotFoundError:
        print("Arquivo de metas não encontrado.")
    except Exception as e:
        print("Erro ao listar metas:", e)

def concluir_metas():
    global metas_concluidas 

    listar_metas()
    try:
        with open("Metas.txt", "r") as arquivo:
            metas = arquivo.readlines()

        if not metas:
            print("\nNão é possível marcar metas como concluídas, pois não há metas cadastradas.\n")
            return

        indice = int(input("\nDigite o número da meta que você deseja marcar como concluída: ")) - 1

        if 0 <= indice < len(metas):
            meta_concluida = metas[indice].strip()
            metas_concluidas.append(meta_concluida)

            del metas[indice]

            with open("Metas.txt", "w") as arquivo:
                arquivo.writelines(metas)

            print("Meta marcada como concluída!")
        else:
            print("Meta inexistente")
    except Exception as e:
        print("Erro ao marcar meta como concluída:", e)

def sugestoes_cuidados():
    print("\nSUGESTÕES DE CUIDADOS")
    try:
        arquivo = open("Cadastro.txt", "r")
        pets = arquivo.readlines()
        arquivo.close()

        if not pets:
            print("Não há pets cadastrados.")
            return

        print("\nSugestões baseadas em espécie e idade aproximada:")

        for i, linha in enumerate(pets):
            dados = linha.strip().split(" | ")
            nome = dados[0]
            especie = dados[1]
            data_nasc = dados[3]

            try:
                dia_atual = 15
                mes_atual = 5
                ano_atual = 2025

                dia_nasc, mes_nasc, ano_nasc = map(int, data_nasc.split("/"))

                idade = ano_atual - ano_nasc
                if mes_nasc > mes_atual or (mes_nasc == mes_atual and dia_nasc > dia_atual):
                    idade -= 1 
            except:
                idade = -1  

            print(f"\nPet: {nome} ({especie})")

            if idade >= 0:
                print(f"Idade aproximada: {idade} anos")
            else:
                print("Idade: não pôde ser calculada")

            especie_lower = especie.lower()
            if especie_lower == "cachorro":
                if idade >= 0 and idade < 2:
                    print("- Recomendado: vacinas em dia, socialização e brinquedos para filhotes.")
                elif idade >= 2:
                    print("- Recomendado: passeios regulares, consultas veterinárias anuais e alimentação balanceada.")
                else:
                    print("- Cuidados gerais: alimentação saudável e atenção veterinária.")
            elif especie_lower == "gato":
                print("- Recomendado: arranhadores, locais altos para subir e higiene da caixa de areia.")
            else:
                print("- Espécie não reconhecida: siga recomendações gerais de cuidado e bem-estar.")
    except Exception as e:
        print("Erro ao gerar sugestões:", e)

def visao_geral_do_pet():
    try:
        with open("Cadastro.txt", "r") as arq_cadastro:
            pets = arq_cadastro.readlines()

        if not pets:
            print("Não há pets cadastrados.")
            return

        print("\nEscolha o pet para visualizar a visão geral:")
        for i, linha in enumerate(pets):
            dados = linha.strip().split(" | ")
            print(f"{i + 1} -> Nome: {dados[0]} | Espécie: {dados[1]} | Raça: {dados[2]}")

        indice = int(input("\nDigite o número do pet: ")) - 1

        if not (0 <= indice < len(pets)):
            print("Número inválido.")
            return

        nome_pet = pets[indice].strip().split(" | ")[0]

        print(f"\n==== Visão Geral de {nome_pet} ====")

        print("\n--- Eventos ---")
        try:
            with open("Eventos.txt", "r") as arq_eventos:
                eventos = arq_eventos.readlines()
                eventos_filtrados = [ev for ev in eventos if ev.lower().startswith(nome_pet.lower() + ":")]
                if eventos_filtrados:
                    for ev in eventos_filtrados:
                        print("- " + ev.strip())
                else:
                    print("Nenhum evento encontrado para este pet.")
        except FileNotFoundError:
            print("Arquivo de eventos não encontrado.")

        print("\n--- Metas ---")
        try:
            with open("Metas.txt", "r") as arq_metas:
                metas = arq_metas.readlines()
                metas_filtradas = [meta for meta in metas if meta.lower().startswith(nome_pet.lower() + ":")]
                if metas_filtradas:
                    for meta in metas_filtradas:
                        print("- " + meta.strip())
                else:
                    print("Nenhuma meta a fazer para este pet.")
        except FileNotFoundError:
            print("Arquivo de metas não encontrado.")

        print("\n--- Metas Concluídas ---")
        metas_pet_concluidas = [meta for meta in metas_concluidas if meta.lower().startswith(nome_pet.lower() + ":")]
        if metas_pet_concluidas:
            for meta in metas_pet_concluidas:
                print("✅ Metas concluídas: \n" + meta)
        else:
            print("Nenhuma meta concluída para este pet.")
    except Exception as e:
        print("Erro ao gerar Visão geral:", e)

menu()
