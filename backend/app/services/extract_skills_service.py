import time

import pandas as pd
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from tqdm import tqdm
import os
from dotenv import load_dotenv
load_dotenv()
ENDPOINT = os.getenv('AZURE_ENDPOINT')
KEY = os.getenv('KEY')


def authenticate_client():
    return TextAnalyticsClient(endpoint=ENDPOINT, credential=AzureKeyCredential(KEY))


def run_ner_extraction(data_path, output_path, limit=100):
    client = authenticate_client()
    df = pd.read_csv(data_path)

    # Process only the requested limit
    df_subset = df.head(limit).copy()

    all_skills = []

    print(f"Extracting skills for {limit} jobs using Azure NER...")

    # Process 1 by 1 to avoid batch limits
    for i, row in tqdm(df_subset.iterrows(), total=len(df_subset)):
        description = str(row["Job Description"])[:1000]  # 1000 chars
        try:
            response = client.recognize_entities([description])
            doc = response[0]
            if not doc.is_error:
                # relevant skills are in 'Skill' or 'Product' categories
                skills = [
                    entity.text
                    for entity in doc.entities
                    if entity.category in ["Skill", "Product"]
                ]
                all_skills.append(", ".join(list(set(skills))))
            else:
                all_skills.append("")
        except Exception as e:
            print(f"\nError at row {i}: {e}")
            all_skills.append("")

        # Free tier pause
        time.sleep(1.0)

    df_subset["extracted_skills"] = all_skills
    df_subset.to_csv(output_path, index=False)
    print(f"\nExtraction complete. Saved {len(df_subset)} records to {output_path}")


def extract_skills_for_one_job(description1: str):
    client = authenticate_client()

    print(f"Extracting skills for jobs using Azure NER...")
    skills_list = []
    description = str(description1)[:1000]  # 1000 chars
    try:
        response = client.recognize_entities([description])
        doc = response[0]

        if not doc.is_error:
            skills_list = [
                entity.text
                for entity in doc.entities
                if entity.category in ["Skill", "Product"]
            ]
            skills_list = sorted(set(skills_list))  # remove duplicates
    except Exception as e:
        print(f"Error processing description: {e}")

    time.sleep(1.0)
    print(skills_list)
    return skills_list

if __name__ == "__main__":
    run_ner_extraction("backend/app/data/cleaned_jobs.csv", "backend/app/data/dataset_with_skills.csv", limit=5)