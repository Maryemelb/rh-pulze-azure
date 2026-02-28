

from backend.app.models.jobs import Jobs
from backend.app.schemas.job_schema import JobCreate

from requests import Session

async def addjob(db: Session,job: JobCreate):
    #pydantic to scheme
    new_job = Jobs(**job.model_dump())

    db.add(new_job)
    db.commit()
    return {
        'title': new_job.job_title,
        'message': 'job added succesfully'
    }

async def getJobs(db: Session,job: JobCreate):
    jobs= db.query(Jobs).all()
    if jobs is None:
        print('j')
    return jobs 