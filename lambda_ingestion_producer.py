import sys
import os
import tweepy as tw
from tweepy.parsers import JSONParser
import json
from datetime import datetime
import boto3

auth = tw.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
api = tw.API(auth, parser=JSONParser())

def twitter_search(api, query_string, count):
    search = api.search(q=query_string, count=count, tweet_mode='extended')
    return search

def store_api_calls(dict_obj):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Twitter-API-Calls')

    metadata = {}
    metadata['timestamp'] = str(datetime.utcnow())
    metadata['status_count'] = int(dict_obj['count'])
    metadata['completed_in'] = str(dict_obj['completed_in'])
    metadata['query_string'] = dict_obj['query']
    table.put_item(Item=metadata)

results = twitter_search(api, query_string='massive puppy dog', count=5)
store_api_calls(results['search_metadata'])
jsonfile['meta']['timestamp'] = str(datetime.utcnow())
jsonfile = {}
key = 0

for i in results['statuses']:
    key +=1
    jsonfile[key] = i
    

with open('./tweets', 'w') as f:
    json.dump(jsonfile, f, indent=4)

    
