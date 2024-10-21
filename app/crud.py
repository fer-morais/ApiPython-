from sqlalchemy.orm import Session
from . import modelo, estrutura

def get_aluno(db: Session, aluno_id: int):
    return db.query(modelo.Aluno).filter(modelo.Aluno.id == aluno_id).first()

def get_alunos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(modelo.Aluno).offset(skip).limit(limit).all()

def create_aluno(db: Session, aluno: estrutura.AlunoCreate):
    db_aluno = modelo.Aluno(**aluno.dict())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def update_aluno(db: Session, aluno_id: int, aluno: estrutura.AlunoCreate):
    db_aluno = db.query(modelo.Aluno).filter(modelo.Aluno.id == aluno_id).first()
    for key, value in aluno.dict().items():
        setattr(db_aluno, key, value)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def delete_aluno(db: Session, aluno_id: int):
    db_aluno = db.query(modelo.Aluno).filter(modelo.Aluno.id == aluno_id).first()
    db.delete(db_aluno)
    db.commit()
    return db_aluno
