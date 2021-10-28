from flask_restx import Namespace, Resource, fields
from flask import request
from boto3 import resource
from datetime import datetime
from pytz import timezone
from dotenv import load_dotenv

import os

load_dotenv()
env_table = os.getenv('TABLE')

dynamodb = resource('dynamodb')
table = dynamodb.Table(env_table)

api = Namespace('users/', description='Users')

userReturn = api.model('User', {
    'id': fields.String(readonly=True),
    'username': fields.String(),
    'password': fields.String(),
    'created_at': fields.String()
})

userExpect = api.model('User', {
    'username': fields.String(),
    'password': fields.String(required=True)
})

@api.route('/')
class Index(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(userReturn)
    def get(self):
        response = table.scan()

        return response['Items']


    @api.doc('store_user')
    @api.expect(userExpect)
    def post(self):
        data = request.get_json()

        response = table.scan()

        data['id'] = (len(response['Items']) + 1) + int(datetime.now(timezone('America/Sao_Paulo')).strftime('%m%d%Y%H%M%S'))
        data['created_at'] = str(datetime.now(timezone('America/Sao_Paulo')))

        table.put_item(Item=data)

        return 'User created', 200



@api.route('/<int:id>')
@api.param('id', 'User identifier')
@api.response(404, 'User not found')
class Id(Resource):
    @api.doc('show_user')
    @api.marshal_with(userReturn)
    def get(self, id):
        response = table.get_item(
            Key={
                'id': id
            }
        )

        return response['Item']


    @api.doc('update_user')
    @api.expect(userExpect)
    @api.marshal_with(userReturn)
    def put(self, id):
        data = request.get_json()

        table.update_item(
            Key={
                'id': id
            },
            UpdateExpression='set username=:u, password=:p',
            ExpressionAttributeValues={
                ':u': data['username'],
                ':p': data['password']
            }
        )

        response = table.get_item(
            Key={
                'id': id
            }
        )

        return response['Item']


    @api.doc('delete_user')
    def delete(self, id):
        table.delete_item(
            Key={
                'id': id
            }
        )

        return 'User deleted', 204