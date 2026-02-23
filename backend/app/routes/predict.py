
from fastapi import APIRouter, Depends, Response

from backend.app.schemas.user_schema import SigninUser
from backend.app.services.authService import login
from backend.app.db.dependencies import getdb

router=APIRouter(
    prefix="/predict-salary",
    tags=["predict-salary"]
)

@router.post('/')
async def signin(user: SigninUser, response:Response,db= Depends(getdb)):
    await login(db,user, response)
    return 'succesfully'