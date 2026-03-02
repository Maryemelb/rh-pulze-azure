
from fastapi import APIRouter, Depends, Response

from backend.app.models.user import User
from backend.app.schemas.job_schema import JobCreate
from backend.app.schemas.user_schema import SigninUser
from backend.app.services.authService import get_current_user, login
from backend.app.db.dependencies import getdb
from backend.app.services.extract_skills_service import extract_skills_for_one_job
from backend.app.services.jobService import addjob, getJobs
router=APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.post('/')
async def addjobs(job: JobCreate,db= Depends(getdb),current_user: User= Depends(get_current_user)):
    await addjob(db,job)
    return {'response':'succesfully', 'job':job}

@router.get('/')
async def getjobs(db= Depends(getdb),current_user: User= Depends(get_current_user)):
    jobs =await getJobs(db)
    return jobs