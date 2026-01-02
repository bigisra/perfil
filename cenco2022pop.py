import pandas as pd
import webbrowser
import os

# 1. Carregar o arquivo
try:
    df = pd.read_excel('pop2022.xlsx')

    # 2. Gerar o HTML com estilo básico para ficar bonito
    # Adicionamos um pouco de CSS para a tabela ocupar a tela e ter bordas limpas
       
    html_tabela = df.to_html(index=False)
    html_final = html_tabela

    # 3. Salvar o arquivo temporariamente
    nome_arquivo = "visualizacao_direta.html"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(html_final)

    # 4. ABRIR DIRETO NA PÁGINA (Navegador)
    caminho_absoluto = os.path.abspath(nome_arquivo)
    webbrowser.open(f'file://{caminho_absoluto}')

    print("O navegador foi aberto com os dados da planilha!")

except FileNotFoundError:
    print("Erro: O arquivo 'pop2022.xlsx' não foi encontrado.")
except Exception as e:
    print(f"Erro: {e}")