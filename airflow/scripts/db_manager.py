from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import pytz

timezone = pytz.time('Asia/Dhaka')

Base = declarative_base()

class JobListing(Base):
    __tablename__ ='job_listings'
    id = Column(String, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    link = Column(String)
    posted_datea = Column(DateTime, default=datetime.now(timezone))

def get_session():
    engine = create_engine('sqlite:///jobs.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def update_job_listings(jobs):
    session = get_session()
    for job in jobs:
        existing_job = session.query(JobListing).filter_by(link=job['link']).first()
        posted_date = datetime.fromisoformat(job['posted_date']).astimezone(timezone) if job.get('posted_date') else None

        if existing_job:
            existing_job.title = job['title']
            existing_job.company = job['company']
            existing_job.location = job['location']
            existing_job.posted_date = posted_date

        else:
            new_job = JobListing(
                id=job['link'],
                title=job['title'],
                company=job['company'],
                location=job['location'],
                link=job['link'],
                posted_date=posted_date
            )

            session.add(new_job)
        session.commit()

    
    def remove_old_listings():
        session = get_session()
        one_month_ago = datetime.now(timezone) - timedelta(days=30)
        old_jobs = session.query(JobListing).filter(JobListing.posted_date < one_month_ago).all()
        for job in old_jobs:
            session.delete(job)
        session.commit()