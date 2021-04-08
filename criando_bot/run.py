import discord     #vamos começar fazendo as importações do bot
from discord.ext import commands


Prefix = 'prefix do bot' #a variavel client define o prefix do bot
client = commands.Bot(command_prefix=Prefix) 

#este event escrevera, "tudo pronto" no terminal se der tudo certo
@client.event 
async def on_ready():
   print('tudo pronto')

#define o token deu seu bot
client.run('Token')
