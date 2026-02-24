
from fastapi import APIRouter, Depends, Response

from backend.app.schemas.user_schema import SigninUser
from backend.app.services.authService import login
from backend.app.db.dependencies import getdb
from backend.app.services.predict import predict_salary
from backend.app.schemas.job_schema import JobCreate
import pandas as pd

router=APIRouter(
    prefix="/predict-salary",
    tags=["predict-salary"]
)
#, response:Response,db= Depends(getdb)
@router.post('/')
async def signin(job: JobCreate):
    job_df= pd.DataFrame([job.model_dump()])
    predicted_salary= predict_salary(job_df)
    return {'salary': predicted_salary}