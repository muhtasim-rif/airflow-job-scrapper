import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from scripts.scraper import scrape_jobs
from scripts.s3_manager import upload_to_s3
from datetime import datetime, timedelta
import pytz


timezone = pytz.timezone('Asia/Dhaka')

default_args={
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'timezone': timezone,

}

dag = DAG(
    'job_scraper',
    default_args=default_args,
    description='A DAG to fetch job listings from Google Jobs using SerpApi and uploads to MinIO',
    schedule_interval='0 20 * * *',
    
)

def run_scraper_and_upload():
    jobs = scrape_jobs()
    if jobs: 
        file_name = f'files/jobs_{datetime.now(timezone).strftime("%Y%m%d_%H%M%S")}.json'
        with open(file_name, 'w') as f:
            json.dump(jobs, f, indent=4)

        upload_to_s3(file_name)

scrape_and_upload = PythonOperator(
    task_id='scrape_and_upload',
    python_callable=run_scraper_and_upload,
    dag=dag,
)

