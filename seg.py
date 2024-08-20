import streamlit as st
import pandas as pd
from collections import Counter

# Inicializa a lista de cursos, a lista de profissionais, a lista de Bravos e os treinamentos no session_state se ainda não existir
if 'cursos' not in st.session_state:
    st.session_state['cursos'] = [
        {'nome': 'Regulamento', 'numero_pessoas': 10},
        {'nome': 'Sistema Operacional do CB - Tática', 'numero_pessoas': 10},
        {'nome': 'Equipamentos de Sapa/Arrombamento/Maca', 'numero_pessoas': 8},
        {'nome': 'Montagem de Linha Simples e Composta', 'numero_pessoas': 7},
        {'nome': 'Teoria do Fogo I', 'numero_pessoas': 10},
        {'nome': 'Teoria do Fogo II', 'numero_pessoas': 10},
        {'nome': 'Proteção Respiratória I', 'numero_pessoas': 10},
        {'nome': 'Proteção Respiratória II', 'numero_pessoas': 10},
        {'nome': 'Proteção Respiratória III', 'numero_pessoas': 10},
        {'nome': 'Identificação de Risco Químico I', 'numero_pessoas': 10},
        {'nome': 'Identificação de Risco Químico II', 'numero_pessoas': 10},
        {'nome': 'Identificação de Risco Químico III', 'numero_pessoas': 10},
        {'nome': 'Rádio Comunicações', 'numero_pessoas': 10},
        {'nome': 'Leão (Tripulação/Saída)', 'numero_pessoas': 7},
        {'nome': 'Anatomia /Fraturas', 'numero_pessoas': 10},
        {'nome': 'Gavião(Tripulação/Saída)', 'numero_pessoas': 7},
        {'nome': 'Queimaduras/Hemorragias', 'numero_pessoas': 10},
        {'nome': 'Puma (Tripulação/Saída)', 'numero_pessoas': 4},
        {'nome': 'Transporte de Vítimas/ RCP', 'numero_pessoas': 10},
        {'nome': 'Técnicas de Locomoção no Escuro', 'numero_pessoas': 6},
        {'nome': 'Animais Peçonhentos', 'numero_pessoas': 10},
        {'nome': 'Roupas Especiais', 'numero_pessoas': 6},
        {'nome': 'Moto Bomba Brun', 'numero_pessoas': 7},
        {'nome': 'Treinamento na Pista com Extintores', 'numero_pessoas': 7},
        {'nome': 'Escada Mecânica', 'numero_pessoas': 4},
        {'nome': 'Treinamento na Pista c/Mangueiras', 'numero_pessoas': 7},
        {'nome': 'Corte Oxi-Acetileno', 'numero_pessoas': 4},
        {'nome': 'Espuma Mecânica', 'numero_pessoas': 4},
        {'nome': 'Escada Extensível/cordas', 'numero_pessoas': 4},
        {'nome': 'Contenção de vazamento', 'numero_pessoas': 4},
        {'nome': 'Resgate em Altura', 'numero_pessoas': 4},
        {'nome': 'Remoção de Vítimas em Recinto Fechado', 'numero_pessoas': 4},
        {'nome': 'Casa de Fumaça (Nível a definir)', 'numero_pessoas': 8},
        {'nome': 'Oficina de Autônomos/ Inspeção de equipamentos', 'numero_pessoas': 4},
        {'nome': 'Exercício de Emergência', 'numero_pessoas': 0},  # todos
        {'nome': 'Avaliações teóricas e práticas', 'numero_pessoas': 0}  # todos
    ]

if 'profissionais' not in st.session_state:
    st.session_state['profissionais'] = []

if 'cursos_selecionados' not in st.session_state:
    st.session_state['cursos_selecionados'] = []

