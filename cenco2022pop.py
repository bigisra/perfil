import pandas as pd

# 1. Cole aqui o link que você copiou do "Compartilhar"
url_compartilhada = "https://fatecspgov-my.sharepoint.com/:x:/r/personal/israel_barros_fatec_sp_gov_br/Documents/Tabela_04_Pop_resid_por_cor_ou_raca_e_pessoas_indigenas_2022_MU%201.xlsx?d=w148d9f6dafa44030a4837d49af6f9a67&csf=1&web=1&e=jmz5F0"

# 2. Ajuste para download direto (funciona para a maioria dos links de OneDrive/SharePoint)
url_direta = url_compartilhada.replace("view.aspx", "download.aspx").replace("?guestaccess", "?download=1&guestaccess")

try:
    # 3. Ler a tabela diretamente da web
    print("Acessando tabela...")
    df = pd.read_excel(url_direta)

    # 4. Fazer a tabela aparecer formatada
    print("\n--- TABELA CARREGADA ---")
    print(df.head(20)) # Mostra as primeiras 20 linhas
    print(f"\nTotal de registros: {len(df)}")

except Exception as e:
    print(f"Erro: Certifique-se de que o link é público. Detalhes: {e}")