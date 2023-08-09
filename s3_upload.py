import boto3
from botocore.exceptions import ClientError

client = boto3.client(
    's3',
    aws_access_key_id="ACCESS_KEY",
    aws_secret_access_key="SECRET_KEY",
    aws_session_token="SESSION_TOKEN"
)

# # If S3 object_name was not specified, use file_name
# if object_name is None:
#     object_name = os.path.basename(file_name)

file_name = ""
bucket = ""
object_name = ""

# Upload the file
s3_client = boto3.client('s3')
try:
    response = s3_client.upload_file(file_name, bucket, object_name)
except ClientError as e:
    print(e)