

import pandas as pd
import numpy as np


# from anuidades_posfixadas import calcular_anuididade_vitalicia_posfixada
# Leitura da base de dados e criação da tabela feminina e masculina
BREMS_F = pd.read_excel(
    'C:\\Users\\CAIXAFILIAL\\Documents\\Raphael\\ciencias atuariais\\DDA0006 - MATEMÁTICA ATUARIAL I\\Tabua_mortalidade_BREMS_2021.xlsx', sheet_name="BREMS_mt_2021_f")
# BREMS_M = pd.read_excel(
#     'C:\\Users\\CAIXAFILIAL\\Documents\\Raphael\\ciencias atuariais\\DDA0006 - MATEMÁTICA ATUARIAL I\\Tabua_mortalidade_BREMS_2021.xlsx', sheet_name="BREMS_mt_2021_m")


# Calculando as colunas l e p
########## tabua feminina #################
for i in range(len(BREMS_F)):
    if BREMS_F.loc[i, 'x'] == 0:
        BREMS_F.loc[i, 'l_BREMS'] = 100000
    elif BREMS_F.loc[i, 'x'] != 0:
        BREMS_F.loc[i, 'l_BREMS'] = BREMS_F.loc[i-1, 'l_BREMS'] - \
            (BREMS_F.loc[i-1, 'l_BREMS']*BREMS_F.loc[i-1, 'q'])

for i in range(0, 113):
    BREMS_F.loc[i, 'p_BREMS'] = BREMS_F.loc[i +
                                            1, 'l_BREMS']/BREMS_F.loc[i, 'l_BREMS']

BREMS_F.rename(columns={'q': 'q_BREMS'}, inplace=True)

# print((BREMS_F.head()))
# print('____________________________')
# print()
# ########## tabua masculina #################
# for i in range(len(BREMS_M)):
#     if BREMS_M.loc[i, 'x'] == 0:
#         BREMS_M.loc[i, 'l_BREMS'] = 100000
#     elif BREMS_M.loc[i, 'x'] != 0:
#         BREMS_M.loc[i, 'l_BREMS'] = BREMS_M.loc[i-1, 'l_BREMS'] - \
#             (BREMS_M.loc[i-1, 'l_BREMS']*BREMS_M.loc[i-1, 'q'])

# for i in range(0, 113):
#     BREMS_M.loc[i, 'p_BREMS'] = BREMS_M.loc[i +
#                                             1, 'l_BREMS']/BREMS_M.loc[i, 'l_BREMS']

# BREMS_M.rename(columns={'q': 'q_BREMS'}, inplace=True)
# print((BREMS_M.head()))


##################################################################################
####################### Funções de Anuidades #####################################


def anuidade_temporaria_antecipada(bf, idade, n, taxa_juros, tabela_mortalidade):
    # Crie uma lista de valores de k de 0 a n-1
    k_valores = list(range(n))

    # Crie um DataFrame para armazenar os valores
    Calculo = pd.DataFrame({'k': k_valores})

    # Calcule VP usando a fórmula VP = bf * (1 / (1 + tx))^k
    Calculo['VP'] = bf * (1 / (1 + taxa_juros)) ** Calculo['k']

    # Inicialize listas vazias para as idades x e kPx
    idades = []
    kPx_valores = []

    # Calcule idades e kPx para cada valor de k
    for k in k_valores:
        idade_k = idade + k  # Idade x + k
        idades.append(idade_k)

        # Calcule o valor de kPx com base na tabela de mortalidade
        if idade_k >= 0 and idade_k <= 112:
            lx = tabela_mortalidade.loc[tabela_mortalidade['x']
                                        == idade_k, 'l_BREMS'].values[0]
            if k == 0:
                kPx = lx / lx  # Primeiro valor é lx/lx
            else:
                lx_k = tabela_mortalidade.loc[tabela_mortalidade['x']
                                              == idade_k + k, 'l_BREMS'].values[0]
                kPx = lx_k / lx  # Use lx_k / lx
        else:
            kPx = 0  # Defina um valor padrão para idades fora do intervalo da tabela
        kPx_valores.append(kPx)

    # Adicione as listas de idades e kPx ao DataFrame
    Calculo['x'] = idades
    Calculo['kPx'] = kPx_valores

    # Calcule äx:nꓶ como a soma dos produtos de VP e kPx
    Calculo['äx:nꓶ'] = Calculo['VP'] * Calculo['kPx']

    # Calcule o valor final da anuidade somando todos os termos
    Valor_anuidade = Calculo['äx:nꓶ'].sum()

    # Formate o valor final da anuidade com 5 casas decimais
    Valor_anuidade_formatado = round(Valor_anuidade, 3)

    print(
        f"O valor da anuidade ä_{idade}:{n}ꓶ é: R$ {Valor_anuidade_formatado}")


