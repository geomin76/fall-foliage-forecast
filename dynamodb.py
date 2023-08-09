import boto3
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.client(
    'dynamodb', 
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
)

dynamodb.put_item(TableName='fall-foliage', Item={'location_id': {'S': 'hello'}})
