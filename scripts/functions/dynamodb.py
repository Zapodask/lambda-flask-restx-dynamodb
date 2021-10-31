import boto3
import os

from dotenv import load_dotenv

load_dotenv()
table = os.getenv('TABLE')

client = boto3.resource('dynamodb')


class Dynamodb():
    def create(self):
        try:
            client.create_table(
                TableName=table,
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'N'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
        except Exception as e:
            print(e)

        print('Dynamodb table created')
