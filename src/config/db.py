# Script para criar conexão com banco de dados, criando o banco e as tabelas se eles não exisisrem

from sqlalchemy.orm import sessionmaker # Para criar sessão com o banco de dados
from sqlalchemy import create_engine # Para criar conexão com o banco de dados
from src.models.Base import Base # Classe base para criar as tabelas
from src.models.Position import Position 

# Cria conexão com o banco de dados db.db
engine = create_engine('sqlite:///db.db')

# Cria sessão com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Cria o banco de dados e as tabelas se eles não existirem
Base.metadata.create_all(engine)