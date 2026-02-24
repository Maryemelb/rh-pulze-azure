from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    index: int
    job_title: str
    salary_estimate: str
    job_description: str
    rating: float
    company_name: str
    location: str
    headquarters: str
    size: str
    founded: int
    type_of_ownership: str
    industry: str
    sector: str
    revenue: str
    competitors: str