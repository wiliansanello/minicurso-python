from Model.base import Base
from sqlalchemy import Column, Integer, String

class Livro(Base):
    __tablename__ = "livro"

    isbn = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    ano = Column(Integer)

    def __repr__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"