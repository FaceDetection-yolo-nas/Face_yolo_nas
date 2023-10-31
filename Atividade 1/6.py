# Para ler um arquivo CSV no Pandas, utilizamos o comando pandas.read_csv
# Já para mostrar as primeiras linhas, utilizamos o método "head()" com o parâmetro de linhas desejado
import pandas as pd

df = pd.read_csv("Employee.csv")
print(df.head(6))
