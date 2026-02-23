from fastapi import FastAPI

from sqlalchemy_utils import create_database, database_exists
from backend.app.db.database import Base, engine, sessionLocal


app= FastAPI()

if not database_exists(engine.url):
  try:
    create_database(engine.url)
    Base.metadata.create_all(bind=engine)
  except:
    print('database creation did not succeed')
else:
    try:
       Base.metadata.create_all(bind=engine)
    except:
       print('failed')


