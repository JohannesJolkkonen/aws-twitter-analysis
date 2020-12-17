import boto3
import zipfile
import shutil
import os
import psycopg2

uri = 'twitter-comprehend-output-bucket'
key = '902466892473-TOPICS-6039ff5c9a55af512a4bc453617dfc72/output/output.tar.gz'
root = key.split('/')[0]
rs_client = boto3.client('redshift')
s3_client = boto3.client('s3')

# Download comprehend-output from S3 and unpack it 
download_path = './tmp/download/output.tar.gz' 
upload_path = './tmp/upload'
s3_client.download_file(uri, key, Filename=download_path)
shutil.unpack_archive(download_path, extract_dir=upload_path)

# Upload unpacked csv-files back to S3
for file in os.listdir(upload_path):
    path = upload_path + '/' + file
    s3_client.upload_file(path, uri, f'{root}/unpacked/output/{file}')

# Load the csv-data from S3 into Redshift
db_params = {
    'db':'twitter-analytics',
    'user':os.getenv('DB_USER'),
    'pwd':os.getenv('DB_PASS'),
    'host':os.getenv('DB_HOST')
    } 

conn_string = f"dbname={db_params['db']}' port='5439' user={db_params['user']} password={db_params['pwd']} host={db_params['host']}"
con = psycopg2.connect(conn_string)
sql = open('./sql-scripts.sql', 'r').read()
con.cursor().execute(sql)
con.commit()
con.close()

