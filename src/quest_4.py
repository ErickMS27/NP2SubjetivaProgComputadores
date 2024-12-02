import pandas as pd

file_path = 'C:/Users/Erick/git/NP2SubjetivaProgComputadores/src/docs/alunos.csv'

data = pd.read_csv(file_path, sep=';')

print("Colunas disponíveis no arquivo CSV:")
print(data.columns)

if 'Media' not in data.columns:
    raise ValueError("A coluna 'Media' não foi encontrada no arquivo CSV. Verifique os dados.")

media_disciplinas = data.groupby('Disciplina')['Media'].mean()

melhor_disciplina = media_disciplinas.idxmax()
melhor_rendimento = media_disciplinas.max()

print(f"A disciplina com o melhor rendimento, com a maior média, é da disciplina: {melhor_disciplina} com média {melhor_rendimento:.2f}")

output_file = 'quest_4_erick.csv'
media_disciplinas.to_csv(output_file, header=True)

print(f"Arquivo salvo como {output_file}")
