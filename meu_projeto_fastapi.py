from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Gerenciador de Tarefas")

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

@app.get("/")
def read_root():
    return {"message": "API rodando com sucesso!"}

@app.post("/tasks")
def create_task(task: Task):
    return {"status": "Tarefa criada", "data": task}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("meu_projeto_fastapi:app", host="127.0.0.1", port=8000, reload=True)