import boto3
import os

from dotenv import load_dotenv

load_dotenv()
name = os.getenv('NAME')
table = os.getenv('TABLE')

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')

class Lambda():
    def create(self):
        role = iam_client.get_role(
            RoleName=f'{name}-role'
        )

        lambda_client.create_function(
            FunctionName=name,
            Role=role['Role']['Arn'],
            Code={
                'S3Bucket': f'{name}-bucketz',
                'S3Key': 'build.zip'
            },
            Runtime='python3.9',
            Handler='index.handler',
            Environment={
                'Variables': {
                    'TABLE': table
                }
            }
        )

        print('Lambda created')


    def update(self):
        lambda_client.update_function_code(
            FunctionName=name,
            S3Bucket=f'{name}-bucketz',
            S3Key='build.zip',
            Publish=True,
        )

        print('Lambda updated')
