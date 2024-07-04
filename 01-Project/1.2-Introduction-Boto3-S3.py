'''
**Tasks**:

1. Install Boto3 and set up AWS credentials.
2. Write a basic script to create an S3 bucket using Boto3.
3. List all S3 buckets in your AWS account using Boto3.
'''


import boto3

s3_client = boto3.client('s3')

def create_bucket(bucket_name, region):
    s3_client = boto3.client('s3', region_name=region)
    location = {'LocationConstraint': region}
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)


create_bucket('mm-y2', 'us-east-2')

###########

response = s3_client.list_buckets()

# Output the bucket names
print('Existing buckets:')

for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')