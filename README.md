#projeto

README

Arquivos utilizados
Cadastro.txt – Armazena os dados dos pets cadastrados.

Eventos.txt – Armazena os eventos vinculados a cada pet.

Metas.txt – Armazena metas definidas para cada pet.

Funcionalidades do Sistema

Menu Principal de Pets
Chamado pela função menu(). Exibe as opções abaixo:

css
Copiar
Editar
1 - Adicionar pet
2 - Listar pets
3 - Editar pet
4 - Excluir pet
5 - Menu eventos
6 - Menu de Metas
7 - Sugestões e Cuidados
8 - Linha do tempo
0 - Voltar ao Menu Principal

Descrição das Funções
1. adicionar()
Cadastra um novo pet no arquivo Cadastro.txt, solicitando:

Nome

Espécie

Raça

Data de nascimento

Peso

2. listar()
Exibe todos os pets cadastrados, lendo e formatando os dados do arquivo Cadastro.txt.

3. editar()
Permite alterar os dados de um pet já cadastrado. Substitui a linha correspondente no arquivo com os novos dados fornecidos.

4. excluir()
Remove um pet da lista, com base no número da lista exibida.

Menu de Eventos (menu_eventos())
Permite registrar eventos importantes para os pets, como vacinas ou consultas.

Subopções:
css
Copiar
Editar
1 - Adicionar evento
2 - Listar eventos
3 - Excluir eventos
0 - Voltar ao menu principal
1. add_evento()
Associa um evento a um pet específico. Tipos disponíveis:

Vacina

Consulta veterinária

Aplicação de medicamentos

Também permite adicionar observações opcionais.

2. listar_eventos()
Lista todos os eventos registrados em Eventos.txt.

3. excluir_eventos()
Permite remover um evento da lista com base em seu número na lista.

Menu de Metas (menu_metas())
Permite o gerenciamento de metas relacionadas ao cuidado com o pet.

Subopções:
css
Copiar
Editar
1 - Adicionar meta
2 - Listar metas
0 - Voltar ao menu principal
1. adicionar_meta()
Permite definir uma meta personalizada para um pet (exemplo: "Levar ao veterinário a cada 6 meses").

2. listar_metas()
Lista todas as metas registradas em Metas.txt.

sugestoes_cuidados()
Gera dicas personalizadas de cuidados com base na espécie e idade do pet. Calcula a idade aproximada com base na data de nascimento e faz recomendações específicas para cães e gatos.

linha_do_tempo_pet()
Gera uma linha do tempo completa para um pet, reunindo:

Todos os eventos registrados

Todas as metas definidas

Ajuda o tutor a visualizar o histórico de cuidados com o animal.

Requisitos para a execução 

- Python (versão 3 ou acima)
- ⁠Editor de texto ou terminal para execução do script
- ⁠Arquivos .txt criados automaticamente após a execução
