'''
**Tasks**:

1. Write a script to upload a single file to an S3 bucket.
2. Modify the script to upload multiple files from a directory.
3. Add error handling for common issues like missing files or incorrect permissions.
'''


# 1. Write a script to upload a single file to an S3 bucket.

# import boto3

# s3 = boto3.client('s3')

# s3.upload_file('./Readme.md', 'mm-yy', 'Readme.md')
    

#########################################################################

# 2. Modify the script to upload multiple files from a directory.


# import boto3
# import os

# s3 = boto3.client('s3')

# files_in_dir = os.listdir(r'/home/vagrant/BOTO3_Project_HUB/01-Project')

# for each_file in files_in_dir:
#     s3.upload_file(each_file, 'yo-yo-bucket', each_file)



#########################################################################


# 3. Add error handling for common issues like missing files or incorrect permissions.


import boto3
import os

s3 = boto3.client('s3')


