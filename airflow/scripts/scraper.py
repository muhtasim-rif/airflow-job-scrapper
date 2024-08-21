import requests
from datetime import datetime
import pytz

timezone = pytz.timezone('Asia/Dhaka')


ACCESS_TOKEN = 'access_token'
BASE_URL = 'https://api.linkedin.com/v2'


def get_header():
    return {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'

    }


def fetch_job():
    url = f'{BASE_URL}/jobs'
    headers = get_header()
    params = {
        'keywords': 'data engineer',
        'location': 'Dhaka',
        'count': 25
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error fetching data: {response.status_code}')
        return None
    
def scrape_linkedIn():
    job_data = fetch_job()
    jobs = []
    if job_data:
        for job in job_data.get('elements', []):
            title = job.get('title', 'N/A')
            company = job.get('companyName', 'N/A')
            location = job.get('location', 'N/A')
            link = job.get('url', 'N/A')
            posted_date_str = job.get('datePosted', '')

            try:
                posted_date = datetime.strptime(posted_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                posted_date = posted_date.astimezone(timezone)

            except ValueError:
                posted_date = timezone.localize(datetime.now(timezone))


            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'link': link,
                'posted_date': posted_date.isoformat()

            })
    return jobs
