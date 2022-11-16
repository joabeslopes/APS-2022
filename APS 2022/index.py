import pandas as pd

tabela = pd.read_csv('APS 2022/medicamentos.csv', delimiter =';', encoding='latin-1')

print(tabela.head(9))
