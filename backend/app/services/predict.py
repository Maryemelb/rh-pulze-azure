import sys
from backend.app.ml import training_pipeline

# Inject frequency_encoding into __main__ so pickle can find it
import __main__
__main__.frequency_encoding = training_pipeline.frequency_encoding

import joblib
from backend.app.schemas.job_schema import JobCreate
from backend.app.ml.data_processing.processing import process_single_row
import pandas as pd

def predict_salary(df: pd.DataFrame ):
    df = df.rename(columns={
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

    df=process_single_row(df)
    model= joblib.load('backend/app/saved_model/rf_model.pkl')
    salary_predict= model.predict(df)
    print(salary_predict[0])
    return salary_predict[0]

# {
#   "index": 0,
#   "job_title": "Développeur Full Stack",
#   "salary_estimate": "10,000 - 15,000 MAD / mois",
#   "job_description": "Développement et maintenance d'applications web, intégration front-end et back-end, travail avec Angular et Node.js.",
#   "rating": 4.2,
#   "company_name": "Inwi",
#   "location": "Casablanca, Maroc",
#   "headquarters": "Casablanca, Maroc",
#   "size": "1000-5000 employés",
#   "founded": 1999,
#   "type_of_ownership": "Privée",
#   "industry": "Télécommunications",
#   "sector": "Technologie",
#   "revenue": "5 milliards MAD",
#   "competitors": "Orange Maroc, Maroc Telecom"
# }
