from pydantic import BaseModel
from pydantic import EmailStr

class CreateUser(BaseModel):
    email : EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    role: str

class SigninUser(BaseModel):
    email: EmailStr
    password: str