# Para selecionar uma coluna específica utilizamos o método "df["c"]" e como parâmetro o nome da coluna.
# (df aqui representa o nome do DataFrame e c representa o nome da coluna)
# Para filtrar linhas baseada em uma condição específica, basta fazer uma expressão do tipo "df["c"]> x"
# (x aqui representa um valor qualquer).

import pandas as pd

df = pd.read_csv("Employee.csv")
print(df["JoiningYear"] > 2015)
