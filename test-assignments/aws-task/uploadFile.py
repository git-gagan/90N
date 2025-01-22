import boto3
import base64
import json
import os

'''
Reference:-> https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html

{
    "name": "sample file",
    "content": "base64-encoded file"
}
'''

s3_custom_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket_name = os.environ['BUCKET_NAME']
        file_name = event.get('file_name')
        file_content = event.get('file_content')

        if not file_name or not file_content:
            raise ValueError("Missing required fields")

        decoded_file = base64.b64decode(file_content)
        
        s3_custom_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=decoded_file,
            ContentType='application/pdf'
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully!', 'file': file_name})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
