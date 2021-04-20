import discord #importações do seu bot
from discord.ext import commands

PREFIX = 'prefix' #prefixo do seu bot
client = commands.Bot(command_prefix=PREFIX)

@client.event #definimos um evento
async def on_ready():
    print('Pronto para uso!\n') #prints no log
    print(f'Nome: {client.user}\n')

Token = 'Token'#Token do seu bot
client.run(Token)
