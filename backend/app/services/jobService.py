

from fastapi import Session
from backend.app.models.jobs import Jobs
from backend.app.schemas.job_schema import JobCreate


def addjob(db: Session,job: JobCreate, response):
    #pydantic to scheme
    new_job = Jobs(**job.model_dump())

    db.add(new_job)
    db.commit()
    return {
        'title': new_job.job_title,
        'message': 'job added succesfully'
    }

def getJobs(db: Session,job: JobCreate):
    jobs= db.query(Jobs).all()
    if jobs is None:
        print('j')
    return jobs 