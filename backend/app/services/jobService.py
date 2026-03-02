

from backend.app.ml.data_processing.processing import process_single_row
from backend.app.models.jobs import Jobs
from backend.app.schemas.job_schema import JobCreate
import pandas as pd
from requests import Session

async def addjob(db: Session,job: JobCreate):
    job_df= pd.DataFrame([job.model_dump()])
    job_df = job_df.rename(columns={
    "job_title": "Job Title",
    "salary_estimate": "Salary Estimate",
    "job_description": "Job Description",
    "rating": "Rating",
    "company_name": "Company Name",
    "location": "Location",
    "headquarters": "Headquarters",
    "size": "Size",
    "founded": "Founded",
    "type_of_ownership": "Type of ownership",
    "industry": "Industry",
    "sector": "Sector",
    "revenue": "Revenue",
    "competitors": "Competitors"
})
    df=process_single_row(job_df)

    #rename columns again

    df = df.rename(columns={
    "Job Title": "job_title",
    "Salary Estimate": "salary_estimate",
    "Job Description": "job_description",
    "Rating": "rating",
    "Company Name": "company_name",
    "Location": "location",
    "Headquarters": "headquarters",
    "Size": "size",
    "Founded": "founded",
    "Type of ownership": "type_of_ownership",
    "Industry": "industry",
    "Sector": "sector",
    "Revenue": "revenue",
    "Competitors": "competitors"
})
    
    #pydantic to scheme
    job_data = df.iloc[0].to_dict()

    new_job = Jobs(**job_data)

    db.add(new_job)
    db.commit()
    return {
        'title': new_job.job_title,
        'message': 'job added succesfully'
    }

async def getJobs(db: Session):
    jobs= db.query(Jobs).all()
    if jobs is None:
        print('j')
    return jobs 