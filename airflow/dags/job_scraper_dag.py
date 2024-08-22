from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from scripts.scraper import scrape_jobs
from scripts.git_manager import upload_to_git
from datetime import datetime, timedelta
import pytz
#from scripts.s3_manager import upload_to_s3

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
    description='A DAG to fetch job listings from SerpApi and upload to Git',
    schedule_interval='0 20 * * *',
    
)

def run_scraper_and_upload():
    jobs = scrape_jobs()
    if jobs: 
        file_name = f'jobs_{datetime.now(timezone).strftime("%Y%m%d_%H%M%S")}.json'
        upload_to_git(jobs, file_name)

scrape_and_upload = PythonOperator(
    task_id='scrape_and_upload',
    python_callable=run_scraper_and_upload,
    dag=dag,
)

