"""
PRECISO:  ̅
PEGAR A TABELA DE MORTALIDADE PARA CALCULAR O Lx E O PX
    IMPORTAR PANDAS E NUMPY PARA LER ARQUIVO
    ARMAZENAR EM 2 VARIAVEIS, UM PARA 'MASC' OUTRA PARA 'F', SENDO QUE AS DUAS TABELAS ESTAO EM UM MESMO ARQUIVO, SEPARADO POR ABA EM PLANILHAS DISTINTAS    
    CRIAR AS COLUNAS COM OS VALORES DE 'L'
        PARA O 'L' CONSIDERAR O L0 INICIAL COMO 100000, e OS SEGUINTES LX = LX-1*(LX-1*QX)
        PX = LX+1/LX
         
formulas
V = 1/(1+i)
kPx = lx/lx+k
        FINANCEIRA:
        anuidade financeira antecipada = änꓶ = (1-V^n)/(1-V) 
        anuidade financeira postecipada = anꓶ = Vz(1-V^n)/(1-V) 
ATUARIAL:
ANUIDADE VITALICIA ANTECIPADA:
äx = ∑(k=0 a ∞) (V^k)*kPx 
ANUIDADE VITALICIA POSTECIPADA:
ax = ∑(k=1 a ∞) (V^k)*kPx 
ANUIDADE TEMPORARIA ANTECIPADA POR "n" ANOS:
äx:nꓶ = ∑(k=0 a n-1) (V^k)*kPx
ANUIDADE TEMPORARIA POSTECIPADA POR "n" ANOS:
ax:nꓶ = ∑(k=1 a n) (V^k)*kPx
ANUIDADE VITALICIA ANTECIPADA DIFERIDA POR 'm' ANOS:
m|äx = ∑(k=m a ∞) (V^k)*kPx  ou m|äx = a(x+m)*(V^m)*mPx
ANUIDADE VITALICIA POSTECIPADA DIFERIDA POR 'm' ANOS:
m|ax = ∑(k=m+1 a ∞) (V^k)*kPx  ou m|äx = a(x+m)*(V^m)*mPx
ANUIDADE VITALICIA ANTECIPADA COM "n" PAGAMENTOS CERTOS(soma de n anuidades financeiras com o somatorio da anuidade atuarial)
äx̅:n̅ꓶ = änꓶ + ∑(k=n a ∞) (V^k)*kPx 
ANUIDADE VITALICIA POSTECIPADA COM "n" PAGAMENTOS CERTOS(soma de n anuidades financeiras com o somatorio da anuidade atuarial)
ax̅:n̅ꓶ = anꓶ + ∑(k=(n+1) a ∞) (V^k)*kPx 
"""


import pandas as pd
import numpy as np

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

print((BREMS_F.head()))
print('____________________________')
print()

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

# SUPORTE
# Defina os parâmetros
# bf = 1  # Benefício
# idade = 60  # Idade  x do participante
# n = 5  # Tempo do seguro
# taxa_juros = 0.05  # Taxa de juros

# # Crie uma lista de valores de k de 0 a n-1
# k_valores = list(range(n))

# # Crie um DataFrame para armazenar os valores
# Calculo = pd.DataFrame({'k': k_valores})

# # Calcule VP usando a fórmula VP = bf * (1 / (1 + tx))^k
# Calculo['VP'] = bf * (1 / (1 + taxa_juros)) ** Calculo['k']

# # Inicialize listas vazias para as idades x e kPx
# idades = []
# kPx_valores = []

# # Calcule idades e kPx para cada valor de k
# for k in k_valores:
#     idade_k = idade + k  # Idade x + k
#     idades.append(idade_k)

#     # Calcule o valor de kPx com base na tabela de mortalidade feminina (BREMS_F no exemplo)
#     if idade_k >= 0 and idade_k <= 112:
#         lx = BREMS_F.loc[BREMS_F['x'] == idade_k, 'l_BREMS'].values[0]
#         if k == 0:
#             kPx = lx / lx  # Primeiro valor é lx/lx
#         else:
#             lx_k = BREMS_F.loc[BREMS_F['x'] ==
#                                idade_k + k, 'l_BREMS'].values[0]
#             kPx = lx_k / lx  # Use lx_k / lx
#     else:
#         kPx = 0  # Defina um valor padrão para idades fora do intervalo da tabela
#     kPx_valores.append(kPx)

# # Adicione as listas de idades e kPx ao DataFrame
# Calculo['x'] = idades
# Calculo['kPx'] = kPx_valores

# # Calcule äx:nꓶ como a soma dos produtos de VP e kPx
# Calculo['äx:nꓶ'] = Calculo['VP'] * Calculo['kPx']

# # Calcule o valor final da anuidade somando todos os termos
# Valor_anuidade = Calculo['äx:nꓶ'].sum()

# # Formate o valor final da anuidade com 5 casas decimais
# Valor_anuidade_formatado = round(Valor_anuidade, 5)

# print(
#     f"O valor da anuidade para n = {n}, com taxa de juros de {taxa_juros} é: {Valor_anuidade_formatado:.5f}")

# # Exiba o DataFrame com os resultados
# print(Calculo)


def calcular_anuidade(bf, idade, n, taxa_juros, tabela_mortalidade):
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
    Valor_anuidade_formatado = round(Valor_anuidade, 2)

    print(f"O valor da anuidade é: R$ {Valor_anuidade_formatado}")


# Exemplo de uso da função
bf = 1  # Benefício
idade = 60  # Idade do participante
n = 5  # Tempo do seguro
taxa_juros = 0.05  # Taxa de juros
tabela_mortalidade = BREMS_F  # Substitua pelo caminho do seu arquivo


calcular_anuidade(
    bf, idade, n, taxa_juros, tabela_mortalidade)


def calcular_anuidade_vitalicia_antecipada(bf, idade, taxa_juros, tabela_mortalidade):
    idade_maxima = 112
    k_maximo = idade_maxima - idade

    V = 1 / (1 + taxa_juros)
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

        VP = (V ** k) * kPx
        anuidade += VP

    # Formate o valor final da anuidade com 5 casas decimais
    valor_anuidade = round(anuidade, 5)

    return valor_anuidade


# Exemplo de uso da função
bf = 100000  # Benefício
idade = 60  # Idade do participante
taxa_juros = 0.05  # Taxa de juros
tabela_mortalidade = BREMS_F  # Substitua pelo caminho do seu arquivo

valor_anuidade = calcular_anuidade_vitalicia_antecipada(
    bf, idade, taxa_juros, tabela_mortalidade)
print(f"O valor da anuidade vitalícia antecipada é: {valor_anuidade:.5f}")
