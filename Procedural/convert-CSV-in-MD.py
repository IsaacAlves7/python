import pandas as pd

# Caminho para o arquivo CSV
file_path = r"C:\Users\jamal\Downloads\adjetivos_ingles.csv"

try:
    # Ler o arquivo CSV com especificação de encoding
    df = pd.read_csv(file_path, encoding='utf-8')

    # Substituir os símbolos Unicode pelos símbolos correspondentes
    df['Phoneme'] = df['Phoneme'].str.replace('\u02c8', 'ˈ')
    df['Phoneme'] = df['Phoneme'].str.replace('\u025b', 'ɛ')

    # Converter para formato de tabela Markdown
    markdown_table = df.to_markdown(index=False)

    # Exibir a tabela Markdown
    print(markdown_table)
except FileNotFoundError:
    print(f"O arquivo em {file_path} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
