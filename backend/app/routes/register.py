from fastapi import APIRouter, Depends

from backend.app.schemas.user_schema import CreateUser
from backend.app.services.authService import create_new_user
from backend.app.db.dependencies import getdb

router=APIRouter(
    prefix="/Auth",
    tags=["Auth"]
)


@router.post('/register')
async def register(user: CreateUser, db= Depends(getdb)):
    await create_new_user(db, user)
    return 'user created'
