from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ARRAY, JSON
from app.db.database import Base
class Skills(Base):
    __tablename__= 'skills'
    id= Column(Integer, primary_key=True)
    job_title= Column(String)
    skills_extracted= Column(ARRAY(JSON), nullable=True) 