

from http.client import HTTPException
from fastapi import Response
from requests import Session
from backend.app.schemas.user_schema import CreateUser, SigninUser, UserResponse
from backend.app.models.user import User
import uuid
from passlib.context import CryptContext
import jwt
import os
from dotenv import load_dotenv

load_dotenv()


context= CryptContext(schemes=["argon2"],deprecated='auto')

async def create_new_user(db: Session, user: CreateUser):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_password= hash_password(user.password)
    new_user= User(
        id= uuid.uuid4(),
        name= user.name,
        email= user.email,
        hashedPassword= hashed_password

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(
        id= str(new_user.id),
        email= new_user.email,
        is_verified= new_user.is_verified,
        is_active=new_user.is_active,
        role= new_user.role
    )

async def login(db:Session, user: SigninUser, response:Response):
    user_db=get_user_by_email(db, user.email)

    if not user_db :
        raise HTTPException(status_code=400, detail='Invalid Email or Password')
    
    if not verify_password(user.password, user_db.hashedPassword):
        raise HTTPException(status_code=400, detail='Invalid Email or Password')
    
    token= create_token(user_db.email, user_db.role)
    #set token in the coockies
    response.set_cookie(key='token', value=token)
    return 'succesfully logged in'


def get_user_by_email(db:Session, email: str):
    return db.query(User).filter(User.email == email).first()


def hash_password(password:str):
    return context.hash(password)


def create_token(email:str, role:str):
    payload= {
        'email': email,
         'role': role
    }
    return jwt.encode(payload=payload, key=os.getenv('jwt_secret_key'), algorithm=os.getenv('algorithm'))


def decode_token(token:str):
    return 'decoded'


def verify_password(inserted_password:str, hashed_password:str):
    return context.verify(inserted_password,hashed_password)