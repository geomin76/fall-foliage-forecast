import boto3
import os
from dotenv import load_dotenv
from service.model import DataEntry
from boto3.dynamodb.conditions import Key
load_dotenv()

dynamodb = boto3.client(
    'dynamodb', 
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID_KEY'),
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_PASSWORD_KEY'),
)

def insert_data(item: DataEntry) -> bool:
    dynamodb.put_item(TableName='fall-foliage', Item={
        'location_id': {'S': item.location_id}, 
        'blob_url': {'S': item.blob_url},
        'color_percentage': {'N': str(item.color_percentage)},
        'timestamp': {'S': str(item.timestamp)}
    })
    return True

def get_data(key: str, enable_data = False):
    table = boto3.resource('dynamodb').Table('fall-foliage')
    response = table.query(
        KeyConditionExpression=Key('location_id').eq(key)
    )
    items: [DataEntry] = []
    for item in response['Items']:
        if enable_data:
            print("Photo taken on {} with percentage {}".format(item['timestamp'],float(item['color_percentage'])))
        items.append(
            DataEntry(
                blob_url = item['blob_url'], 
                location_id = item['location_id'],
                timestamp = item['timestamp'],
                color_percentage = float(item['color_percentage'])
            )
        )
        
    if len(items) > 0:
        sorted(items, key=lambda item: item.timestamp)
        return items
    else:
        return items