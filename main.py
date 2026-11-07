from fastapi import FastAPI

app = FastAPI(title="API Exercício AST12")


@app.get("/")
def read_root():
    return {"mensagem": "API rodando com sucesso!"}


@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    # Parte 1 e Estado Final Correto: a + b
    # (Para a Parte 2, você alterará temporariamente para: a - b)
    return {"resultado": a + b}


@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    # Criado na Parte 3
    return {"resultado": a * b}