if 'bravos' not in st.session_state:
    st.session_state['bravos'] =[
    {'nome': 'Luiz Antônio Neri', 'numero': 37, 'curso': ''},
    {'nome': 'Alexander Braga', 'numero': 39, 'curso': ''},
    {'nome': 'José Ricardo', 'numero': 38, 'curso': ''},
    {'nome': 'João Vitor', 'numero': 40, 'curso': ''},
    {'nome': 'Sandro da Conceição', 'numero': 42, 'curso': ''},
    {'nome': 'Clerio Lino', 'numero': 44, 'curso': ''},
    {'nome': 'José Carlos Batista', 'numero': 43, 'curso': ''},
    {'nome': 'Benedito Francisco', 'numero': 62, 'curso': ''},
    {'nome': 'Roniere Mendelson', 'numero': 27, 'curso': ''},
    {'nome': 'Diego Souza', 'numero': 53, 'curso': ''},
    {'nome': 'Élson Sidnei', 'numero': 63, 'curso': ''},
    {'nome': 'José Paulo Ramos', 'numero': 28, 'curso': ''},
    {'nome': 'David Lucas', 'numero': 61, 'curso': ''},
    {'nome': 'Caio Valente', 'numero': 22, 'curso': ''},
    {'nome': 'André Luiz Honostório', 'numero': 66, 'curso': ''},
    {'nome': 'Lilian Nunes', 'numero': 29, 'curso': ''},
    {'nome': 'Romulo Martins', 'numero': 64, 'curso': ''},
    {'nome': 'Thiago da Silva', 'numero': 23, 'curso': ''},
    {'nome': 'Evandro Reis', 'numero': 67, 'curso': ''},
    {'nome': 'Cosme da Silva', 'numero': 30, 'curso': ''},
    {'nome': 'Charlon Vagner', 'numero': 65, 'curso': ''},
    {'nome': 'Marcos André', 'numero': 25, 'curso': ''},
    {'nome': 'André Vilanova', 'numero': 72, 'curso': ''},
    {'nome': 'Vladimir Santos', 'numero': 32, 'curso': ''},
    {'nome': 'Carlos Eduardo Delgado', 'numero': 68, 'curso': ''},
    {'nome': 'Maisa Santos', 'numero': 26, 'curso': ''},
    {'nome': 'Rafael Maurílio', 'numero': 77, 'curso': ''},
    {'nome': 'Luis Fernando', 'numero': 33, 'curso': ''},
    {'nome': 'Claudemir Riehl', 'numero': 69, 'curso': ''},
    {'nome': 'Rafael Ribeiro Leal', 'numero': 31, 'curso': ''},
    {'nome': 'Daniel Castelo', 'numero': 78, 'curso': ''},
    {'nome': 'Douglas Coelho', 'numero': 34, 'curso': ''},
    {'nome': 'João Vitor Oliveira', 'numero': 71, 'curso': ''},
    {'nome': 'Aron Honório', 'numero': 36, 'curso': ''},
    {'nome': 'Douglas Cavalcanti', 'numero': 35, 'curso': ''},
    {'nome': 'Douglas Luiz', 'numero': 70, 'curso':'' }
]

if 'treinamentos' not in st.session_state:
    st.session_state['treinamentos'] = []


# Função para exibir o formulário de cadastro de pessoas
def exibir_formulario():
    st.title("Cadastro de Pessoas")

    nome = st.text_input("Nome")
    email = st.text_input("Email")
    tipo = st.radio("Tipo de Pessoa", ["Bravo", "Treinador"])

    if tipo == "Bravo":
        numero = st.number_input("Número", min_value=1, step=1)
        multiselect_cursos = []
    else:
        cursos_disponiveis = [curso['nome'] for curso in st.session_state['cursos']]

        # Multiselectbox para escolher cursos cadastrados
        multiselect_cursos = st.multiselect("Cursos", cursos_disponiveis,
                                            default=st.session_state['cursos_selecionados'])

        # Botão para adicionar todos os cursos
        if st.button("Adicionar todos os cursos"):
            st.session_state['cursos_selecionados'] = cursos_disponiveis
            st.experimental_rerun()  # Atualiza a página para refletir as mudanças

    if st.button("Cadastrar"):
        if not nome or not email or (tipo == "Treinador" and not st.session_state['cursos_selecionados']) or (tipo == "Bravo" and not numero):
            st.error("Preencha todos os campos antes de finalizar o cadastro")
        else:
            profissional = {
                'nome': nome,
                'email': email,
                'tipo': tipo,
                'cursos': st.session_state['cursos_selecionados'] if tipo == "Treinador" else []
            }

            if tipo == "Bravo":
                st.session_state['bravos'].append({'nome': nome, 'numero': numero})

            st.session_state['profissionais'].append(profissional)
            st.success(f"{tipo} {nome} cadastrado com sucesso! Cursos: {', '.join(st.session_state['cursos_selecionados']) if tipo == 'Treinador' else 'Nenhum curso vinculado'}")


