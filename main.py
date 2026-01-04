from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# PERMITE o HTML acessar o Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, defina o domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dados")
def dados():
    return {
        "nome": "Israel",
        "area": "Dados",
        "status": "Funcionando"
    }
