import discord #vamos começar fazendo as importações do bot
from discord.ext import commands


Prefix = 'prefix do bot' #a variavel client define o prefix do bot
client = commands.Bot(command_prefix=Prefix) 


@client.event 
async def on_ready():
   print('tudo pronto')


client.run('Token')
