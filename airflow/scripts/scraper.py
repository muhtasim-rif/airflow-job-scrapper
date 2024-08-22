import os
import serpapi
from datetime import datetime
import pytz

timezone = pytz.timezone('Asia/Dhaka')


SERPAPI_API_KEY = '65a170ad84895c39a99003aa0f033fe7def1f0c7'

if not SERPAPI_API_KEY:
    raise ValueError("No SERPAPI_API_KEY found in environment variables. Please set it before running the script.")


def fetch_jobs_from_serpapi():

    client = serpapi.Client(api_key=SERPAPI_API_KEY)

    params = {
        "engine": "google_jobs",
        "q": "data engineer",
        "location": "Dhaka",
        
    }

    results = client.search(params)

    if 'jobs' in results:
        return results['jobs']
    else:
        print(f"Error fetching data from SerpApi: {results.get('error', 'Unknown error')}")
        return None

    
def scrape_jobs():
    job_data = fetch_jobs_from_serpapi()
    jobs = []

    if job_data:
        for job in job_data:
            title = job.get('title', 'N/A')
            company = job.get('company_name', 'N/A')
            location = job.get('location', 'N/A')
            link = job.get('url', 'N/A')
            posted_date_str = job.get('date_posted', '')

            try:
                posted_date = datetime.strptime(posted_date_str, '%Y-%m-%d')
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
