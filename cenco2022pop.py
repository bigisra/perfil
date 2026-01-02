import pandas as pd

# Nota: Links do SharePoint/OneDrive costumam exigir permissão ou 
# um link de "download direto" para funcionarem via código.
url = 'https://fatecspgov-my.sharepoint.com/:x:/r/personal/israel_barros_fatec_sp_gov_br/Documents/Tabela_04_Pop_resid_por_cor_ou_raca_e_pessoas_indigenas_2022_MU%201.xlsx?d=w148d9f6dafa44030a4837d49af6f9a67&csf=1&web=1&e=hGwImo'

# Alterado de read_csv para read_excel
# Você pode precisar instalar a biblioteca openpyxl: pip install openpyxl
df = pd.read_excel(url)


# Comando para exibir
print("Estrutura da Tabela:")
print(df.head())