import os
import boto3
from datetime import datetime
import pytz

timezone = pytz.timezone('Asia/Dhaka')

S3_BUCKET = os.getenv("S3_BUCKET")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")


def upload_to_s3(file_name):
    s3 = boto3.client('s3',
                      endpoint_url='http://minio:9000',
                      aws_access_key_id=S3_ACCESS_KEY,
                      aws_secret_access_key=S3_SECRET_KEY)
    
    s3.upload_file(file_name, S3_BUCKET, f"jobs_{datetime.now(timezone).strftime("%Y%m%d_%H%M%S")}.json")

    print('Uploaded data.')