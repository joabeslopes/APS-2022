import pandas as pd

# Ler a tabela inteira
medicamentos = pd.read_csv('medicamentos.csv', delimiter =';', encoding='latin-1')

# Gerar nova tabela filtrada
novaTab = medicamentos[['COMERCIALIZAÇÃO 2022','PRODUTO','APRESENTAÇÃO','LABORATÓRIO','PF Sem Impostos','PF 20%','PMC 0%','PMC 20%']]


# Definir o lucro dos laboratórios e das farmácias, baseado no comércio à população
lucroLabs = []
lucroFarms= []

for i in range(novaTab.shape[0]):
    if novaTab['COMERCIALIZAÇÃO 2022'].loc[i] == 'Sim':
        lucroLabs.append(float(novaTab['PF 20%'].loc[i]) - float(novaTab['PF Sem Impostos'].loc[i]))
        lucroFarms.append(float(novaTab['PMC 20%'].loc[i]) - float(novaTab['PMC 0%'].loc[i]))
    else:
        lucroLabs.append(float(novaTab['PF 20%'].loc[i]) - float(novaTab['PF Sem Impostos'].loc[i]))
        lucroFarms.append(0)

# Colocar os resultados em novas colunas na tabela
novaTab.loc[:,'LUCRO LABORATÓRIOS'] = lucroLabs
novaTab.loc[:,'LUCRO FARMÁCIAS'] = lucroFarms

