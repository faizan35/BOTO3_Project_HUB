'''
**Tasks**:

1. Write a script to upload a single file to an S3 bucket.
2. Modify the script to upload multiple files from a directory.
3. Add error handling for common issues like missing files or incorrect permissions.
'''


# 1. Write a script to upload a single file to an S3 bucket.

import boto3

s3 = boto3.client('s3')

s3.upload_file('./Readme.md', 'mm-yy', 'Readme.md')
    




