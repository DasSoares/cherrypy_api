from sqlalchemy.sql import text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
# from sqlalchemy.pool import NullPool
from .dbconfig import USERNAME, PASSWORD, IP_ADDRESS, DATABASE


def create_session():
    engine = create_engine(
        f'mysql+pymysql://{USERNAME}:{PASSWORD}@{IP_ADDRESS}/{DATABASE}', #DATABASE?charset=latin1
        future=True,
        #poolclass=NullPool
    )
    return scoped_session(sessionmaker(bind=engine))

class ConnectDB:
    def __init__(self, session=None):
        self.session = session if session else create_session()

    def execute(self, stmt):
        return self.session.execute(stmt)

    def _execute(self, sql, params):
        stmt = text(sql)
        return self.session.execute(stmt, params)

    def _execute_no_param(self, sql):
        stmt = text(sql)
        return self.session.execute(stmt)

    def commit(self):
        self.session.commit()

    def close_session(self):
        self.session.close()
    
    def _session_rollback(self):
        self.session.rollback()

        