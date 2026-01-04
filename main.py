from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API rodando"}

@app.get("/tabela")
def tabela():
    return {
        "Anos": [1872, 1890, 1940, 1950, 1960, 1980, 1991, 2000],
        "Branca (%)": [58.0, 44.0, 35.8, 37.5, 38.2, 44.8, 47.5, 44.7],
        "Negra (%)": [38.1, 47.0, 63.5, 61.7, 61.1, 54.2, 51.6, 53.7]
    }
    df = pd.DataFrame(dados)

    tabela_html = df.to_html(
        index=False,
        border=1,
        classes="tabela"
    )

    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial;
                padding: 20px;
            }}
            table {{
                border-collapse: collapse;
                width: 60%;
            }}
            th {{
                background-color: #f2f2f2;
                padding: 8px;
            }}
            td {{
                padding: 8px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <h2>Distribuição da população por raça (%)</h2>
        {tabela_html}
    </body>
    </html>
    """

    return html
