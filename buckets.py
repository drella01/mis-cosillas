import boto3
import os

#AWS_ACCESS_KEY_ID='your-aws-key-id'
#AWS_SECRET_ACCESS_KEY=''

s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
#jmcbucket = s3.Bucket('bucket-name')

path = f"{os.getenv('HOME')}/Downloads/"

def download(item):
    if not os.path.exists(os.path.dirname(f'{path}{item.key}')):
        os.makedirs(os.path.dirname(f'{path}{item.key}'))
    response = jmcbucket.download_file(item.key,f'{path}{item.key}')
    return response

for file in list(jmcbucket.objects.all()):
    download(file)
    print(file.key)

"""for file in os.listdir(path):
    jmcbucket.upload_file(f'{path}{file}',f'renting/{file}')
    print(f'{path}{file}')"""
