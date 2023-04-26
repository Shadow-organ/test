import sys
import logging

from aiohttp.web import run_app

from sqli.app import init as init_app

log = logging.getLogger(__name__)

SECRET_KEY="mhTJv54FF5YT6YGzWZAff-X_53e591HZW4EF154h16v0="
S3_BUCKET_NAME=uat
AWS_ACCESS_KEY_ID=AFIAQWESQRFOAR6UK990
AWS_SECRET_ACCESS_KEY=mBA09a5QSZ37QqwLaOL2/Dj5dpgYq5Y1tkCNoUkb
AWS_REGION=ap-south-1

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(sys.argv[1:])

    host = app['config']['app']['host']
    port = app['config']['app']['port']
    log.info(f'App is listening at http://{host}:{port}')
    run_app(app, host=host, port=port)
    
    
