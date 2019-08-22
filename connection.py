import psycopg2
import json
import sys
import os

with open(os.environ.get('CONFIG')) as file:
    config = json.load(file)

if 'host' not in config.keys():
    config['host'] = '127.0.0.1'
if 'port' not in config.keys():
    config['port'] = '5432'

required_keys = ['user', 'password', 'host', 'port']
try:
    for i in required_keys:
        if not config[i]:
            raise Exception
except Exception:
    print(' "{}" has empty value.'.format(i))
    sys.exit()
