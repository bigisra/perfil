from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def exibir_tabela():
    # URL do seu arquivo (certifique-se de que é um link de download direto)
    url = 'https://fatecspgov-my.sharepoint.com/:x:/r/personal/israel_barros_fatec_sp_gov_br/Documents/Tabela_04_Pop_resid_por_cor_ou_raca_e_pessoas_indigenas_2022_MU%201.xlsx?d=w148d9f6dafa44030a4837d49af6f9a67&csf=1&web=1&e=F89oDK'
    
    try:
        # Lê o arquivo Excel
        df = pd.read_excel(url)
        
        # Converte o DataFrame para uma tabela HTML formatada
        tabela_html = df.head().to_html(classes='table table-striped', index=False)
        
        # Retorna uma página simples com a tabela
        return render_template_string('''
            <html>
                <head>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
                </head>
                <body class="container mt-5">
                    <h2>Estrutura da Tabela:</h2>
                    {{ tabela | safe }}
                </body>
            </html>
        ''', tabela=tabela_html)
        
    except Exception as e:
        return f"Erro ao carregar os dados: {e}"

if __name__ == '__main__':
    app.run(debug=True)