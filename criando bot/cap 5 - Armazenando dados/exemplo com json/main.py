import discord 
import json # importando json

from discord.ext import commands

with open('config.json') as e: 
  set_config = json.load(e) # Abrindo arquivo .json
  TOKEN = set_config['token'] # pegando o token e o prefix
  PREFIX = set_confog['prefix']

client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
  print('hello world')
  
client.run(TOKEN)
