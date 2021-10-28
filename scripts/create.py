from functions.iam import create as c_iam
from functions.dynamodb import create as c_dynamodb
from functions.s3 import create as c_s3, update as u_s3
from functions.lambda_f import create as c_lambda_f

# Create iam function and add permissions
c_iam()

# Create dynamodb table
c_dynamodb()

# Create s3 bucket
c_s3()

# Update s3 bucket
u_s3()

# Create lambda function
c_lambda_f()

