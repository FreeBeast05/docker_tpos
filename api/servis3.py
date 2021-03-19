import os
import json 
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse 
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify, abort, request, make_response, url_for
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
app = FastAPI()

pg = PostgresConfiguration()
engine = create_engine(pg.postgres_db_path)

Session = sessionmaker(bind=engine)
session = Session()

from starlette.exceptions import HTTPException as StarletteHTTPException
@app.exception_handler(StarletteHTTPException)
def custom_http_exception_handler(request, exc):
    return JSONResponse({"Error:404": "Wrong request address"})

@app.get('/')
def get_all_items():
    ready_table = session.query(HomeTable).all()
    return [ix.as_dict() for ix in ready_table]
@app.get('/health')
def heath():
    return 200

