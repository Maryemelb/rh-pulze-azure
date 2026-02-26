
from fastapi import APIRouter, Depends, Response

from backend.app.schemas.user_schema import SigninUser
from backend.app.services.authService import login
from backend.app.db.dependencies import getdb

router=APIRouter(
    prefix="/health",
    tags=["health"]
)

@router.post('/')
async def health(user: SigninUser, response:Response,db= Depends(getdb)):
    return 'succesfully '