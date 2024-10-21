from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, modelo, estrutura, database

app = FastAPI()

modelo.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"Bem vindo ao meu API - Fernanda morais"}

@app.post("/alunos/", response_model=estrutura.Aluno)
def create_aluno(aluno: estrutura.AlunoCreate, db: Session = Depends(database.get_db)):
    return crud.create_aluno(db=db, aluno=aluno)

@app.get("/alunos/{aluno_id}", response_model=estrutura.Aluno)
def read_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    db_aluno = crud.get_aluno(db, aluno_id=aluno_id)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    return db_aluno

@app.get("/alunos/", response_model=list[estrutura.Aluno])
def read_alunos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    alunos = crud.get_alunos(db, skip=skip, limit=limit)
    return alunos

@app.put("/alunos/{aluno_id}", response_model=estrutura.Aluno)
def update_aluno(aluno_id: int, aluno: estrutura.AlunoCreate, db: Session = Depends(database.get_db)):
    return crud.update_aluno(db, aluno_id=aluno_id, aluno=aluno)

@app.delete("/alunos/{aluno_id}", response_model=estrutura.Aluno)
def delete_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_aluno(db, aluno_id=aluno_id)
