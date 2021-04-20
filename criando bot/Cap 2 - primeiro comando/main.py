import discord 
from discord.ext import commands

PREFIX = 'prefixo_do_seu_bot'
client = commands.Bot(command_prefix=PREFIX)

@client.event 
async def on_ready():
    print('Pronto para uso!\n') 
    print(f'Nome: {client.user}\n')

@client.command() # definimos o comando
async def ola(ctx):  #aqui definimos o comando quando digitarmos /ola o bot vai responder 
    msg = 'olá mundo'  #criamos uma váriavel para a msg
    await ctx.send(msg) 
            #colocamos para o bot mandar essa msg no chat do ctx ou membro 
    
    
Token = 'Token_do_seu_bot' 
client.run(Token)
