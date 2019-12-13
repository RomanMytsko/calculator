import json
import sys
import os

with open(os.environ.get('CONFIG')) as file:
    config = json.load(file)

config['host'] = config.setdefault('host', '127.0.0.1')
config['port'] = config.setdefault('port', '5432')

required_keys = ['user', 'password']
try:
    for i in required_keys:
        if not config[i]:
            raise Exception
except Exception:
    print(' "{}" has empty value.'.format(i))
    sys.exit()


