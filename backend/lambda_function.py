import json
import boto3
import base64
import uuid
import datetime

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

DDB_TABLE = 'StudentResumes'
S3_BUCKET = 'student-resumes-pdf'

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        student_id = str(uuid.uuid4())

        file_data = base64.b64decode(body['resume'])
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=f"{student_id}.pdf",
            Body=file_data,
            ContentType='application/pdf'
        )

        table = dynamodb.Table(DDB_TABLE)
        table.put_item(Item={
            'id': student_id,
            'full_name': body['full_name'],
            'email': body['email'],
            'education': body['education'],
            'skills': body['skills'],
            'uploaded_at': datetime.datetime.utcnow().isoformat()
        })

        return {
            'statusCode': 200,
            'headers': { "Access-Control-Allow-Origin": "*" },
            'body': json.dumps({'message': 'Resume uploaded successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': { "Access-Control-Allow-Origin": "*" },
            'body': json.dumps({'error': str(e)})
        }
