from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Float

class Aposta(Base):
    __tablename__ = 'aposta'

    id_aposta = Column(Integer, autoincrement=True, primary_key=True)
    nome_apostador = Column(String(100), nullable=False)
    valor_aposta = Column(Float, nullable=False)
    vencedor = Column(String(100), nullable=True)
    placar = Column(String(100), nullable=False)
    premio= Column(Float, nullable=False)

    def __repr__(self):
        return f'Aposta = {self.id_aposta}, Apostador = {self.nome_apostador}, Valor da Aposta = {self.valor_aposta}, Vencedor = {self.vencedor}, Placar = {self.placar}, Prêmio = {self.premio}'