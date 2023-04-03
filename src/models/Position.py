from models.Base import Base # Classe base para criar as tabelas
from sqlalchemy import Column, Integer, Float # Para criar as colunas da tabela

# Classe que representa a tabela de jogos
class Position(Base):

    # Nome da tabela
    __tablename__ = 'positions'

    # Colunas da tabela
    id = Column(Integer, primary_key=True) # Chave primária
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    r = Column(Float)
    j1 = Column(Float)
    j2 = Column(Float)
    j3 = Column(Float)
    j4 = Column(Float)
    
    # Função que retorna uma representação em string do objeto, com preço em formato brasileiro
    def __repr__(self):
        return f'Position(id={self.id}, x={self.x}, y={self.y}, z={self.z}, r={self.r}, j1={self.j1}, j2={self.j2}, j3={self.j3}, j4={self.j4})'
    
    # Função que retorna um dicionário com os dados do objeto
    def return_json(self):
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'r': self.r,
            'j1': self.j1,
            'j2': self.j2,
            'j3': self.j3,
            'j4': self.j4
        }