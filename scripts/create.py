from functions.Iam import Iam
from functions.Dynamodb import Dynamodb
from functions.S3 import S3
from functions.Lambda import Lambda
from functions.CloudWatch import CloudWatch

# Create iam function and add permissions
Iam.create()

# Create dynamodb table
Dynamodb.create()

# Create s3 bucket
S3.create()

# Update s3 bucket
S3.update()

# Create lambda function
Lambda.create()

# Create log group
CloudWatch.create()