# Função para exibir o formulário de cadastro de cursos
def exibir_formulario_curso():
    st.title("Cadastro de Cursos")

    nome_curso = st.text_input("Nome do Curso")
    numero_pessoas = st.number_input("Número de Pessoas por Curso", min_value=1, step=1)

    if st.button("Cadastrar Curso"):
        if not nome_curso or not numero_pessoas:
            st.error("Preencha todos os campos antes de finalizar o cadastro do curso")
        else:
            st.session_state['cursos'].append({'nome': nome_curso, 'numero_pessoas': numero_pessoas})
            st.success(f"Curso {nome_curso} cadastrado com sucesso!")

import streamlit as st
import pandas as pd
from collections import Counter

def contar_ocorrencias_cursos(bravos_presentes, cursos_disponiveis):
    contagem = Counter()
    for bravo_nome in bravos_presentes:
        for bravo in st.session_state['bravos']:
            if bravo['nome'] == bravo_nome:
                cursos = bravo['curso'].split(', ')
                for curso in cursos:
                    if curso in cursos_disponiveis:
                        contagem[curso] += 1
    return contagem

def criar_treinamento():
    st.title("Criação de Treinamento")

    # Atualiza o estado da sessão com a lista de profissionais
    if 'profissionais' not in st.session_state:
        st.session_state['profissionais'] = []

    # Campo para selecionar os treinadores presentes
    nomes_profissionais = [prof['nome'] for prof in st.session_state['profissionais']]
    treinadores_presentes = st.multiselect("Selecione os Treinadores Presentes", nomes_profissionais)

    # Campo para selecionar os Bravos presentes
    if 'bravos' not in st.session_state:
        st.session_state['bravos'] = []
    nomes_bravos = [bravo['nome'] for bravo in st.session_state['bravos']]
    bravos_presentes = st.multiselect("Selecione os Bravos Presentes", nomes_bravos)

    # Campo para selecionar a data do treinamento
    data_treinamento = st.date_input("Selecione a Data do Treinamento", value=pd.to_datetime("today"))

    # Atualiza o número de pessoas presentes de acordo com os Bravos selecionados
    num_pessoas_presentes = len(bravos_presentes)
    st.write(f"Número de Pessoas Presentes: {num_pessoas_presentes}")

    if treinadores_presentes:
        # Filtra os cursos disponíveis de acordo com os treinadores presentes
        cursos_disponiveis = []
        for treinador in treinadores_presentes:
            profissional = next(prof for prof in st.session_state['profissionais'] if prof['nome'] == treinador)
            cursos_disponiveis.extend(profissional['cursos'])

        # Remove duplicatas
        cursos_disponiveis = list(set(cursos_disponiveis))

        # Filtra os cursos disponíveis com base na capacidade em relação ao número de pessoas presentes
        if 'cursos' not in st.session_state:
            st.session_state['cursos'] = []
        cursos_disponiveis_capacidade = [
            curso['nome'] for curso in st.session_state['cursos']
            if curso['nome'] in cursos_disponiveis and curso['numero_pessoas'] >= num_pessoas_presentes
        ]

        # Calcular a popularidade de cada curso
        contagem_cursos = contar_ocorrencias_cursos(bravos_presentes, cursos_disponiveis_capacidade)

        # Filtrar os cursos por capacidade e experiência do treinador
        cursos_filtrados = [curso for curso in cursos_disponiveis_capacidade if
                           any(curso in prof['cursos'] for prof in st.session_state['profissionais'] if prof['nome'] in treinadores_presentes)]

        # Calcular a popularidade dos cursos não presentes na lista de cursos dos profissionais
        cursos_nao_presentes = set(cursos_disponiveis_capacidade) - set(cursos_filtrados)
        for curso in cursos_nao_presentes:
            contagem_cursos[curso] = 0  # Atribui 0 para os cursos não presentes

        # Ordenar os cursos por popularidade (ascendente) e capacidade (descendente)
        cursos_ordenados = sorted(cursos_disponiveis_capacidade, key=lambda x: (contagem_cursos[x], -next(curso['numero_pessoas'] for curso in st.session_state['cursos'] if curso['nome'] == x)))

        # Multiselect para escolher o primeiro grupo de cursos
        cursos_selecionados_1 = st.multiselect("Selecione o Primeiro Grupo de Cursos (os menos populares aparecem primeiro)", cursos_ordenados)

        if cursos_selecionados_1:
            # Pergunta sobre a duração do curso
            duracao_curso = st.radio("O Curso se estenderá por quanto tempo?", ["2 horas", "4 horas"])

            # Exclui os cursos já selecionados do segundo multiselect
            cursos_disponiveis_excluidos = [curso for curso in cursos_ordenados if curso not in cursos_selecionados_1]

            # Multiselect para escolher o segundo grupo de cursos
            cursos_selecionados_2 = st.multiselect("Insira o Segundo Grupo de Cursos", cursos_disponiveis_excluidos)

            if cursos_selecionados_2:
                # Adiciona o campo para selecionar o terceiro grupo de cursos
                cursos_disponiveis_excluidos_3 = [curso for curso in cursos_disponiveis_excluidos if curso not in cursos_selecionados_2]
                cursos_selecionados_3 = st.multiselect("Insira o Terceiro Grupo de Cursos", cursos_disponiveis_excluidos_3)

                if cursos_selecionados_3:
                    # Adiciona campos para selecionar treinadores para cada curso
                    st.write("Selecione o treinador para cada curso:")

                    treinadores = st.session_state['profissionais']
                    cursos_com_treinadores = {}

                    for curso in cursos_selecionados_1 + cursos_selecionados_2 + cursos_selecionados_3:
                        treinadores_disponiveis = [prof['nome'] for prof in treinadores if curso in prof['cursos']]
                        selecionado = st.selectbox(f"Treinador para o curso '{curso}'", treinadores_disponiveis, key=curso)
                        cursos_com_treinadores[curso] = selecionado

                    # Inicializa cursos_selecionados_4 como uma lista vazia
                    cursos_selecionados_4 = []

                    # Adiciona um curso adicional se o primeiro curso for de 2 horas
                    if duracao_curso == "2 horas":
                        cursos_disponiveis_excluidos_4 = [curso for curso in cursos_disponiveis_excluidos_3 if curso not in cursos_selecionados_3]
                        cursos_selecionados_4 = st.multiselect("Insira um Curso Adicional", cursos_disponiveis_excluidos_4)

                        if cursos_selecionados_4:
                            st.write("Selecione o treinador para o curso adicional:")
                            for curso in cursos_selecionados_4:
                                treinadores_disponiveis = [prof['nome'] for prof in treinadores if curso in prof['cursos']]
                                selecionado = st.selectbox(f"Treinador para o curso adicional '{curso}'", treinadores_disponiveis, key=f"adicional_{curso}")
                                cursos_com_treinadores[curso] = selecionado

            if st.button("Criar Treinamento"):
                if not treinadores_presentes:
                    st.error("Selecione pelo menos um treinador antes de criar o treinamento")
                else:
                    st.success(f"Treinamento criado com sucesso! Treinadores presentes: {', '.join(treinadores_presentes)}")

                    # Atualiza o campo curso dos bravos presentes
                    cursos_selecionados_total = (cursos_selecionados_1 + cursos_selecionados_2 + cursos_selecionados_3 + cursos_selecionados_4)
                    for bravo_nome in bravos_presentes:
                        for bravo in st.session_state['bravos']:
                            if bravo['nome'] == bravo_nome:
                                # Adiciona os cursos à lista existente, evitando duplicatas
                                bravo['curso'] = ', '.join(sorted(set(bravo['curso'].split(', ') + cursos_selecionados_total)))

                    # Cria a tabela com 4 colunas se a duração do curso for 2 horas
                    if duracao_curso == "2 horas":
                        cursos_selecionados_total = (
                                cursos_selecionados_1 + cursos_selecionados_2 + cursos_selecionados_3 + cursos_selecionados_4)[:4]
                        while len(cursos_selecionados_total) < 4:
                            cursos_selecionados_total.append("Nenhum")

                        df_detalhes = pd.DataFrame([cursos_selecionados_total],
                                                   columns=["Curso 1 - 8:00 até 10:00", "Curso 2 - 10:00 até 12:00",
                                                            "Curso 3 - 13:00 até 15:00", "Curso 4 - 15:00 até 17:00"])

                        treinadores_row = [cursos_com_treinadores.get(curso, 'Nenhum') for curso in cursos_selecionados_total]
                        df_detalhes.loc[1] = treinadores_row
                        df_detalhes.index = ['Cursos', 'Treinadores']

                        st.table(
                            df_detalhes.style.set_properties(**{'text-align': 'center'}).set_table_styles(
                                [{'selector': 'th',
                                  'props': [('text-align', 'center')]},
                                 {'selector': 'td',
                                  'props': [('padding', '10px')]}]))

                    elif duracao_curso == "4 horas":
                        # Cria a tabela com 3 colunas
                        cursos_selecionados_total_3_col = (
                                cursos_selecionados_1 + cursos_selecionados_2 + cursos_selecionados_3)[:3]
                        while len(cursos_selecionados_total_3_col) < 3:
                            cursos_selecionados_total_3_col.append("Nenhum")

                        df_detalhes_3_col = pd.DataFrame([cursos_selecionados_total_3_col],
                                                         columns=["Curso 1 - 8:00 até 12:00",
                                                                  "Curso 2 - 13:00 até 15:00",
                                                                  "Curso 3 - 15:00 até 17:00"])

                        treinadores_row_3_col = [cursos_com_treinadores.get(curso, 'Nenhum') for curso in
                                                 cursos_selecionados_total_3_col]
                        df_detalhes_3_col.loc[1] = treinadores_row_3_col
                        df_detalhes_3_col.index = ['Cursos', 'Treinadores']

                        st.write("**Tabela com 3 Cursos**")
                        st.table(
                            df_detalhes_3_col.style.set_properties(**{'text-align': 'center'}).set_table_styles(
                                [{'selector': 'th',
                                  'props': [('text-align', 'center')]},
                                 {'selector': 'td',
                                  'props': [('padding', '10px')]}]))

                    if st.button("Salvar Treinamento"):
                        if not treinadores_presentes:
                            st.error("Selecione pelo menos um treinador antes de criar o treinamento")
                        else:
                            st.success(f"Treinamento salvo com sucesso! Treinadores presentes: {', '.join(treinadores_presentes)}")

                            # Atualiza o campo curso dos bravos presentes
                            cursos_selecionados_total = (
                                        cursos_selecionados_1 + cursos_selecionados_2 + cursos_selecionados_3 + cursos_selecionados_4)
                            for bravo_nome in bravos_presentes:
                                for bravo in st.session_state['bravos']:
                                    if bravo['nome'] == bravo_nome:
                                        # Adiciona os cursos à lista existente, evitando duplicatas
                                        bravo['curso'] = list(set(bravo['curso'].split(', ') + cursos_selecionados_total))
