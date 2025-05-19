CRUD de animais

README

Esse projeto é um sistema em Python para gerenciar informações de pets, como cadastro, edição, eventos, metas e sugestões de cuidados. Os dados são salvos em arquivos .txt.

- Estrutura de Arquivos Utilizados

	•	Cadastro.txt: Armazena os dados dos pets cadastrados.

	•	Eventos.txt: Registra os eventos vinculados aos pets (vacinas, consultas, medicamentos).

	•	Metas.txt: Contém metas a serem realizadas para os pets.

	•	Lista interna metas_concluidas: Guarda as metas marcadas como concluídas durante a execução do programa.


Funcionalidades Disponíveis

- Menu Principal (menu())

Apresenta as opções principais:

1- Adicionar pet 

2- Listar pets

3- Editar pet

4- Excluir pet 

5- Menu de eventos

6- Menu de metas

7- Sugestões e cuidados

8- Visão geral do pet

0- Voltar ao menu principal

- Pets

1. Adicionar pet

Coleta nome, espécie, raça, data de nascimento e peso do pet. Grava em Cadastro.txt.

2. Listar pets

Exibe todos os pets cadastrados com seus dados básicos.

3. Editar pet

Permite editar os dados de um pet existente, selecionado por número.

4. Excluir pet

Remove o pet do Cadastro.txt e também apaga os eventos e metas associadas. Remove metas concluídas do mesmo pet.

- Eventos (menu_eventos())

1. Adicionar evento

Vincula um evento (vacina, consulta ou medicamento) a um pet. Grava em Eventos.txt.

2. Listar eventos

Mostra todos os eventos registrados.

3. Excluir evento

Permite excluir eventos específicos por número da lista.

- Metas (menu_metas())

1. Adicionar meta

Associa uma meta (ex: “levar ao veterinário”) a um pet. Grava em Metas.txt.

2. Listar metas

Exibe todas as metas registradas.

3. Concluir meta

Marca uma meta como concluída. A meta é armazenada na lista metas_concluidas, mas não é removida do arquivo.

- Sugestões e Cuidados (sugestoes_cuidados())

Oferece recomendações de cuidados com base na espécie e idade estimada dos pets.

- Para cachorros, sugestões variam com a idade.
 
 - Para gatos, são dadas recomendações gerais.
  
 - Outras espécies recebem orientações genéricas.


Visão Geral do Pet (visao_geral_do_pet())

Mostra um resumo completo de um pet específico, incluindo:

- Eventos registrados
- Metas associadas
- Metas concluídas 

Requisitos

- Python 3.x
- Sistema de arquivos com permissão de leitura/escrita
