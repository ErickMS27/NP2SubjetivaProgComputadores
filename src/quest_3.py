import pandas as pd

file_path = 'C:/Users/Erick/git/NP2SubjetivaProgComputadores/src/docs/alunos.csv'

data = pd.read_csv(file_path, sep=';')

print("Colunas disponíveis no arquivo CSV:")
print(data.columns)

colunas_np1 = [coluna for coluna in data.columns if "np1" in coluna.lower()]

if not colunas_np1:
    raise ValueError("Nenhuma coluna contendo 'NP1' foi encontrada no arquivo CSV. Verifique os dados.")

data['Media_NP1'] = data[colunas_np1].apply(pd.to_numeric, errors='coerce').mean(axis=1)

melhor_aluno = data.loc[data['Media_NP1'].idxmax()]

print(f"O melhor aluno, com a maior média em NP1, é:")
print(melhor_aluno[['Nome', 'Media_NP1']])

output_file = 'quest_3_erick.csv'
data.to_csv(output_file, index=False, sep=';')

print(f"Arquivo salvo como {output_file}")
