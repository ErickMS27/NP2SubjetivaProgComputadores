import pandas as pd

file_path = 'C:/Users/Erick/git/NP2SubjetivaProgComputadores/src/docs/alunos.csv'

data = pd.read_csv(file_path)

print("Colunas disponíveis no arquivo CSV:")
print(data.columns)

coluna_nomes = None
for coluna in data.columns:
    if "nome" in coluna.lower():
        coluna_nomes = coluna
        break

if coluna_nomes is None:
    raise ValueError("Nenhuma coluna contendo 'nome' foi encontrada no arquivo CSV. Verifique os dados.")

print(f"Coluna identificada como nomes: {coluna_nomes}")

data_ordenada = data.sort_values(by=coluna_nomes, ascending=True)

output_file = 'quest_2_erick.csv'
data_ordenada.to_csv(output_file, index=False)

print(f"Arquivo salvo como {output_file}")
print(f"Todos os registros da coluna '{coluna_nomes}' ordenados:")
print(data_ordenada[coluna_nomes].to_string(index=False)) 