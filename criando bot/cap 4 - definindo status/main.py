import discord 
from discord.ext import commands

PREFIX = 'prefixo_do_seu_bot'
client = commands.Bot(command_prefix=PREFIX)

@client.event 
async def on_ready():
    activity = discord.Game(name='Ola mundo', type=3)
    await client.change_presence(status=discord.Status.online, activity=activity) 
    '''
    ao vivo -> activity = discord.Streaming(name="ola mundo", url="twitch_url")
    ouvindo -> activity = discord.Activity(type=discord.ActivityType.listening, name="ola mundo")
    assistindo -> activity = discord.Activity(type=discord.ActivityType.watching, name="ola mundo")
    '''
    print('Pronto para uso!\n') 
    print(f'Nome: {client.user}\n')
         
Token = 'Token_do_seu_bot' 
client.run(Token)
