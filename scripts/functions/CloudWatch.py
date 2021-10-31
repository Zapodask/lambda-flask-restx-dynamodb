import boto3
import os

from dotenv import load_dotenv

load_dotenv()
name = os.getenv('NAME')

client = boto3.client('logs')

class CloudWatch():
    def create(self):
        client.create_log_group(
            logGroupName=f'/aws/lambda/{name}'
        )
