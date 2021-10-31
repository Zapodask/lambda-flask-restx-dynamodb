import boto3
import os
import json

from dotenv import load_dotenv

load_dotenv()
name = os.getenv('NAME')

client = boto3.client('iam')


class Iam:
    def create(self):
        role_name = f'{name}-role'

        role = {
            "Version": "2012-10-17",
            "Statement": [
                {
                "Effect": "Allow",
                "Principal": {
                    "Service": [
                        "lambda.amazonaws.com"
                    ]
                },
                    "Action": "sts:AssumeRole"
                }
            ]
        }


        client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(role),
        )

        client.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
        )

        
        client.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess'
        )


        print('Iam created')
