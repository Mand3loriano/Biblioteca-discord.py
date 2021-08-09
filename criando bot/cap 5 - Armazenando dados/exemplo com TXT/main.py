import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

with open('token.txt','r') as arquivo:
  # R --> read ou ler
  # W --> write ou escrever
  # A --> add ou adicionar
  TOKEN = arquivo.read()
  
@client.event
asycn def on_ready():
  print('hello world')
  
client.run(TOKEN)
