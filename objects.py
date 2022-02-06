import random
import json

color_list = ["white", "gray", "yellow", "black"]

hat_list = ["cowboy", "santa", "police", "beanie"]

outfit_list = ["cowboy", "santa", "police", "jacket"]

class User:
  def __init__(self):
    # We should probably encrypt PII
    self.expecting = ""
    
    self.birth_year = 0
    self.major = ""
    self.interest = ""
    self.personality = ""

    # self.cat = Cat()
    # self.connections = []
    # self.time_without_connection = 0

    self.x, self.y = (0,0)
    self.color = ""
    self.hat = ""
    self.outfit = ""

  @classmethod
  def fromJson(cls, Json):
    d = json.loads(Json)
    user = cls()
    for key in d:
      user.__dict__[key] = d[key]
    return user

  def toJson(self):
    return json.dumps(self.__dict__)


class Cat:
  def __init__(self, color="white", hat="cowboy", outfit="cowboy"):
    self.x, self.y = (0,0)
    self.color = color
    self.hat = hat
    self.outfit = outfit
    self.hats = [hat]
    self.outfits = [outfit]

  @staticmethod
  def randomCat():
    return Cat(random.choice(color_list), random.choice(hat_list), random.choice(outfit_list))

  def __repr__(self):
    return "A {} cat with a {} hat in a {} outfit.".format(self.color, self.hat, self.outfit)
