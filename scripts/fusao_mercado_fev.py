# Importação
from processamento_dados import Dados

# Caminhos
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'

# Extract
dados_empresaA = Dados(path_json, 'json')
print(f'Nome das colunas a empresa A: {dados_empresaA.nome_colunas}')
print(f'Quantidade de linhas da empresa A: {dados_empresaA.qtd_linhas}\n')

dados_empresaB = Dados(path_csv, 'csv')
print(f'Nome das colunas a empresa B: {dados_empresaB.nome_colunas}')
print(f'Quantidade de linhas da empresa B: {dados_empresaB.qtd_linhas}\n')

# Tranform
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(f'Nome das colunas da empresa B atualizado: {dados_empresaB.nome_colunas}\n')

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f'Nome das colunas das duas empresas juntas: {dados_fusao.nome_colunas}')
print(f'Nova quantidade de linhas: {dados_fusao.qtd_linhas}')

# Load
dados_fusao.salvando_dados(path_dados_combinados)
print(f'Caminho dos dados salvos: {path_dados_combinados}')