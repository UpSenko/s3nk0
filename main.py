import os 
os.system('pip install discord')
import json
import discord
from discord.ext import commands
import urllib
 
client = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())
 
async def on_ready():
    print('Server Running')
 
 
@client.command()
async def meme(ctx):
    memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
 
    memeData = json.load(memeAPI)
     
    memeUrl = memeData['url']
    memeName = memeData['title']
     
    embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    embed.set_image(url=memeUrl)
    await ctx.send(embed=embed)
 
@client.command()
async def pring(ctx):
    await ctx.reply("Pong")
 
#BOT TOKEN
client.run('MTAyOTk0NDQ2MzA1OTA3NTE2Mg.GT03Y3.SriTYAboQXuevfTxWQgKTklKJ_FmhqwtFHfrH4')
