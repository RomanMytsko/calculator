import psycopg2
import json
import sys
import os
import my_config

# CONFIG_FILE = 'config.json'

# config = json.load(config.json)
config = my_config.config

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
