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

def formatar_nome(nome):
    partes = str(nome).split()
    if len(partes) > 1:
        sobrenome = partes[-1].capitalize()
        restante = " ".join([p.capitalize() for p in partes[:-1]])
        return f"{sobrenome}, {restante}"
    return str(nome).capitalize()

nomes_formatados = data[coluna_nomes].apply(formatar_nome)

output_file = 'quest_1_erick.csv'
nomes_formatados.to_csv(output_file, index=False, header=["Nome_Formatado"])

print(f"Arquivo salvo como {output_file}")
