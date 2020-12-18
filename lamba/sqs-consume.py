import boto3
import os
import random
import string
import json

sqsurl = 'https://sqs.eu-central-1.amazonaws.com/902466892473/Twitter-Search-Queue.fifo'

sqs = boto3.client('sqs')

def sqs_receive():
    response = sqs.receive_message(
        QueueUrl=sqsurl,
        MaxNumberOfMessages=1
    )
    message = response['Messages'][0]

    sqs.delete_message(
        QueueUrl=sqsurl,
        ReceiptHandle=message['ReceiptHandle']
    )
    return message


lista = []
for i in range(5):
    lista.append(sqs_receive())

with open('sqs-rcvmsgs.json', 'w') as file:
    json.dump(lista, file, indent=4)
