
import pandas as pd
import numpy as np
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk
import pandas as pd
import os
from pathlib import Path


def retrieve_job_role(title):
    title= title.lower()
    if 'data scientist' in title or 'decision scientist' in title:
        return 'Data Scientist'
    elif 'data engineer' in title or 'big data engineer' in title or 'data & analytics platform engineer' in title:
        return 'Data Engineer'
    elif 'data analyst' in title or 'business intelligence analyst' in title or 'operations data analyst' in title:
        return 'Data Analyst'
    elif 'machine learning' in title or 'ml' in title or 'ai/ml' in title:
        return 'Machine Learning Engineer'
    elif 'scientist' in title or 'research' in title or 'medical lab' in title or 'human factors' in title or 'purification' in title:
        return 'Scientist'
    elif 'software engineer' in title or 'engineering specialist' in title or 'computer scientist' in title or 'developer' in title:
        return 'Software / Engineer'
    elif 'analytics manager' in title or 'data science manager' in title or 'director' in title or 'vp' in title:
        return 'Analytics / Manager'
    else:
        return 'Other'


def check_is_senior(title):
    title= title.lower()
    if 'sr' in title or 'Senior' in title:
        return 1
    else :
       return 0

def processing():
    
    current_dir = Path(__file__).parent
    data_path = current_dir.parent.parent / "data" / "uncleaned-ds-jobs.csv"
    df = pd.read_csv(data_path)

    # 1.Convert object column type to String

    for col in df.columns:
       if df[col].dtype == object:
         df[col]= df[col].astype("string")

    # 2. deal with Salary Estimate and Revenue features

    num_columns= ["Salary Estimate", "Revenue"]
    for col in num_columns:
        df[col]=df[col].apply(lambda x:
                            (np.median([ float(i) for i in re.findall(r"\d+", x)])* 
                            (1000 if 'billion' in x.lower() else 1)) 
                            if isinstance(x, str) and re.findall(r"\d+", x) 
                            else np.nan
                            )
    # 3. Handle messing values of column Revenue after transformation

    revenue_mode_by_year = df.groupby('Founded')['Revenue'].apply(
        lambda x: x.mode()[0] if not x.mode().empty else None
    )
    mod_global_rev= df['Revenue'].mode()[0]
    revenue_mode_by_year.shape
    revenue_mode_by_year=revenue_mode_by_year.fillna(mod_global_rev)
    revenue_mode_by_year.shape
    
    df["Revenue"]=df["Revenue"].fillna(df['Founded'].map(revenue_mode_by_year))

    # 4. handle outliers

    q1_list= {}
    q3_list = {}
    iqr_list= {}
    lower_bound= {}
    uper_bound= {}

    numeric_data= df[["Founded","Revenue"]].copy()
    numeric_data.head()
    for col in numeric_data.columns:
        print(f'handle outlier for {col}')
        q1_list[col]=np.percentile(numeric_data[col], 25)
        q3_list[col]=np.percentile(numeric_data[col], 75)
        iqr_list[col]=q3_list[col]- q1_list[col]
        lower_bound[col]= q1_list[col] -( 1.5 * iqr_list[col])
        uper_bound[col]= q3_list[col] +( 1.5 * iqr_list[col])
    print(q1_list)
    print(q3_list)
    print(iqr_list)
    print(lower_bound)
    print(uper_bound)
    #replace them
    for col in numeric_data.columns:
        numeric_data[col]= np.where(numeric_data[col]> uper_bound[col], uper_bound[col], numeric_data[col])
        numeric_data[col]= np.where(numeric_data[col]< lower_bound[col], lower_bound[col], numeric_data[col])
        df[col]=numeric_data[col]
    # 5. create new columns more specifique for title
    df["job_role"]= df["Job Title"].apply(retrieve_job_role)
    df["is_senior"]= df["Job Title"].apply(check_is_senior)

    # NLP cleaning for textual data
    # 1. Normalisation(lowercase)

    nlp_features = ["Job Description"]
    for feature in nlp_features:
        df[feature]= df[feature].str.lower()

    # 2. Tokenization & detele ponctuations

    tokenizer= RegexpTokenizer(r'\w+')
    for feature in nlp_features:
        df[feature]= df[feature].apply(lambda x: tokenizer.tokenize(str(x)))
    print('tokenisation')

    # 3. suppression des stopwords

    nltk.download('stopwords')
    stopwrords_en= stopwords.words('english')
    for feature in nlp_features:
        df[feature]= df[feature].apply(lambda x:[word for word in x if word not in stopwrords_en])
    print("stopwords")
    df.drop(columns= ["Job Title", "index","Rating"])
    # with open("./data/cleaned_jobs.csv", "wb") as f:
    #     f.write(df)
    df.to_csv("backend/app/data/cleaned_jobs.csv", index=False)
    return df

df = processing()
print(df.head())


    
