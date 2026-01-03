import pandas as pd 


dados = {
    'Anos': [1872, 1890, 1940, 1950, 1960, 1980, 1991, 2000],
    'Branca (%)': [58.0, 44.0, 35.8, 37.5, 38.2, 44.8, 47.5, 44.7],
    'Negra (%)': [38.1, 47.0, 63.5, 61.7, 61.1, 54.2, 51.6, 53.7]
}

# Cabeçalho formatado (ajustado para os novos nomes das chaves)
print(f"{'Ano':^6} | {'Branca (%)':^12} | {'Negra (%)':^12}")
print("-" * 36)

# Percorrendo os dados
for i in range(len(dados['Anos'])):
    ano = dados['Anos'][i]
    branca = dados['Branca (%)'][i]
    negra = dados['Negra (%)'][i]
    
    # Exibe os dados centralizados e com 1 casa decimal
    print(f"{ano:^6} | {branca:^12.1f} | {negra:^12.1f}")
    
    df = pd.DataFrame(dados)
    
    html_tabela = df.to_html(index=False, classes='tabela-populacao')