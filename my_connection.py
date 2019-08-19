import psycopg2
import json
import sys

with open("/Users/roma/PycharmProjects/Calculator/venv/config.json") as file:
    config = json.load(file)

config['host'] = '127.0.0.1'
config['port'] = '5432'

required_keys = ['user', 'password', 'host', 'port']
try:
    for i in required_keys:
        if not config[i]:
            raise Exception
except Exception:
    print(' "{}" has empty value.'.format(i))
    sys.exit()
