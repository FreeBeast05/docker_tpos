import pandas as pd
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class HomeTable(declarative_base()):
    __tablename__ = 'hometable'
    word = sql.Column(sql.String, primary_key=True)
    number = sql.Column(sql.Integer)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
       
class PostgresConfiguration:
    POSTGRES_USER = "postgres"
    POSTGRES_DB_PASSWORD = "postgres"
    POSTGRES_DB_HOST = "db"
    POSTGRES_DB_NAME = "postgres"
    POSTGRES_DB_PORT = "5432"
    
    @property
    def postgres_db_path(self):
        return f'postgres://{self.POSTGRES_USER}:{self.POSTGRES_DB_PASSWORD}@' \
               f'{self.POSTGRES_DB_HOST}:' \
               f'{self.POSTGRES_DB_PORT}/{self.POSTGRES_DB_NAME}'
                  
pg = PostgresConfiguration()
engine = sql.create_engine(pg.postgres_db_path)
Session = sessionmaker(bind=engine)
session = Session()

data = pd.read_csv("data/data.csv",header=None, names=['word', 'number'])
data.to_sql('hometable', engine, if_exists='replace')
print("Recorded csv to table in postgre........")

ready_table = session.query(HomeTable).all()
if ready_table:
    print("================ DATA =================")
    for text in ready_table:
        print(text.word, text.number)
    print("=========================== Data is exist ===========================")
else:
    print("Error: data not loaded")
