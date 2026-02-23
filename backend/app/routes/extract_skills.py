
from fastapi import APIRouter, Depends, Response

from backend.app.schemas.user_schema import SigninUser
from backend.app.services.authService import login
from backend.app.db.dependencies import getdb
from backend.test_zure_model import run_ner_extraction

router=APIRouter(
    prefix="/extract_skills",
    tags=["skills"]
)

@router.post('/')
async def signin(user: SigninUser, response:Response,db= Depends(getdb)):
     await   run_ner_extraction("backend/app/data/cleaned_jobs.csv", "backend/app/data/dataset_with_skills.csv", limit=5)
     return 'succesfully'