import json
import random
import boto3
import shutil
import os

download_path = './download/output.tar.gz'
upload_path = './upload'
try:
    os.mkdir('./download')
    os.mkdir(upload_path)
except:
    pass

uri = 'twitter-comprehend-output-bucket'
key = '902466892473-KP-04d2491a86f2290b69d20c43fa98eaac/output/output.tar.gz'
root = key.split('/')[0]

def s3_unpack(uri, key):
    # Download compressed comprehend-output from s3 and unpack it.
    s3_client = boto3.client('s3')
    s3_client.download_file(uri, key, Filename=download_path)
    shutil.unpack_archive(download_path, extract_dir=upload_path)

s3_unpack(uri, key)

def parse_phrases(infile_path):
    # Read and write keyphrases from comprehend-output into json.
    # Return random selection of phrases as a list.
    data = []
    with open(infile_path, 'r') as file:
        for line in file.readlines():
            try:
                obj = json.loads(line)['KeyPhrases']
            except:
                pass

            n = json.loads(line)['Line']
            for item in obj:
                phrase = item['Text']
                score = item['Score']
                if len(phrase) > 16 and len(phrase) < 80 and '@' not in phrase and score > 0.99:
                    item = {}
                    item['id'] = n
                    item['score'] = float(score)
                    item['phrase'] = phrase
                    data.append(item)

    # items = sorted(data.items(), key=lambda x: x[1], reverse=True)
    with open('clean-json.json', 'w') as file:
        for item in data:
            file.write(json.dumps(item, indent=4) + '\n')

    highlights = []
    for i in range(15):
        phrase = random.choice(data)
        print((phrase)['phrase'])
        highlights.append(phrase)

parse_phrases(upload_path+'/output')
