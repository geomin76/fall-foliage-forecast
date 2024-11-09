import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os
import uuid
from PIL import Image
load_dotenv()

client = boto3.client(
    's3',
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID_KEY'),
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_PASSWORD_KEY'),
)

def upload_blob(file_path):
    object_name = str(uuid.uuid4()) + ".jpg"

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        compress_image(file_path)
        print("Uploading image to s3 for: ", object_name)
        response = s3_client.upload_file('./output.jpg', "fall-foliage-forecast-images", object_name)
    except ClientError as e:
        print(e)
    finally:
        os.remove('./output.jpg')
    
    return "https://s3.amazonaws.com/fall-foliage-forecast-images/" + object_name

def compress_image(file_path):
    print("Compressing image for: ", file_path)
    img = Image.open(file_path)
    rgb_im = img.convert('RGB')
    rgb_im.save('./output.jpg', optimize=True, quality=90)