import os
import json
from replit import db

class Pet:
  def __init__(self, name):
    self.name = name

  @classmethod
  def fromdict(cls, dict):
    return cls(dict['name'])

tort = Pet('tort')

print("tort:", tort)
db['key'] = json.dumps(tort.__dict__)

txt = json.loads(db['key'])
tle = Pet.fromdict(txt)

print("tle:", tle)
print(tle.name)
print(db['key'])