def anuidade_vitalicia_antecipada(bf, idade, taxa_juros, tabela_mortalidade):
    idade_maxima = 112
    k_maximo = idade_maxima - idade

    FUNCAO_DESCONTO = 1 / (1 + taxa_juros)
    anuidade = 0

    for k in range(k_maximo + 1):
        idade_k = idade + k

        # Verifique se a idade está no intervalo da tabela de mortalidade
        if idade_k >= 0 and idade_k <= 112 and 'l_BREMS' in tabela_mortalidade.columns:
            if k == 0:
                lx = tabela_mortalidade.loc[tabela_mortalidade['x']
                                            == idade_k, 'l_BREMS'].values
                if len(lx) > 0:
                    lx = lx[0]
                else:
                    lx = 0
                kPx = lx / lx  # Primeiro valor é lx/lx
            else:
                lx_k = tabela_mortalidade.loc[tabela_mortalidade['x']
                                              == idade_k + k, 'l_BREMS'].values
                if len(lx_k) > 0:
                    lx_k = lx_k[0]
                else:
                    lx_k = 0
                kPx = lx_k / lx  # Use lx_k / lx
        else:
            kPx = 0  # Defina um valor padrão para idades fora do intervalo da tabela

        VP = (FUNCAO_DESCONTO ** k) * kPx
        anuidade += VP

    # Formate o valor final da anuidade com 5 casas decimais
    valor_anuidade = round(anuidade, 3)

    print(f"O valor da anuidade vitalícia antecipada é: R$ {valor_anuidade}")


def anuidade_temporaria_postecipada(bf, idade, n, taxa_juros, tabela_mortalidade):
    k_valores = list(range(1, n + 1))
    Calculo = pd.DataFrame({'k': k_valores})
    # Calcule VP usando a fórmula VP = bf * (1 / (1 + tx))^k
    Calculo['VP'] = bf * (1 / (1 + taxa_juros)) ** Calculo['k']

    # Calcule VP usando a fórmula VP = bf * (1 / (1 + tx))^k
    Calculo['VP'] = bf * (1 / (1 + taxa_juros)) ** Calculo['k']

    # Inicialize listas vazias para as idades x e kPx
    idades = []
    kPx_valores = []

    # Calcule idades e kPx para cada valor de k
    for k in k_valores:
        idade_k = idade + k  # Idade x + k
        idades.append(idade_k)

        # Calcule o valor de kPx com base na tabela de mortalidade
        if idade_k >= 0 and idade_k <= 112:
            lx = tabela_mortalidade.loc[tabela_mortalidade['x']
                                        == idade_k, 'l_BREMS'].values[0]
            if k == 0:
                kPx = lx / lx  # Primeiro valor é lx/lx
            else:
                lx_k = tabela_mortalidade.loc[tabela_mortalidade['x']
                                              == idade_k + k, 'l_BREMS'].values[0]
                kPx = lx_k / lx  # Use lx_k / lx
        else:
            kPx = 0  # Defina um valor padrão para idades fora do intervalo da tabela
        kPx_valores.append(kPx)

    # Adicione as listas de idades e kPx ao DataFrame
    Calculo['x'] = idades
    Calculo['kPx'] = kPx_valores

    # Calcule äx:nꓶ como a soma dos produtos de VP e kPx
    Calculo['äx:nꓶ'] = Calculo['VP'] * Calculo['kPx']

    # Calcule o valor final da anuidade somando todos os termos
    Valor_anuidade = Calculo['äx:nꓶ'].sum()

    # Formate o valor final da anuidade com 5 casas decimais
    Valor_anuidade_formatado = round(Valor_anuidade, 3)

    print(
        f"O valor da anuidade a_{idade}:{n}ꓶ é: R$ {Valor_anuidade_formatado}")


##################################################################################
####################### Calculo das Anuidades ####################################
# Insira os parametros:
# Anuidade temporararia antecipada n anos
bf = 1  # Benefício
idade = 60  # Idade do participante
n = 5  # Tempo do seguro
taxa_juros = 0.05  # Taxa de juros
tabela_mortalidade = BREMS_F  # Substitua pelo caminho do seu arquivo

anuidade_temporaria_antecipada(
    bf, idade, n, taxa_juros, tabela_mortalidade)

# Anuidade vitalicia antecipada
idade = 60  # Idade do participante
taxa_juros = 0.05  # Taxa de juros
tabela_mortalidade = BREMS_F  # Substitua pelo caminho do seu arquivo

anuidade_vitalicia_antecipada(bf, idade, taxa_juros, tabela_mortalidade)


# Anuidade temporararia postecipada n anos
bf = 1  # Benefício
idade = 60  # Idade do participante
n = 5  # Tempo do seguro
taxa_juros = 0.05  # Taxa de juros
tabela_mortalidade = BREMS_F  # Substitua pelo caminho do seu arquivo

anuidade_temporaria_postecipada(
    bf, idade, n, taxa_juros, tabela_mortalidade)
