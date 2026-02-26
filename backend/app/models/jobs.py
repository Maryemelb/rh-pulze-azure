


from backend.app.db.database import Base
from sqlalchemy import Column, String,Integer,Float
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
import uuid

class Jobs(Base):
    __tablename__="jobs"
    id = Column(UNIQUEIDENTIFIER, index= True, primary_key=True, default=uuid.uuid4)
    index=Column(Integer, nullable= False)
    job_title=Column(String, nullable= False),
    description=Column(String, nullable= True),
    salary_estimate= Column(String, nullable= False)
    job_description= Column(String, nullable= False)
    rating= Column(Float, nullable= False)
    company_name= Column(String, nullable= False)
    location= Column(String, nullable= False)
    headquarters= Column(String, nullable= False)
    size= Column(String, nullable= False)
    founded= Column(String, nullable= False)
    type_of_ownership= Column(String, nullable= False)
    industry= Column(String, nullable= False)
    sector= Column(String, nullable= False)
    revenue= Column(String, nullable= False)
    competitors= Column(String, nullable= False)
