import boto3
import os
import shutil

from dotenv import load_dotenv

load_dotenv()
name = os.getenv('NAME')

client = boto3.client('s3')


class S3():
    def create(self):
        client.create_bucket(
            Bucket=f'{name}-bucketz',
        )

        print('S3 created')


    def update(self):
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path + '/../../')
        cwd = os.getcwd()

        try:
            shutil.rmtree('build.zip', ignore_errors=True)
            shutil.rmtree('build')
        except:
            pass

        os.system(f'pip3 install -r ./requirements.txt \
            --upgrade --target {cwd}/build/')
        
        to_move = ['index.py', 'requirements.txt']
        [shutil.copyfile(file, f'build/{file}') for file in to_move]


        if 'src' in os.listdir():
            shutil.copytree('src', 'build/src')

        shutil.make_archive('build', 'zip', 'build')

        shutil.rmtree('build')

        client.upload_file(
            'build.zip',
            f'{name}-bucketz',
            'build.zip',
            {'ContentType': 'application/zip'},
        )

        os.remove('build.zip')

        print('S3 updated')
