import boto3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
client = boto3.client('comprehend')

def start_topic_job(client, input, output):
    client.start_topics_detection_job(
        InputDataConfig={
            'S3Uri': input,
            'InputFormat': 'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': output,
            'KmsKeyId': ''
        },
        JobName='job-name-string',
        NumberOfTopics=4,
        VpcConfig={
            'SecurityGroupIds': ['string'],
            'Subnets': ['string']
        }
    )


def start_sentiment_job(client, input, output):
    client.start_sentiment_detection_job(
        InputDataConfig={
            'S3Uri': input,
            'InputFormat': 'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': output
        },
        DataAccessRoleArn=os.getenv('COMPREHEND_IAM_ROLE'),
        JobName='job-name-string',
        LanguageCode='en'
    )


def lambda_handler(event, context):
    logger.info(f'Event: {event}')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key'].replace('%3A', ':')
    input = f's3://{bucket}/{key}'
    output = f"s3://{os.getenv('OUTPUT_BUCKET')}"
    start_sentiment_job(client, input, output)
