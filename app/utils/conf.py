import commentjson

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = open("./conf/conf.json", "r")

import os
print(str(os.getcwd()))

config = commentjson.load(f)
print(commentjson.dumps(config, indent=4, sort_keys=True))