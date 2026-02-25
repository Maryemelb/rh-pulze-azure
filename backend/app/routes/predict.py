
from fastapi import APIRouter, Depends, Response
from pytest import Session

from backend.app.schemas.user_schema import SigninUser
from backend.app.services.authService import login
from backend.app.db.dependencies import getdb
from backend.app.services.predict import predict_salary
from backend.app.schemas.job_schema import JobCreate
from backend.app.models.user import User
from backend.app.services.authService import get_current_user
import pandas as pd

router=APIRouter(
    prefix="/predict-salary",
    tags=["predict-salary"]
)
#, response:Response,db= Depends(getdb)
@router.post('/')
async def predict(job: JobCreate, db:Session= Depends(getdb), current_user: User= Depends(get_current_user)):
    job_df= pd.DataFrame([job.model_dump()])
    predicted_salary= predict_salary(job_df)
    return {'salary': predicted_salary}