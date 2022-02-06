import discord
import os
import math
import random
import json
from replit import db
from objects import User, Cat

client = discord.Client()

command_prefix = "tc!"

major_list = ["IS", "CS", "Math", "Physics"]

def print_db():
  print("Printing Replit database")
  for key in db.keys():
    print("{", key, ":", db[key], "}")


# DMs the user for some info to get them set up
# TODO: Use reactions instead of manual typing
async def signup(id, msg=None):
  users = db["users"]

  my_key = str(id)
  # if user not in database, add them
  if my_key in users.keys():
    my_user = User.fromJson(users[my_key])
    print("expecting: ", my_user.expecting)
    
  else:
    my_user = User()
    users[my_key] = my_user.toJson()

  assert(isinstance(my_user, User))

  
  # Switch on user.expecting
  option = my_user.expecting
  print("LOOK HERE!!!!", option)
  if (option == ""):
    await id.send("Hi and welcome, let's get you set up with TravelCats!")
    my_user.expecting = "birth_year"

    new_str= my_user.toJson()
    print("new update:", new_str)
    users[my_key] =new_str
    print("new_user thingy", users[my_key])
    #check here if save to json
    new_user = User.fromJson(users[my_key])
    print("new user pulled", new_user)


    db["user"] = users
    print_db()
    await id.send("First, when were you born?")


  elif (option == "birth_year"):
    if(msg.isnumeric() and
       int(msg) >= 1900 and
       int(msg) <= 2022):
      my_user.birth_year = int(msg)
      my_user.expecting = "major"

      users[my_key] = my_user.toJson()
      db["users"] = users
      await id.send("What is your major?")
    else:
      await id.send("Please enter your birth year again.")


  elif (option == "major"):
    if msg in major_list:
      my_user.major = msg
      my_user.expecting = ""

      users[my_key] = my_user.toJson()
      db["users"] = users
      await id.send("Done! Here is your cat.")
    else:
      await id.send("Sorry, what you entered is not in our list. Please enter one of {}.".format(major_list))


  else:
    await id.send("Something wrong happened. Do you already have a profile?")

  users[my_key] = my_user.toJson()
  db["users"] = users
  return
      

@client.event
async def on_ready():
  print("TC is running on {}".format(client.user))
  db["users"] = {}

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  # print(message.channel)
  # print(message.author)

  # Commands we want to use
    # tc!help
    # tc!join - adds a user
    # tc!visit - set new travel location
    # tc!cat - go to dressing room
    # tc!inv - check inventory
  if msg.startswith(command_prefix):
    rest = msg[len(command_prefix):]
    words = rest.split()
    keyword = words[0]

    if keyword == "help":
      await message.channel.send("This is not a helpful message!")
    elif keyword == "join":
      # await signup(message.author) # DM them for more information
      await message.channel.send("I have sent you a message, please check your DMs!")
      await signup(message.author)

    elif keyword == "visit":
      pass
    elif keyword == "cat":
      pass
    elif keyword == "inv":
      pass


  if (isinstance(message.channel, discord.channel.DMChannel)):
    # Direct message
    print("reached dm")
    await signup(message.author, msg)


client.run(os.getenv('TOKEN'))

# db["users"] = {}
# users = db["users"]

# my_user = User()
# my_user.major = "Gamer"

# string = my_user.toJson()
# print(string)
# users["shep"] = string 

# new_user = User.fromJson(users["shep"])

# print(new_user.major)


