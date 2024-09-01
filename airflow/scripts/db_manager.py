from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import pytz

timezone = pytz.timezone('Asia/Dhaka')

Base = declarative_base()

class JobListing(Base):
    __tablename__ ='job_listings'
    id = Column(String, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    link = Column(String)
    posted_date = Column(DateTime(Timezone=True), default=lambda: datetime.now(timezone))

def get_session():
    DATABASE_URL = 'postgresql+psycopg2://postgres:admin@localhost/postgres'
    engine = create_engine(DATABASE_URL)
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
        session.query(JobListing).filter(JobListing.posted_date < one_month_ago).delete(synchronize_session=False)
        
        session.commit()