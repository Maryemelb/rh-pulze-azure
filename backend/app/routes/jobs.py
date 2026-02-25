
from fastapi import APIRouter, Depends, Response

from backend.app.schemas.job_schema import JobCreate
from backend.app.schemas.user_schema import SigninUser
from backend.app.services.authService import login
from backend.app.db.dependencies import getdb

router=APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.post('/')
async def addjob(job: JobCreate, response:Response,db= Depends(getdb)):
    await addjob(db,job, response)
    return 'succesfully'

@router.get('/')
async def getjobs(user: SigninUser, response:Response,db= Depends(getdb)):
    message =await getjobs(db,user, response)
    return message