def visualizar_bravos():
    st.title("Visualizar Bravos e Seus Cursos")

    if 'bravos' not in st.session_state:
        st.session_state['bravos'] = []

    if not st.session_state['bravos']:
        st.write("Nenhum Bravo registrado.")
        return

    # Cria uma lista de dicionários para a tabela
    dados_bravos = []
    for bravo in st.session_state['bravos']:
        dados_bravos.append({
            'Nome': bravo['nome'],
            'Cursos': ', '.join(bravo['curso'].split(', '))
        })

    # Converte a lista de dicionários em um DataFrame
    df_bravos = pd.DataFrame(dados_bravos)

    # Exibe a tabela com formatação melhorada
    st.write("**Lista de Bravos e seus Cursos**")
    st.table(df_bravos.style.set_properties(**{'text-align': 'left'})
                                 .set_table_styles(
                                     [{'selector': 'th',
                                       'props': [('text-align', 'center'),

                                                 ]},
                                      {'selector': 'td',
                                       'props': [('padding', '10px'),
                                                ]}]
                                 ))

def visualizar_cadastros():
    st.title("Visualizar Cadastros")

    st.subheader("Profissionais Cadastrados")
    df_profissionais = pd.DataFrame(st.session_state['profissionais'])
    st.dataframe(df_profissionais)

    st.subheader("Cursos Cadastrados")
    df_cursos = pd.DataFrame(st.session_state['cursos'])
    st.dataframe(df_cursos)

    st.subheader("Bravos Cadastrados")
    df_bravos = pd.DataFrame(st.session_state['bravos'])
    st.dataframe(df_bravos)

    st.subheader("Treinamentos Cadastrados")
    df_treinamentos = pd.DataFrame(st.session_state['treinamentos'])
    st.dataframe(df_treinamentos)


# Barra lateral para navegação entre as páginas
opcao = st.sidebar.selectbox("Escolha uma opção", [
    "Cadastro de Pessoas",
    "Cadastro de Cursos",
    "Criar Treinamento",
    "Visualizar bravos e cursos"
])

if opcao == "Cadastro de Pessoas":
    exibir_formulario()
elif opcao == "Cadastro de Cursos":
    exibir_formulario_curso()
elif opcao == "Criar Treinamento":
    criar_treinamento()
elif opcao == "Visualizar bravos e cursos":
    visualizar_bravos()
