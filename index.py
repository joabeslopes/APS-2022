import pandas as pd

# Ler a tabela inteira
medicamentos = pd.read_csv('medicamentos.csv', delimiter =';', encoding='latin-1',decimal=',')

# Gerar nova tabela filtrada
novaTab = medicamentos[['COMERCIALIZAÇÃO 2022','PRODUTO','APRESENTAÇÃO','LABORATÓRIO','PF Sem Impostos','PF 20%','PMC 0%','PMC 20%']]


# Definir o lucro dos laboratórios e das farmácias, baseado no comércio à população
lucroLabs = []
lucroFarms= []
margemTotalLabs=0
margemTotalFarms=0
contSim = 0
for i in range(novaTab.shape[0]):
    if novaTab['COMERCIALIZAÇÃO 2022'].loc[i] == 'Sim':
        lucroLabs.append(float(novaTab['PF 20%'].loc[i]) - float(novaTab['PF Sem Impostos'].loc[i]))
        lucroFarms.append(float(novaTab['PMC 20%'].loc[i]) - float(novaTab['PMC 0%'].loc[i]))
        contSim += 1

    else:
        lucroLabs.append(float(novaTab['PF 20%'].loc[i]) - float(novaTab['PF Sem Impostos'].loc[i]))
        lucroFarms.append(0)
    # Calcula as margens de lucro geral, filtrando o que não for número
    if lucroLabs[i]>=0:
        margemTotalLabs += lucroLabs[i]
    if lucroFarms[i]>=0:
        margemTotalFarms += lucroFarms[i]

# Colocar os resultados em novas colunas na tabela
novaTab.loc[:,'LUCRO LABORATÓRIOS'] = lucroLabs
novaTab.loc[:,'LUCRO FARMÁCIAS'] = lucroFarms

# Calcular proporção
comercial = round((contSim / novaTab.shape[0]) * 100)

# Gerar o resultado final
novaTab.to_csv('NovaTabela.csv')
print('=='*30)
print('Tabela reduzida foi gerada com sucesso!\n')
print(f'Margem de lucro total permitida aos laboratórios pelos produtos: R$ {margemTotalLabs:.2f}\n')
print(f'Margem de lucro total permitida às farmácias pelos produtos: R$ {margemTotalFarms:.2f}\n')
print(f'Proporção de produtos comercializáveis ao público geral: {comercial}%\n')
print('=='*30)