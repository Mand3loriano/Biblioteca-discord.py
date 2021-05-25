import discord
from discord.ext import commands 

PREFIX = 'prefixo_do_seu_bot'
client = commands.Bot(command_prefix=PREFIX)

@client.event 
async def on_ready():
    print('Pronto para uso!\n') 
    print(f'Nome: {client.user}\n')
    
@client.command() # comando de kick
async def kick(ctx, membro : discord.Member, *,motivo=None):
    if ctx.author.guild_permissions.kick_members:
     canal = client.get_channel(id=id_do_canal)
     msg = f'{ctx.author.mention} expulsou {membro.mention} por {motivo}'
     await membro.kick()
     await canal.send(msg)

@client.command() # comando de ban
async def ban(ctx, membro : discord.Member, *,motivo=None):
    if ctx.author.guild_permissions.ban_members:
     canal = client.get_channel(id=id_do_canal)
     msg = f'{ctx.author.mention} baniu {membro.mention} por {motivo}'
     await membro.ban()
     await canal.send(msg) 
    
Token = 'Token_do_seu_bot' 
client.run(Token)
