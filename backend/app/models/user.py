from backend.app.db.database import Base
from sqlalchemy import Column, DateTime, String, Enum, Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
import uuid
from datetime import datetime
from sqlalchemy.sql import func
import enum
class UserRole(str,enum.Enum):
    MNAGER= "ADMIN"
    USER="USER"

class User(Base):
    __tablename__= "Users"
    id = Column(UNIQUEIDENTIFIER, index= True, primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable= False)
    hashedPassword = Column(String)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    created_at = Column(DateTime, default= datetime.now)
    updated_at = Column(DateTime,default= func.now(), onupdate= func.now())

