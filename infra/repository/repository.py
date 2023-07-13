from infra.configs.connection import DBConnectionHandler
from infra.entities import apostas
from infra.entities.apostas import Aposta


class ApostaRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Aposta).all()
            return data

    def insert(self, aposta):
        with DBConnectionHandler() as db:
            try:
                db.session.add(aposta)
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e