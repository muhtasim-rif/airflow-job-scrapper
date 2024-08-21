import boto3
import json
from datetime import datetime

S3_BUCKET = 'bucket_name'
S3_KEY = 'job_listings/'

def upload_to_s3(data, file_name):
    s3 = boto3.client('s3')
    file_path = f'{S3_KEY}{file_name}'
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=file_path,
        Body=json.dumps(data),
        ContentType='application/json'

    )

    print(f'Uploaded data to {file_path}')