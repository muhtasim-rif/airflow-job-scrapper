import os
import serpapi
from datetime import datetime
import pytz
# import json

timezone = pytz.timezone("Asia/Dhaka")

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

if not SERPAPI_API_KEY:
    raise ValueError(
        "No SERPAPI_API_KEY found in environment variables. Please set it before running the script."
    )


def fetch_jobs_from_serpapi():
    client = serpapi.Client(api_key=SERPAPI_API_KEY)

    params = {
        "engine": "google_jobs",
        "q": "data engineer",
        "location": "Dhaka",
        "api_key": SERPAPI_API_KEY,
    }

    results = client.search(params)

    if results and isinstance(results, serpapi.models.SerpResults):
        results_dict=results.as_dict()
        if 'jobs_results' in results_dict:
            return results_dict['jobs_results']
        else:
            print(f"Error: 'jobs_results' not found in the response. Full Response: {results_dict}")
        return None
    else:
        print(f"Unexpected response type from SerpApi: {type(results)}. Full Response: {results}")
        return None


def scrape_jobs():
    job_data = fetch_jobs_from_serpapi()
    jobs = []

    if job_data:
        for job in job_data:
            title = job.get("title", "N/A")
            company = job.get("company_name", "N/A")
            location = job.get("location", "N/A")
            link = job.get("share_link", "N/A")
            posted_date_str = job.get("date_posted", "")

            try:
                posted_date = datetime.strptime(posted_date_str, "%Y-%m-%d")

                if posted_date.tzinfo is None:
                    posted_date = timezone.localize(posted_date)
                else:
                    posted_date = posted_date.astimezone(timezone)

            except ValueError:
                posted_date = timezone.localize(datetime.now())

            jobs.append(
                {
                    "title": title,
                    "company": company,
                    "location": location,
                    "link": link,
                    "posted_date": posted_date.isoformat(),
                }
            )
    return jobs
