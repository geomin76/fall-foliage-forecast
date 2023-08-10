import boto3
import os
from dotenv import load_dotenv
from model import DataEntry

load_dotenv()

dynamodb = boto3.client(
    'dynamodb', 
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
)

def insert_data(item: DataEntry) -> bool:
    dynamodb.put_item(TableName='fall-foliage', Item={
        'location_id': {'S': item.location_id}, 
        'blob_url': {'S': item.blob_url},
        'color_percentage': {'N': str(item.color_percentage)},
        'timestamp': {'S': str(item.timestamp)},
        'id': {'S': str(item.id)}
    })
    return True

def get_data():
    response = dynamodb.scan(TableName='fall-foliage')
    return response['Items']