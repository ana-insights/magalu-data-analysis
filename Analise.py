# libs para análise grafica
import pandas as pd
import matplotlib.pyplot as plt

# libs para modelagem e matrizes
import numpy as np
import seaborn as sns
import plotly.graph_objects as go

# lib para ignorar avisos
import warnings
warnings.filterwarnings('ignore')

Base_Dados = pd.read_excel('Vase_004 - Magalu - Sem Resolução.xlsx')

# verificando os dados
print(Base_Dados.head())
print(Base_Dados.tail())

# verificando a dimensão
print(Base_Dados.shape)

print(Base_Dados.info())

print(Base_Dados.describe())

# Series Temporais
Dados = Base_Dados.set_index('Data')

plt.figure(figsize=(16, 5))
plt.style.use('Solarize_Light2')
plt.title('Análise das ações da magalu - Fechamento', fontsize=15, loc='left')
plt.plot(Dados.index, Dados['Fechamento'])
plt.xlabel('Período da Cotação')
plt.ylabel('Valor da Ação (R$)')
plt.show()


# Calculando médias móveis de curto (5 dias) e longo prazo (30 dias)
Media_Movel = Dados['Fechamento'].rolling(5).mean()
Media_Tendencia = Dados['Fechamento'].rolling(30).mean()

plt.figure(figsize=(16, 5))
plt.style.use('Solarize_Light2')
plt.title('Análise das ações da magalu - Fechamento', fontsize=15, loc='left')
plt.plot(Dados.index, Dados['Fechamento'])
plt.plot(Dados.index, Media_Movel)
plt.plot(Dados.index, Media_Tendencia)
plt.xlabel('Período da Cotação')
plt.ylabel('Valor da Ação (R$)')
plt.show()

sns.boxenplot(data=Dados, x='Fechamento')
plt.show()

# Boxplot Mensal

Base_Dados['Mes'] = Base_Dados['Data'].dt.month
plt.figure(figsize=(16, 5))
sns.boxplot(data=Base_Dados, x='Mes', y='Fechamento', palette='Set2')
plt.show()

print(Base_Dados.groupby(['Mes']).describe()['Fechamento'])

Grafico = go.Figure(
    data=[
        go.Candlestick(
            x=Dados.index,
            open=Dados['Abertura'],
            high=Dados['Maior'],
            low=Dados['Menor'],
            close=Dados['Fechamento']
        )
    ]
)
Grafico.update_layout(xaxis_rangeslider_visible=False)
Grafico.show()
