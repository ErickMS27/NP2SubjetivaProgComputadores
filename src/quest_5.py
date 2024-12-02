import pandas as pd

file_path = 'C:/Users/Erick/git/NP2SubjetivaProgComputadores/src/docs/alunos.csv'

data = pd.read_csv(file_path, sep=';')

print("Colunas disponíveis no arquivo CSV:")
print(data.columns)

if 'Media' not in data.columns:
    raise ValueError("A coluna 'Media' não foi encontrada no arquivo CSV. Verifique os dados.")

data['Soma_Medias'] = data.groupby('Nome')['Media'].transform('sum')

aluno_maior_soma = data.loc[data['Soma_Medias'].idxmax()]

data.loc[data['Soma_Medias'].idxmax(), 'Nome'] = aluno_maior_soma['Nome'] + " (Maior Soma de Médias)"

data = data.drop(columns=['Soma_Medias'])

output_file = 'quest_5_erick.csv'
data.to_csv(output_file, index=False)

print(f"Aluno com maior soma de médias: {aluno_maior_soma['Nome']}")
print(f"Arquivo salvo como {output_file}")
