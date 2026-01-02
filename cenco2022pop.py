import pandas as pd

# Exemplo com um arquivo CSV online
url = 'https://fatecspgov-my.sharepoint.com/:x:/r/personal/israel_barros_fatec_sp_gov_br/Documents/Tabela_04_Pop_resid_por_cor_ou_raca_e_pessoas_indigenas_2022_MU%201.xlsx?d=w148d9f6dafa44030a4837d49af6f9a67&csf=1&web=1&e=9R8tUR'
df = pd.read_csv(url)

# Se for um arquivo Excel:
# url_excel = 'URL_DO_SEU_ARQUIVO.xlsx'
# df = pd.read_excel(url_excel)

# Se for uma tabela HTML em uma página web (retorna uma lista de DataFrames, você pode selecionar a desejada):
# url_html = 'URL_DA_PAGINA_WEB'
# tables = pd.read_html(url_html)
# df = tables[0] # Seleciona a primeira tabela encontrada



