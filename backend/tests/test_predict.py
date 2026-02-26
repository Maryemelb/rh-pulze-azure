import pytest
import pandas as pd
from backend.app.services.predict import predict_salary
@pytest.fixture
def job_df():
   job= {
            "index": 0,
            "job_title": "Développeur Full Stack",
            "salary_estimate": "10,000 - 15,000 MAD / mois",
            "job_description": "Développement et maintenance d'applications web, intégration front-end et back-end, travail avec Angular et Node.js.",
            "rating": 4.2,
            "company_name": "Inwi",
            "location": "Casablanca, Maroc",
            "headquarters": "Casablanca, Maroc",
            "size": "1000-5000 employés",
            "founded": 1999,
            "type_of_ownership": "Privée",
            "industry": "Télécommunications",
            "sector": "Technologie",
            "revenue": "5 milliards MAD",
            "competitors": "Orange Maroc, Maroc Telecom"
            }
   job_df= pd.DataFrame([job.model_dump()])
   return job_df

def test_predict_service(job_df: pd.DataFrame):
   predicted_salary= predict_salary(job_df)
   assert predicted_salary is not None
   assert isinstance(predicted_salary, float)


