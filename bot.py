import io
import aiohttp
import gogo_scraper
import alexflipnote
import discord
import asyncio
import os
import datetime
import random
import wikipedia
import giphy_client

import requests
import json
import praw
import re
import nekos
from urllib import parse
import urllib
import platform
import time
import sys
import colorsys
import random as r


from discordTogether import DiscordTogether
from discord import Color, Embed, Member
from discord.ext.commands import (
    BadArgument,
    BucketType,
    Cog,
    Context,
    command,
    cooldown,
    is_nsfw,)
from typing import ByteString, Union
from aiohttp.client import request
from discord import client
from discord import guild
from discord.colour import Color
from discord.ext import commands
from PIL import Image, ImageFilter
from io import BytesIO
from discord.ext.commands import Bot 
from random import randint
from discord.ext.commands.cooldowns import BucketType
from discord.webhook import RequestsWebhookAdapter
from random import choice
from asyncdagpi import Client, ImageFeatures
from giphy_client.rest import ApiException
from PIL import ImageEnhance
from discord.ext.commands import CommandNotFound
from discord_components import DiscordComponents, Button,ButtonStyle
from discord_components import DiscordComponents, Button
from nekos import img as nekosimg



bot = commands.Bot(command_prefix='f.')
api_key = "AIzaSyAz4iuQ6TScVN0eX1X6b80QTFoDrNMUcOc"
nasa_api = os.getenv('aPrygXh2F0jGxUQyJGki9gWhUUaLn1xnyhtEGfN7')
togetherControl = DiscordTogether(bot)
available_tags = ['wallpaper', 'meow', 'tickle', 'feed', 'poke', 'slap', 'avatar' 'holo', 'lizard', 'waifu', 'pat', '8ball', 'kiss', 'neko', 'spank', 'cuddle', 'hug' ]
lenght = int( '20' )
chars = '+-/*$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
warn_count = {}
snipe_message_content = None
snipe_message_author = None
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
alex_api = alexflipnote.Client("_joGe0upGjoZMByyFv-GdyGGoCunGJjyPOtv1Vq8")
DiscordComponents(bot)
YOUTUBE_KEY = os.getenv('AIzaSyCzJXKbpyUiAwLD6h-xz9YX-NEm7zz-mqU')


@bot.event
async def on_ready():
    print("""
   ▄████████    ▄████████     ███        ▄████████ 
  ███    ███   ███    ███ ▀█████████▄   ███    ███ 
  ███    █▀    ███    █▀     ▀███▀▀██   ███    ███ 
  ███         ▄███▄▄▄         ███   ▀   ███    ███ 
▀███████████ ▀▀███▀▀▀         ███     ▀███████████ 
         ███   ███    █▄      ███       ███    ███ 
   ▄█    ███   ███    ███     ███       ███    ███ 
 ▄████████▀    ██████████    ▄████▀     ███    █▀  
                                                   
""")

    print(f"———«Flarot Online»———")
    print(f"Bot online and logged in as {bot.user}")
    print(f"———«Ve a desarrollar mierda.»———")
    print(
        f"""--------
Current Discord.py Version: {discord.__version__}
--------
Use this link to invite {bot.user.name}
https://discordapp.com/api/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8
"""
)
    game = discord.Game('Disfrutando Las Vistas |>|')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="V5.0 || f.ayuda || Flarot"))
    channel = bot.get_channel(849348693144502282)
    embed = discord.Embed(
        color = discord.Color.purple()
    )

    embed.set_author(name="Status")
    embed.add_field(name="<:dataserver:859589182817173552>Flarot Esta Online", value=":green_circle: Probablemente Dani esta probando algo nuevo.")
    embed.set_footer(text=f"Discord Flarot Bot STATUS")
    embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
    await channel.send(embed=embed)
    

def deepfried(img):
    # Generate color overlay
    overlay = img.copy()
    overlay = ImageEnhance.Contrast(overlay).enhance(random.uniform(0.7, 1.8))
    overlay = ImageEnhance.Brightness(overlay).enhance(random.uniform(0.8, 1.3))
    overlay = ImageEnhance.Color(overlay).enhance(random.uniform(0.7, 1.4))

    # Blend random colors onto and sharpen the image
    img = Image.blend(img, overlay, random.uniform(0.1, 0.4))
    img = ImageEnhance.Sharpness(img).enhance(random.randint(5, 200))

    return img

def listToString(s):
    str1 = "\n \n"
    return (str1.join(s).replace(" & ", " AND "))

def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale = image.convert('L')
    return grayscale

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

# Empieza el codigo

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Ayuda"])
async def ayuda(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='|-| Ayuda |-|')
    embed.add_field(name='Diversion :joy:', value='``trivia`` ``yomomma`` ``textcat`` ``fakewords`` ``yesorno`` ``trumpthinks`` ``identity`` ``dick/penis/dong`` ``lovedetect`` ``hacker`` ``8ball`` ``owofy`` ``emojify`` ``freemoney`` ``zalgofy``  ``cheemify`` ', inline=False)
    embed.add_field(name='Anime :comet: ', value='``baka`` ``dance`` ``kill`` ``wink`` ''bored´´ ´´cry´´ ``bite`` ``highfive`` ``kiss`` ``punch`` ``findAnime`` ``laugh`` ``neko`` ``slap`` ``cringeanime`` ``poke`` ``hug`` ``pat`` ``waifu``', inline=False)
    embed.add_field(name='Moderacion :toolbox: ', value='``snipe`` ``warncount`` ``warn`` ``uinfo`` ``embed`` ``banlist`` ``addrole`` ``ban`` ``kick`` ``serverinfo`` ``clear``', inline=False)
    embed.add_field(name='Otros :robot:', value='``sum`` ``howvirgin`` ``howstupid`` ``howchad`` ``howgay`` ``define`` ``clicker`` ``calc`` ``bitcoin`` ``passgen`` ``tinyurl`` ``minecraft`` ``1337speak`` ``say`` ``submit`` ``countdown`` ``ìmg`` ``emoji`` ``avatar`` ``ping`` ``covid`` ``flip``', inline=False)
    embed.add_field(name='Imagenes :file_folder: ', value='``wanted`` ``fumo`` ``nekos`` ``nekos_tags`` ``apod`` ``robohash`` ``tweet`` ``triggered`` ``trump`` ``captcha`` ``pikachu`` ``horny`` ``sus`` ``randomgif`` ``sepia`` ``randompic`` ``glass`` ``deepfry`` ``invertgreyscale`` ``deepfry`` ``greyscale`` ``rainbow`` ``inverted`` ``rip`` ``bobburns`` ``gtawasted`` ``discovered`` ``mapacheqp``', inline=False)
    embed.add_field(name='Reddit <:reddit:855497006013218878> y Animales :fox:', value=' ``cursed`` ``dogfact`` ``catfact`` ``pandafact`` ``aww`` ``foxfact`` ``koalafact`` ``koala`` ``redpanda`` ``panda`` ``cat`` ``dog`` ``fox`` ``internetisart`` ``nature`` ``japan`` ``axolotls`` ``catmemes`` ``cromch`` ``meow`` ``food`` ``crafts`` ``pareidolia`` ``confusingperspective``  ``artbreeder`` ``mildlyinteresting`` ``wtfstock`` ``meme`` ``wtfstock`` ``itookapicture`` ``psbattles`` ``cozyplaces`` ``battlestations`` ``art`` ``architecture``', inline=False)
    embed.add_field(name='NSFW :underage:', value='``waifunsfw`` ``erofeet`` ``feet`` ``femdom`` ``nekonsfw`` ``nekolewd`` ``fourK`` ``blowjob`` ``nsfw_avatar`` ``fuck`` ``yuri`` ``hentai`` ``cum`` ``boobs`` ``lewd`` ``pussy``', inline=False)
    embed.add_field(name='Economia :coin:', value='``inventory`` ``work`` ``pay`` ``bal`` ``shop`` ``buy`` ``sell`` ``rob`` ``withdraw`` ``dep`` ``slots``', inline=False)
    embed.add_field(name='Discord Together :video_camera:', value='``startyt`` ``startchess`` ``startpoker`` ``startbetrayal`` ``startfishing``', inline=True)
    embed.add_field(name='This X Does Not Exist :astonished:', value='``person`` ``artwork`` ``catnot``', inline=True)
    embed.set_footer(text=f'Pedido Por {ctx.author}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("✅")


import numpy














@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='person', aliases=['thispersondoesnotexist', 'personnotexist', 'this_person_does_not_exist', 'this-person-does-not-exist', 'Person'])
async def person(ctx):
    embed = discord.Embed(
        title='Esta Persona No Existe', url="https://thispersondoesnotexist.com", colour=random.randint(0, 16777216), type="image")
    embed.set_image(
        url=f"https://thispersondoesnotexist.com/image?cum={numpy.random.rand()}")
    embed.set_footer(text=f'Pedido Por {ctx.author}', icon_url=ctx.author.avatar_url)
    await ctx.send(content=None, embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='artwork', aliases=['Artwork'])
async def artwork(ctx):
    embed = discord.Embed(
        title='Esta Obra No Existe', url="https://thisartworkdoesnotexist.com", colour=random.randint(0, 16777216), type="image")
    embed.set_image(
        url=f"https://thisartworkdoesnotexist.com/?cum={numpy.random.rand()}")
    await ctx.send(content=None, embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='catnot', aliases=['Catnot'])
async def catnot(ctx):
    embed = discord.Embed(
        title='Este Gato no Existe', url="https://thiscatdoesnotexist.com", colour=random.randint(0, 16777216), type="image")
    embed.set_image(
        url=f"https://thiscatdoesnotexist.com/?cum={numpy.random.rand()}")
    await ctx.send(content=None, embed=embed)














@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Calc"])
async def calc(ctx:discord.Message):
    def genEmbed(calc):
        em=Embed(title=f"Calculadora de {ctx.author.display_name} ",description=f"```-                              {calc}```",color=discord.Color.teal())
        return em
    exit=False

    calculation=""
    msg=await ctx.send(
        embed=genEmbed("0"),
        components = [
            [Button(label="1"),Button(label="2"),Button(label="3"),Button(label="4"),Button(label="5")],
            [Button(label="6"),Button(label="7"),Button(label="8"),Button(label="9"),Button(label="8")],
            [Button(label="9" ),Button(label="0"),Button(label="."),Button(label="Done",style=ButtonStyle.red),Button(label="Clear",style=ButtonStyle.green)],
            [Button(label="/",style=ButtonStyle.blue),Button(label="+",style=ButtonStyle.blue),Button(label="-",style=ButtonStyle.blue),Button(label="x",style=ButtonStyle.blue),Button(label="=",style=ButtonStyle.blue)]
        ]
    )

    while not exit:
        i=await bot.wait_for("button_click")
        if i.user==ctx.author:
            label=i.component.label
            if label=="=":
                try:
                    calculation=str(eval(calculation))
                    await msg.edit(embed=genEmbed(calculation))
                except:
                    await msg.edit(embed=genEmbed("Syntax Error"))
            elif label=="Done":
                exit=True
            elif label=="Clear":
                calculation=""
                await msg.edit(embed=genEmbed("0"))
            else:
                calculation+=i.component.label
                await msg.edit(embed=genEmbed(calculation))
            await i.respond(type=6)
        else:
            await i.respond(f"That isn't your calculator! Get your own with {bot.command_prefix}calc")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Clicker"])
async def clicker(ctx):
    exit=False
    num=0
    print(f"{ctx.author} Uso >clicker")
    msg=await ctx.send(
        "0",
        components=[
            [Button(label="+",style=ButtonStyle.green),Button(label="-",style=ButtonStyle.blue),Button(label="Reset"),Button(label="Hecho",style=ButtonStyle.red)]
        ]
    )
    while not exit:
        i=await bot.wait_for("button_click")
        label=i.component.label
        if label=="+":
            num+=1
        elif label=="-":
            num-=1
        elif label=="Reset":
            num=0
        elif label=="Hecho":
            exit=True
        await msg.edit(content=str(num))
        await i.respond(type=6)











@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Startyt"])
async def startyt(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Haz click en el ``LINK AZUL``!\n{link}")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Startchess"])
async def startchess(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
    await ctx.send(f"Haz click en el ``LINK AZUL``!\n{link}")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Startpoker"])
async def startpoker(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
    await ctx.send(f"Haz click en el ``LINK AZUL``!\n{link}")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Startbetrayal"])
async def startbetrayal(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
    await ctx.send(f"Haz click en el ``LINK AZUL``!\n{link}")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Startfishing"])
async def startfishing(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
    await ctx.send(f"Haz click en el ``LINK AZUL``!\n{link}")




























@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        em = discord.Embed(title=f"Cuida tu teclado!",description=f"Pruebalo denuevo en: {error.retry_after:.2f}s.")
        await ctx.send(embed=em)

@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title='Flarot', color=0xaa0000)
    embed.add_field(name="Hola mundo!. Llegue, soy Flarot", value='\nEscribe >ayuda para ver mis comandos!', inline=False)
    embed.set_footer(text='Gracias por añadirme!')
    await guild.system_channel.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandNotFound):
        embed = discord.Embed(title=f"Comando no Encontrado.",description="Usa `>ayuda` para una lista de comandos disponibles.",)
        await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.GuildNotFound):
        embed = discord.Embed(title=f"Servidor no Encontrado",description="O colocaste mal el nombre, O no estoy en ese servidor. Servidor: {argument}",)
        await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.MemberNotFound):
        embed = discord.Embed(title=f"Miembro no Encontrado",description="No encuentro a ese Miembro en cuestion. Miembro: {argument}",)
        await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.MissingPermissions):
        embed = discord.Embed(title=f"Permisos Insuficientes",description="No tengo permisos para hacer esa accion, Permisos que me faltan: {missing_perms}",)
        await ctx.send(embed=embed)    

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.NSFWChannelRequired):
        embed = discord.Embed(title=f"NSFW",description="Ah... Este canal debe ser uno nsfw...",)
        await ctx.send(embed=embed)  

@bot.event
async def on_message(message):
  if isinstance(message.channel, discord.DMChannel):
    embed = discord.Embed(colour=0xa5a5ed)
    hi = message.content
    member = message.author
    logchannel = bot.get_channel(849348693144502282)
    embed.add_field(name=f'Este MD fue enviado por {member} a el bot!', value=hi)
    await logchannel.send(embed=embed)
  await bot.process_commands(message)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def submit(ctx, *, message):
    embedVar = discord.Embed(title=f"Idea por {ctx.author}",
                             description=message,
                             colour=discord.Color.purple())
    await ctx.send("Tu Idea a sido enviada!")
    channel = bot.get_channel(850179951302017046)
    msg = await channel.send(embed=embedVar)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")

#█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
#█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
#█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
#█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
#█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
#█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
#█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████████████░░▄▀░░█
#█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
#█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█ y NSFW XD y tambien anime mucho.
#█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='findAnime', aliases=["Findanime","FindAnime","findanime"])
async def findAnime(ctx, anime_name: str, base_url: str = gogo_scraper.BASE_URL):

    """
    Uses Gogoanime's (limited) search functionality to find the exact anime or anime the user wants to get info about.
    This is required because the other functions in this bot require the user to input the exact title used in Gogoanime.
    :param anime: Search query
    :param base_url: Base Gogoanime URL. Useful if the current default URL gets taken down
    :return: Iteratively outputs search results to discord chat
    """

    search = gogo_scraper.search(anime_name, base_url)

    if (search is None) or (len(search) == 0):
        await ctx.send(f'Lastimosamente, No he encontrado nada...')
        return

    for res in search:
        anime = res
        output = f'''
                Este es un resultado:
                **Titulo:** {anime['name']}
                {anime['released']}
                **Link:** {anime['link']}
                '''
        await ctx.send(output)

        await ctx.send('\nEste es el anime correcto? (Escribe "si", Una letra o una palabra hara que pare este comando)')
        msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        msg = str(msg.content).lower()

        if msg == 'si' or msg == 'yeah' or msg == 'yup':
            break
        else:
            await ctx.send('Buscando Siguiente Resultado..')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Cringeanime"])
async def cringanime(ctx):
    async with aiohttp.ClientSession() as cringe:
        async with cringe.get(f'https://api.waifu.pics/sfw/cringe') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'{factdata["url"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Waifu"])
async def waifu(ctx):
    async with aiohttp.ClientSession() as waifu:
        async with waifu.get(f'https://api.waifu.pics/sfw/waifu') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'{factdata["url"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Neko"])
async def neko(ctx):
    async with aiohttp.ClientSession() as neko:
        async with neko.get(f'https://api.waifu.pics/sfw/neko') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'{factdata["url"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='pat', aliases=["Pat"]) 
async def pat(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://nekos.life/api/v2/img/pat').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " ha acariciado a alguien"
            else:
                embeddescription = str(ctx.author.mention) + " Acaricia a  " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='poke', aliases=["Poke"]) 
async def poke(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('http://api.nekos.fun:8080/api/poke').json()
            imagegif = imagegif['image']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Molesta a alguien. "
            else:
                embeddescription = str(ctx.author.mention) + " Molesta a" + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='hug', aliases=['abrazo', 'Abrazo', 'ABRAZO', 'aBRAZO', 'abrazO', 'abrAzo']) 
async def hug(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://nekos.life/api/v2/img/hug').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Tiene esquizofrenia. "
            else:
                embeddescription = str(ctx.author.mention) + " Abrazo a " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='bored') 
async def bored(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://nekos.best/api/v1/bored').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Se aburrio "
            else:
                embeddescription = str(ctx.author.mention) + " Se aburrio de " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='cry') 
async def cry(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://nekos.best/api/v1/cry').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Llora "
            else:
                embeddescription = str(ctx.author.mention) + " Llora por culpa de " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un error ha ocurrido", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Laugh"])
async def laugh(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('http://api.nekos.fun:8080/api/laugh').json()
            imagegif = imagegif['image']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Se rio"
            else:
                embeddescription = str(ctx.author.mention) + " Se rio de " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un Error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un Error ha ocurrido ", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Dance"])
async def dance(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://api.waifu.pics/sfw/dance').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Comenzo a Bailar"
            else:
                embeddescription = str(ctx.author.mention) + " Bailo con " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un Error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un Error ha ocurrido ", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Kill"])
async def kill(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://api.waifu.pics/sfw/kill').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Ha sido Asesinado"
            else:
                embeddescription = str(ctx.author.mention) + " Asesino a " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un Error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un Error ha ocurrido ", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Wink"])
async def wink(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://api.waifu.pics/sfw/wink').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Guiño el Ojo"
            else:
                embeddescription = str(ctx.author.mention) + " Le Guiño a " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un Error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un Error ha ocurrido ", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Bite"])
async def bite(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://api.waifu.pics/sfw/bite').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Se Mordio"
            else:
                embeddescription = str(ctx.author.mention) + " Mordio a " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un Error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un Error ha ocurrido ", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Highfive"])
async def highfive(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://api.waifu.pics/sfw/highfive').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Choco los Cinco"
            else:
                embeddescription = str(ctx.author.mention) + " Choco los Cinco con " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un Error ha ocurrido", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un Error ha ocurrido ", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Slap"])
async def slap(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://nekos.life/api/v2/img/slap').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Se pego.. "
            else:
                embeddescription = str(ctx.author.mention) + " Golpeo fuerte a " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="error", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="error lol ", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="baka", aliases=["Baka"])
async def baka(ctx, user: discord.User):
    NEKO_URL = "https://nekos.life/api/v2/img/baka"
    neko = requests.get(NEKO_URL).json()
    embed = discord.Embed(title="Estupido!", description= "**" + ctx.message.author.name + " llamo a " + str(user.name) + " estupido!**")
    embed.set_image(url=neko['url'])
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Punch"])
async def punch(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            randgif = random.randint(0, 16)
            imagegif = "https://kurobot.pw/gifs/punch/" + str(randgif) + ".gif"
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Se Golpeo a el mismo. (¿Le pasa algo?)"
            else:
                embeddescription = str(ctx.author.mention) + " ha golpeado a " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un error a ocurrido.", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un error ha ocurrido.", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Kiss"])
async def kiss(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            imagegif = requests.get('https://nekos.life/api/v2/img/kiss').json()
            imagegif = imagegif['url']
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " Tiene Ezquizofrenia"
            else:
                embeddescription = str(ctx.author.mention) + " le ha dado un beso a" + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Un error ha ocurrido.", color=0xffa500)
            embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Un error ha ocurrido.", color=0xffa500)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)








@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="fuck", aliases=["Fuck"])
async def fuck(ctx, user: discord.User):

    if ctx.channel.is_nsfw():
        NEKO_URL = "https://nekos.life/api/v2/img/anal"
        neko = requests.get(NEKO_URL).json()
        embed = discord.Embed(title="Follada", description= "**" + ctx.message.author.name + " follo a " + str(user.name) + "**")
        embed.set_image(url=neko['url'])

        await ctx.send(embed=embed)
    
    else:
        await ctx.send("Este comando es para canales NSFW!")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Nsfw_avatar"])
async def nsfw_avatar(ctx):
    if ctx.channel.nsfw == True:
        apiout = requests.get('https://nekos.life/api/v2/img/nsfw_avatar').json()
        apiout = apiout['url']
        embed = discord.Embed(color = 0xffa500, title=str("Avatar NSFW"))
        embed.set_image(url=str(apiout))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Fourk","FourK","fourk"])
async def fourK(ctx):
    if ctx.channel.nsfw == True:
        apiout = requests.get('http://api.nekos.fun:8080/api/4k').json()
        apiout = apiout['image']
        embed = discord.Embed(color = 0xffa500, title=str("4K"))
        embed.set_image(url=str(apiout))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Hentai"])
async def hentai(ctx):
    if ctx.channel.nsfw == True:
        apiout = requests.get('https://nekos.life/api/v2/img/hentai').json()
        apiout = apiout['url']
        embed = discord.Embed(color = 0xffa500, title=str("Hentai"))
        embed.set_image(url=str(apiout))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="blowjob", aliases=["Mamada","mamada","Blowjob"])
async def blowjob(ctx, user: discord.User):

    if ctx.channel.is_nsfw():
        NEKO_URL = "https://nekos.life/api/v2/img/blowjob"
        neko = requests.get(NEKO_URL).json()
        embed = discord.Embed(title="Blowjob", description= "**" + ctx.message.author.name + " Se folla a " + str(user.name) + "!!!!**")
        embed.set_image(url=neko['url'])
        await ctx.send(embed=embed)

    else:
        await ctx.send("Este comando es solo para canales NSFW!!!")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Nekonsfw"])
async def nekonsfw(ctx):
    if ctx.channel.is_nsfw():
        async with aiohttp.ClientSession() as nekonsfw:
            async with nekonsfw.get(f'https://api.waifu.pics/nsfw/neko') as jsondata:
                if not (300 > jsondata.status >= 200):
                    await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
                else:
                    factdata = await jsondata.json()
                    await ctx.send(f'{factdata["url"]}')
    else:
        await ctx.send("Debe ser un canal nsfw :underage:")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Waifunsfw"])
async def waifunsfw(ctx):
    if ctx.channel.is_nsfw():
        async with aiohttp.ClientSession() as waifunsfw:
            async with waifunsfw.get(f'https://api.waifu.pics/nsfw/waifu') as jsondata:
                if not (300 > jsondata.status >= 200):
                    await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
                else:
                    factdata = await jsondata.json()
                    await ctx.send(f'{factdata["url"]}')
    else:
        await ctx.send("Debe ser un canal nsfw")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Yuri"])
async def yuri(ctx):
    if ctx.channel.nsfw == True:
        apiout = requests.get('https://nekos.life/api/v2/img/yuri').json()
        apiout = apiout['url']
        embed = discord.Embed(color = 0xffa500, title=str("Yuri para ti!:"))
        embed.set_image(url=str(apiout))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Cum"])
async def cum(ctx):
    if ctx.channel.nsfw == True:
        apiout = requests.get('https://nekos.life/api/v2/img/cum').json()
        apiout = apiout['url']
        embed = discord.Embed(color = 0xffa500, title=str(f"{ctx.author} Se ha venido."))
        embed.set_image(url=str(apiout))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Boobs"])
async def boobs(ctx):
    if ctx.channel.nsfw == True:
        apiout = requests.get('https://nekos.life/api/v2/img/boobs').json()
        apiout = apiout['url']
        embed = discord.Embed(color = 0xffa500, title=str(f"{ctx.author} Muestra sus T E T A S"))
        embed.set_image(url=str(apiout))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Lewd"])
async def lewd(ctx):
    if ctx.channel.nsfw == True:
        apiout = requests.get('https://nekos.life/api/v2/img/lewd').json()
        apiout = apiout['url']
        embed = discord.Embed(color = 0xffa500, title=str("LEWD"))
        embed.set_image(url=str(apiout))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Pussy"])
async def pussy(ctx):
    if ctx.channel.nsfw == True:
        apiout = requests.get('https://nekos.life/api/v2/img/pussy').json()
        apiout = apiout['url']
        embed = discord.Embed(color = 0xffa500, title=str("Pussy"))
        embed.set_image(url=str(apiout))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Femdom"])
@commands.is_nsfw()
async def femdom(ctx):
  r = requests.get("https://nekos.life/api/v2/img/femdom")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Lewdneo"])
@commands.is_nsfw()
async def lewdneko(ctx):
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Erofeet"])
@commands.is_nsfw()
async def erofeet(ctx): 
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Feet"])
@commands.is_nsfw()
async def feet(ctx): 
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

#█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
#█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
#█░░▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
#███░░▄▀░░███░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
#███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
#███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#███░░▄▀░░███░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
#███░░▄▀░░███░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████████████░░▄▀░░█
#█░░░░▄▀░░░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
#█░░▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
#█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Mineach"])
async def mineach(ctx, text: str, icon = None): 
    """Displays a minecraft achievemt"""
    image = await alex_api.achievement(text=text, icon=icon)
    image_bytes = await image.read()
    file = discord.File(image_bytes, "achievement.png")
    await ctx.send(f"`Rendered by {ctx.author}`", file=file)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Randompic"])
async def randompic(ctx):
    urls = ['https://source.unsplash.com/random', 'https://picsum.photos/500/500']
    url = random.choice(urls)
    img = requests.get(url)
    embed= discord.Embed(title="Random Pic")
    embed.set_image(url=img.url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Randomgif"])
async def randomgif(ctx,*,q="Gif Aleatorio De Giphy"):

    api_key="8GmsLsqD3D0wQy8faf8gXieqSvPRUzIx"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Trump"])
async def trump(ctx, *, msg):
    msg = msg.replace(" ", "%20")
    url = 'https://api.no-api-key.com/api/v2/trump?message=' + msg
    embed = discord.Embed(title="¡Tweet importante!", color=0xff00ff)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Captcha"])
async def captcha(ctx, *, msg):
    msg = msg.replace(" ", "%20")
    url = 'https://api.no-api-key.com/api/v2/recaptcha?text=' + msg
    embed = discord.Embed(title="¡Captcha importante!", color=0xff00ff)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["rhash", "robothash", "rh", "rohash"])
async def robohash(ctx: Context, *, meme: str) -> None:
    """Text => robot image thing."""
    try:
        embed = Embed(colour=0x690E8)
        meme = urllib.parse.quote_plus(meme)
        embed.set_image(url=f"https://robohash.org/{meme}.png")
        await ctx.send(embed=embed)
    except Exception as error:
        await ctx.send(f"Algo Fallo [{error}]")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Deepfry"])
async def deepfry(ctx):
    try:
        thename = ctx.message.attachments[0].filename
        deep = "deep_" + str(thename)
        await ctx.message.attachments[0].save(thename)

        img = Image.open(thename)
        theimg = deepfried(img)

        theimg.save(deep)

        mainFile = discord.File(deep)

        await ctx.send("Here you go.", file=mainFile) 

    except:
        await ctx.send("I need an attached file to make this work 🤡")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Mapacheqp"])
async def mapacheqp(ctx, member:discord.Member=None):
    if not member:
        member = ctx.author
    
    qp = Image.open('mapacheqp.png')

    asset = member.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((120, 205))

    qp.paste(pfp, (233, 36))

    qp.save('results/mapacheqpp.png')

    await ctx.send(file = discord.File('results/mapacheqpp.png'))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Discovered"])
async def discovered(ctx, member:discord.Member=None):
    if not member:
        member = ctx.author
    
    discovered = Image.open('discovered.jpg')

    asset = member.avatar_url_as(size=4096)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((151, 151))

    discovered.paste(pfp, (80, 700))

    discovered.save('results/pdiscovered.jpg')

    await ctx.send(file = discord.File('results/pdiscovered.jpg'))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Bob NOOOO``", aliases=["Bobburns"])
async def bobburns(ctx, member:discord.Member=None):
    if not member:
        member = ctx.author
    
    bobburns = Image.open('bobburns.jpg')

    asset = member.avatar_url_as(size=2048)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((140, 200))

    bobburns.paste(pfp, (70, 100))

    bobburns.save('results/pbobburns.jpg')

    await ctx.send(file = discord.File('results/pbobburns.jpg'))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Descansa en paz...``", aliases=["Rip"])
async def rip(ctx, member:discord.Member=None):
    if not member:
        member = ctx.author
    
    rip = Image.open('rip.jpg')

    asset = member.avatar_url_as(size=2048)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((1140, 1110))

    rip.paste(pfp, (267, 1170))

    rip.save('results/prip.jpg')

    await ctx.send(file = discord.File('results/prip.jpg'))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Haz que seas el mas buscado``", aliases=["Wanted"])
async def wanted(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author
    
    wanted = Image.open("wanted.jpg")
    
    asset = member.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    profilepic = Image.open(data)

    profilepic = profilepic.resize((300, 300))
    
    wanted.paste(profilepic, (78, 219))

    wanted.save("results/wantedpic.jpg")

    await ctx.send(file = discord.File("results/wantedpic.jpg"))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Sus.``", aliases=["Sus"])
async def sus(ctx, member: discord.Member=None):
    if not member:
        member = ctx.author
        
    impostor = random.choice(['true', 'false'])
    apikey = 'vYXepVrpXcRxyM42G1lVvv4dg'
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://some-random-api.ml/premium/amongus?username={member.name}&avatar={member.avatar_url_as(format='png')}&impostor={impostor}&key={apikey}") as resp:
            if 300 > resp.status >= 200:
                fp = io.BytesIO(await resp.read())
                
                await ctx.reply(file=discord.File(fp, 'amogus.gif'))
            else:
                await ctx.reply('Couldnt get image :(')
            
            await session.close()

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Tarjeta Horny``", aliases=["Horny"])
async def horny(ctx, member: discord.Member = None):
        '''Licencia Horny, ¡solo para ti!'''
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
         async with session.get(
            f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png")}'
        ) as af:
            if 300 > af.status >= 200:
                fp = io.BytesIO(await af.read())
                file = discord.File(fp, "horny.png")
                em = discord.Embed(
                    title="Ten tu tarjeta Horny, Cuidala eh. (～￣▽￣)～",
                    color=0xf1f1f1,
                )
                em.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
                em.set_image(url="attachment://horny.png")
                await ctx.send(embed=em, file=file)
            else:
                await ctx.send('No horny :(')
            await session.close()

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``**Enojo**``", aliases=["Triggered"])
async def triggered(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as wastedSession:
        async with wastedSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await wastedImage.read()) # read the image/bytes
            
            await wastedSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'triggered.gif')) # sending the file

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Efecto Sepia``", aliases=["Sepia"])
async def sepia(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as aeeeeaSession:
        async with aeeeeaSession.get(f'https://some-random-api.ml/canvas/sepia?avatar={member.avatar_url_as(format="png", size=1024)}') as aeeeeaImage: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await aeeeeaImage.read()) # read the image/bytes
            
            await aeeeeaSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'sepia.png')) # sending the file

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Escale de grey inversa``", aliases=["Invertgreyscale"])
async def invertgreyscale(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as aeeeeSession:
        async with aeeeeSession.get(f'https://some-random-api.ml/canvas/greyscale?avatar={member.avatar_url_as(format="png", size=1024)}') as aeeeeImage: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await aeeeeImage.read()) # read the image/bytes
            
            await aeeeeSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'invertgreyscale.png')) # sending the file

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Haz que tu avatar use la escala de grey. XD``", aliases=["Greyscale"])
async def greyscale(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as aeeeSession:
        async with aeeeSession.get(f'https://some-random-api.ml/canvas/greyscale?avatar={member.avatar_url_as(format="png", size=1024)}') as aeeeImage: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await aeeeImage.read()) # read the image/bytes
            
            await aeeeSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'greyscale.png')) # sending the file

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``LGTBASDFGHJKL+#$) y mas letras moment``", aliases=["Rainbow"])
async def rainbow(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as aeSession:
        async with aeSession.get(f'https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format="png", size=1024)}') as aeImage: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await aeImage.read()) # read the image/bytes
            
            await aeSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'gay.png')) # sending the file

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Coloca una clase de vidrio. en tu avatar``", aliases=["Glass"])
async def glass(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as aSession:
        async with aSession.get(f'https://some-random-api.ml/canvas/glass?avatar={member.avatar_url_as(format="png", size=1024)}') as aImage: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await aImage.read()) # read the image/bytes
            
            await aSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'glass.png')) # sending the file

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Muerto...``", aliases=["Gtawasted"])
async def gtawasted(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as wastedSession:
        async with wastedSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await wastedImage.read()) # read the image/bytes
            
            await wastedSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'wasted.png')) # sending the file

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Pikachu"])
async def pikachu(ctx):
	async with ctx.channel.typing():
		async with aiohttp.ClientSession() as cs:
			async with cs.get("https://some-random-api.ml/img/pikachu") as r:
				data = await r.json()

				embed = discord.Embed(title=f"PI-KA-CHUUU", colour=0x6FB900)
				embed.set_image(url=data['link'])
                
				await ctx.send(embed=embed)

#█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
#█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
#█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
#█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████
#█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
#█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
#█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████████████░░▄▀░░█
#█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█
#█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
#█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Datos sobre Perros``", aliases=["Dogfact"])
async def dogfact(ctx):
    async with aiohttp.ClientSession() as dogsession:
        async with dogsession.get(f'https://some-random-api.ml/facts/dog') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'Facts about dogs: {factdata["fact"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Fotos de Perros``",aliasses=["Dog"])
async def dog(ctx):
    response = requests.get('https://random.dog/woof.json?ref=apilist.fun')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9910, title='Foto de Perros:')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Datos sobre Gatos``", aliases=["Catfact"])
async def catfact(ctx):
    async with aiohttp.ClientSession() as catsession:
        async with catsession.get(f'https://meowfacts.herokuapp.com/') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'Facts about cats: {factdata["data"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Fotos de Gatos``", aliases=["Cat"])
async def cat(ctx):
    response = requests.get('https://aws.random.cat/meow')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9910, title='Foto de Gatos:')
    embed.set_image(url=json_data['file'])
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Datos sobre Pandas``", aliases=["Pandafact"])
async def pandafact(ctx):
    async with aiohttp.ClientSession() as pandasession:
        async with pandasession.get(f'https://some-random-api.ml/facts/panda') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'Facts about Pandas: {factdata["fact"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Fotos de Pandas Rojos``", aliases=["Redpanda"])
async def redpanda(ctx):
    response = requests.get('https://some-random-api.ml/img/red_panda')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9910, title='Foto de Pandas Rojos:')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Fotos de Pandas``", aliases=["Panda"])
async def panda(ctx):
    response = requests.get('https://some-random-api.ml/img/panda')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9910, title='Foto de Pandas:')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Datos sobre Zorros``", aliases=["Foxfact"])
async def foxfact(ctx):
    async with aiohttp.ClientSession() as foxsession:
        async with foxsession.get(f'https://some-random-api.ml/facts/fox') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'Facts about Foxes: {factdata["fact"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Fotos de Zorros``", aliases=["Fox"])
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9910, title='Foto de Zorros:')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Datos sobre Koalas``", aliases=["Koalafact"])
async def koalafact(ctx):
    async with aiohttp.ClientSession() as koalasession:
        async with koalasession.get(f'https://some-random-api.ml/facts/koala') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'Facts about Koalas: {factdata["fact"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Fotos de Koalas``", aliases=["Koala"])
async def koala(ctx):
    response = requests.get('https://some-random-api.ml/img/koala')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9910, title='Foto de Koalas:')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')

#███████████████████████████████████████████████████████████████████████████████████████████
#█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░███░░░░░░░░░░█░░░░░░░░░░░░░░█
#█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░░░▄▀░░░░█░░░░░░▄▀░░░░░░█
#█░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████
#█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████
#█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████
#█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████
#█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████
#█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░░░▄▀░░░░█████░░▄▀░░█████
#█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀░░█████░░▄▀░░█████
#█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░███░░░░░░░░░░█████░░░░░░█████
#███████████████████████████████████████████████████████████████████████████████████████████

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def cursed(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/Cursed_Images.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/Cursed_Images! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Meme"])
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/memes.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/memes! | Meme pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["MidlyInteresting","MI", "mi"])
async def mildyinteresting(ctx):
    async with aiohttp.ClientSession() as cc:
        async with cc.get("https://www.reddit.com/r/mildlyinteresting.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/mildyinteresting! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["ArtBreeder","Artbreeder"])
async def artbreeder(ctx):
    async with aiohttp.ClientSession() as c:
        async with c.get("https://www.reddit.com/r/ArtBreeder.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/ArtBreeder! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Crafts"])
async def crafts(ctx):
    async with aiohttp.ClientSession() as coda:
        async with coda.get("https://www.reddit.com/r/crafts.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.green()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/crafts! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Internetisart", "IIA"])
async def internetisart(ctx):
    async with aiohttp.ClientSession() as copsa:
        async with copsa.get("https://www.reddit.com/r/hmmm.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/hmmm! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Meow"])
async def meow(ctx):
    async with aiohttp.ClientSession() as copsaw:
        async with copsaw.get("https://www.reddit.com/r/MEOW_IRL.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/MEOW_IRL! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Psbattles","PSB"])
async def psbattles(ctx):
    async with aiohttp.ClientSession() as cops:
        async with cops.get("https://www.reddit.com/r/photoshopbattles.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/photoshopbattles! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Pareidolia"])
async def pareidolia(ctx):
    async with aiohttp.ClientSession() as coda:
        async with coda.get("https://www.reddit.com/r/pareidolia.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/pareidolia! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Confusingperspective","cp","CP","Cp"])
async def confusingperspective(ctx):
    async with aiohttp.ClientSession() as cp:
        async with cp.get("https://www.reddit.com/r/confusing_perspective.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/confusing_perspective! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Wtfstock","WS","ws","Ws"])
async def wtfstock(ctx):
    async with aiohttp.ClientSession() as csd:
        async with csd.get("https://www.reddit.com/r/wtfstockphotos.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/wtfstockphotos! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Food"])
async def food(ctx):
    async with aiohttp.ClientSession() as cod:
        async with cod.get("https://www.reddit.com/r/food.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/food! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Aww"])
async def aww(ctx):
    async with aiohttp.ClientSession() as caw:
        async with caw.get("https://www.reddit.com/r/cute.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/cute! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def itookapicture(ctx):
    async with aiohttp.ClientSession() as aw:
        async with aw.get("https://www.reddit.com/r/itookapicture.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/itookapicture! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["CozyPlaces","Cozyp"])
async def cozyplaces(ctx):
    async with aiohttp.ClientSession() as cozy:
        async with cozy.get("https://www.reddit.com/r/CozyPlaces.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/cozyplaces! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Battlestations","BS","Bs","bS"])
async def battlestations(ctx):
    async with aiohttp.ClientSession() as cozy:
        async with cozy.get("https://www.reddit.com/r/battlestations.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/battlestations! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Art"])
async def art(ctx):
    async with aiohttp.ClientSession() as ar:
        async with ar.get("https://www.reddit.com/r/art.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/art! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Architecture"])
async def architecture(ctx):
    async with aiohttp.ClientSession() as arti:
        async with arti.get("https://www.reddit.com/r/ArchitecturePorn.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/architectureporn! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Japan"])
async def japan(ctx):
    async with aiohttp.ClientSession() as copsadaeej:
        async with copsadaeej.get("https://www.reddit.com/r/japanpics.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/japanpics! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Nature"])
async def nature(ctx):
    async with aiohttp.ClientSession() as copsadaee:
        async with copsadaee.get("https://www.reddit.com/r/natureporn.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/natureporn! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Axolotls"])
async def axolotls(ctx):
    async with aiohttp.ClientSession() as copsadae:
        async with copsadae.get("https://www.reddit.com/r/axolotls.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/axolotls! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Catmemes", "CatMemes", "CM"])
async def catmemes(ctx):
    async with aiohttp.ClientSession() as copsade:
        async with copsade.get("https://www.reddit.com/r/catmemes.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/Catmemes! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Cromch"])
async def cromch(ctx):
    async with aiohttp.ClientSession() as copsad:
        async with copsad.get("https://www.reddit.com/r/cromch.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            embed.set_footer(text=f"Proveniente de r/cromch! | Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.worldvectorlogo.com/logos/reddit-4.svg') 
            await ctx.send(embed=embed)

#██████████████████████████████████████████████
#█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
#█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░▄▀░░░░░░░░░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█
#█░░▄▀░░█████████████░░▄▀░░█████░░▄▀░░█████████
#█░░▄▀░░░░░░░░░░█████░░▄▀░░█████░░▄▀░░█████████
#█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀░░█████████
#█░░▄▀░░░░░░░░░░█████░░▄▀░░█████░░▄▀░░█████████
#█░░▄▀░░█████████████░░▄▀░░█████░░▄▀░░█████████
#█░░▄▀░░░░░░░░░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░█
#█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█
#█░░░░░░░░░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░█
#██████████████████████████████████████████████


@bot.event
async def on_message_delete(message):
  global snipe_message_content
  global snipe_message_author

  snipe_message_content = message.content
  snipe_message_author = message.author.name

@bot.command(aliases=['sp'])
async def snipe(message):
  if snipe_message_content==None:
    await message.channel.send("Nada para Mostrar!")
  else:
      embed = discord.Embed(description=f"{snipe_message_content}")
      embed.set_footer(text=f"Pedido por {message.author.name}#{message.author.discriminator}")
      embed.set_author(name=f"Mensaje de: {snipe_message_author}")
      await message.channel.send(embed=embed)
      return

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Howgay"])
async def howgay(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "{0.name} es {1}% gay!".format(member, rand))
  em.set_footer(text = "Flarot")
  await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Howchad"])
async def howchad(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "{0.name} es {1}% chad!".format(member, rand))
  em.set_footer(text = "Flarot")
  await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Howstupid"])
async def howstupid(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "{0.name} es {1}% estupido".format(member, rand))
  em.set_footer(text = "Flarot")
  await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Howvirgin"])
async def howvirgin(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "{0.name} es {1}% virgen!".format(member, rand))
  em.set_footer(text = "Flarot")
  await ctx.send(embed=em)


@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Ping"])
async def ping(ctx):
    testmsg = await ctx.send("Working...")
    await testmsg.delete()
    embed = discord.Embed(color = 0xffa500, title="Pong, " + str(ctx.author.name) + "!")
    embed.add_field(name="ws/API Latency:", value=str(round(bot.latency, 5)) + "s", inline=False)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Flarot", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="flip", aliases=["Flip"])
async def flip(ctx):
    face=randint(0,1)
    e = discord.Embed()
    e.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/612394933294202891/646386235635662849/girl-concentration-composure-coin-toss-wallpaper-preview.png')
    if face == 0:
        e.add_field(name='Que tocara...', value='Cruz!')
    else:
        e.add_field(name='Que tocara...', value='Cara!')
    await ctx.send(embed=e)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Avatar"])
async def avatar(ctx):

    args = ctx.message.content.split(" ")[1:]
    
    embed = discord.Embed()
    embed.colour = discord.Color.from_rgb(0, 255, 255)

    if len(args) == 0:
        embed.title = ctx.author.name
        embed.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    
    elif len(ctx.message.mentions) > 0:
        for member in ctx.message.mentions:
            embed.title = member.name
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)
    
    elif args[0] in ("server", "guild"):
        embed.title = ctx.guild.name
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    else:
        embed.title = "avatar"
        embed.description = f"Muestra tu avatar, de los usuarios mencionados o del servidor."
        embed.add_field(name="Uso:", value=f"{bot}avatar\n{bot}avatar @user1, @user2, ...\n{bot}avatar server", inline=False)
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Say"])
@commands.has_permissions(administrator=True)
async def say(ctx, *, arg):
  await ctx.message.delete()
  new = arg
  if '@everyone' in arg:
    new = arg.replace('@everyone', '')
  await ctx.send(new)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Crea un Embed.``", aliases=["Embed"])
@commands.has_permissions(administrator=True)
async def embed(ctx, *, arg):
  await ctx.message.delete()
  embed=discord.Embed(description=arg, color=0xff5129)
  await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=['8ball','8b']) 
async def _8ball(ctx, *, question):
    response = ['En mi opinión, sí',
                'Es cierto',
                'Es decididamente así',
                'Probablemente',
                'Buen pronóstico',
                'Todo apunta a que sí',
                'Sin duda',
                'Sí',
                'Sí - definitivamente',
                'Debes confiar en ello',
                'Respuesta vaga, vuelve a intentarlo',
                'Pregunta en otro momento',
                'Será mejor que no te lo diga ahora',
                'No puedo predecirlo ahora',
                'Concéntrate y vuelve a preguntar',
                'Puede ser',
                'No cuentes con ello',
                'Mi respuesta es no',
                'Mis fuentes me dicen que no',
                'Las perspectivas no son buenas',
                'Muy dudoso'] # Frases de respuestas que quieres que el bot responda
    _8ball_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
    _8ball_embed.add_field(name="Comando 8ball | :8ball:", value=f"**Pregunta:** {question}\n**Respuesta:** {random.choice(response)}") # Aqui es como quieres que sea su respuesta
    await ctx.send(embed=_8ball_embed) # Enviamos Respuesta

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Trivia"])
async def trivia(ctx):
    async with aiohttp.ClientSession() as trivia:
        
        async with trivia.get(f'https://triviapi.elfedeclips.repl.co/') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                messagedata = await jsondata.json()
                
                
            await ctx.send(f'Pregunta!: {messagedata["question"]} {messagedata["image"]} {messagedata["answers"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(help="``Trump piensa..``", aliases=["Trumpthinks","TT"])
async def trumpthinks(ctx):
    async with aiohttp.ClientSession() as trump:
        async with trump.get(f'https://api.whatdoestrumpthink.com/api/v1/quotes/random') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                messagedata = await jsondata.json()
                
            await ctx.send(f'Trump thinks..: {messagedata["message"]}')

            await ctx.send(file = discord.File("trumpthinks.jpg"))

@bot.command(aliases=["Tinyurl", "TU"])
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Link Acortado', value=r, inline=False )
    await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x004c86)
    await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["YoN","YON"])
async def yesorno(ctx):
    async with aiohttp.ClientSession() as yesorno:
        async with yesorno.get(f'https://yesno.wtf/api') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'{factdata["answer"]} {factdata["image"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Yomomma"])
async def yomomma(ctx):
    async with aiohttp.ClientSession() as momma:
        async with momma.get(f'https://api.yomomma.info/') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                messagedata = await jsondata.json()
                
            await ctx.send(f'{messagedata["joke"]} https://tenor.com/view/jojo-dio-jotaro-yo-mama-big-chungus-gif-17109592')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Sum"])
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Stats"])
async def stats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(bot.guilds)
    memberCount = len(set(bot.get_all_members()))
    await ctx.send(f"Pues estoy en {serverCount} servidores. :smiley:\nEstoy corriendo en la version de Python {pythonVersion} y estoy usando la libreria discord.py {dpyVersion}")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=['uinfo',"Uinfo"])
async def userinfo(ctx, member: discord.Member=None):
    if member != None:
        roles = [role for role in member.roles if role != ctx.guild.default_role]
        try:
            embed = discord.Embed(colour=member.colour)
            embed.set_thumbnail(url=member.avatar_url)
            fields = [("Name", str(member), False),
                      ("ID", member.id, False),
                      ("Status", str(member.status).title(), False),
                      (f"Roles ({len(roles)})", " ".join([role.mention for role in roles][::-1]), False),
                      ("Permissions", ", ".join([str(i[0]).title().replace("_", " ") for i in member.guild_permissions if i[1]]), False),
                      ("Created at", member.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                      ("Joined at", member.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=member.colour)
            embed.set_thumbnail(url=member.avatar_url)
            fields = [("Name", str(member), False),
                      ("ID", member.id, False),
                      ("Status", str(member.status).title(), False),
                      ("Permissions", ", ".join([str(i[0]).title().replace("_", " ") for i in member.guild_permissions if i[1]]), False),
                      ("Created at", member.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                      ("Joined at", member.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await ctx.send(embed=embed)
    else:
        roles = [role for role in ctx.author.roles if role != ctx.guild.default_role]
        try:
            embed = discord.Embed(colour=ctx.author.colour)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            fields = [("Name", str(ctx.author), False),
                      ("ID", ctx.author.id, False),
                      ("Status", str(ctx.author.status).title(), False),
                      (f"Roles ({len(roles)})", " ".join([role.mention for role in roles][::-1]), False),
                      ("Permissions", ", ".join([str(i[0]).title().replace("_", " ") for i in ctx.author.guild_permissions if i[1]]), False),
                      ("Created at", ctx.author.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                      ("Joined at", ctx.author.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=ctx.author.colour)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            fields = [("Name", str(ctx.author), False),
                      ("ID", ctx.author.id, False),
                      ("Status", str(ctx.author.status).title(), False),
                      ("Permissions", ", ".join([str(i[0]).title().replace("_", " ") for i in ctx.author.guild_permissions if i[1]]), False),
                      ("Created at", ctx.author.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                      ("Joined at", ctx.author.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=['sinfo',"Sinfo"])
async def serverinfo(ctx):
    members = [member for member in ctx.guild.members if not member.bot]
    bots = [member for member in ctx.guild.members if member.bot]
    roles = [role for role in ctx.guild.roles if role != ctx.guild.default_role and not role.managed]
    categories = [str(cat) for cat in ctx.guild.categories]
    voice_channels = [str(vc) for vc in ctx.guild.voice_channels]
    text_channels = [str(tc) for tc in ctx.guild.text_channels]
    embed = discord.Embed(title=ctx.guild.name, color=discord.Color.dark_purple())
    embed.set_thumbnail(url=ctx.guild.icon_url)
    fields = [("Owner", ctx.guild.owner, True),
              ("Server ID", ctx.guild.id, True),
              ("Region", ctx.guild.region, True),
              ("Text Channels", len(text_channels), True),
              ("Voice Channels", len(voice_channels), True),
              ("Categories", len(categories), True),
              ("Roles", len(roles), True),
              ("Bots", len(bots), True),
              ("Members", len(members), True)]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=['ctd',"Ctd","Countdown"])
async def countdown(ctx, time : int = None):
    time = time or 3

    if time > 300:
        await ctx.send("maximum countdown time is 300 seconds")

    elif time > 10:
        i = time
        while i > 0:
            while i > 5:
                await ctx.send("{} seconds to go".format(i))
                i -= 5
                await asyncio.sleep(5)

            while i <= 5 and i > 0:
                await ctx.send("{}".format(i))
                i -= 1
                await asyncio.sleep(1)
        await ctx.send("Go !!!")  

    else:
        while time > 0:
            await ctx.send("{}".format(time))
            time -= 1
            await asyncio.sleep(1)

        await ctx.send("Go !!!")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='freemoney', aliases=['givememoney',"Freemoney"])
async def freemoney(ctx):
  last = await ctx.send('Generating free :dollar:...')
  await asyncio.sleep(3)
  people = ['Marilyn Monroe', 'Abraham Lincoln', 'Nelson Mandela', 'John F. Kennedy', 'Martin Luther King', 'Queen Elizabeth II', 'Winston Churchill', 'Donald Trump', 'Bill Gates', 'Muhammad Ali', 'Mahatma Gandhi', 'Mother Teresa', 'Christopher Columbus', 'Charles Darwin', 'Elvis Presley', 'Albert Einstein', 'Paul McCartney', 'Queen Victoria', 'Pope Francis', 'Jawaharlal Nehru', 'Leonardo da Vinci', 'VincentVan Gogh', 'Franklin D. Roosevelt', 'Pope John Paul II', 'Thomas Edison', 'RosaParks', 'Lyndon Johnson', 'Ludwig Beethoven', 'Oprah Winfrey', 'Indira Gandhi','Eva Peron', 'Benazir Bhutto', 'George Orwell', 'Desmond Tutu', 'Dalai Lama', 'Walt Disney', 'Neil Armstrong', 'Peter Sellers', 'Barack Obama', 'Malcolm X', 'J.K.Rowling', 'Richard Branson', 'Pele', 'Angelina Jolie', 'Jesse Owens', 'John Lennon', 'Henry Ford', 'Haile Selassie', 'Joseph Stalin', 'Lord Baden Powell', 'Michael Jordon', 'George Bush Jnr', 'Vladimir Lenin', 'Ingrid Bergman', 'Fidel Castro', 'Leo Tolstoy', 'Greta Thunberg', 'Pablo Picasso', 'Oscar Wilde', 'Coco Chanel', 'Charles de Gaulle', 'Amelia Earhart', 'John M Keynes', 'Louis Pasteur', 'Mikhail Gorbachev', 'Plato', 'Adolf Hitler', 'Sting', 'Mary Magdalene', 'AlfredHitchcock', 'Michael Jackson', 'Madonna', 'Mata Hari', 'Cleopatra', 'Grace Kelly', 'Steve Jobs', 'Ronald Reagan', 'Lionel Messi', 'Babe Ruth', 'Bob Geldof', 'Eva Peron', 'Benazir Bhutto', 'George Orwell', 'Desmond Tutu', 'Dalai Lama', 'Walt Disney', 'Neil Armstrong', 'Peter Sellers', 'Barack Obama', 'Malcolm X', 'J.K.Rowling', 'Richard Branson', 'Pele', 'Angelina Jolie', 'Jesse Owens', 'John Lennon', 'Henry Ford', 'Haile Selassie', 'Joseph Stalin', 'Lord Baden Powell', 'Michael Jordon', 'George Bush Jnr', 'Vladimir Lenin', 'Ingrid Bergman', 'Fidel Castro', 'Leo Tolstoy', 'Greta Thunberg', 'Pablo Picasso', 'Oscar Wilde', 'Coco Chanel', 'Charles de Gaulle', 'Amelia Earhart', 'John M Keynes', 'Louis Pasteur', 'Mikhail Gorbachev', 'Plato', 'Adolf Hitler', 'Sting', 'Mary Magdalene', 'Alfred Hitchcock', 'Michael Jackson', 'Madonna', 'Mata Hari', 'Cleopatra', 'Grace Kelly', 'Steve Jobs', 'Ronald Reagan', 'Lionel Messi', 'Babe Ruth', 'Bob Geldof', 'Roger Federer', 'Sigmund Freud', 'Woodrow Wilson', 'Mao Zedong', 'Katherine Hepburn', 'Audrey Hepburn', 'David Beckham', 'Tiger Woods', 'Usain Bolt', 'Carl Lewis', 'Prince Charles', 'Jacqueline Kennedy Onassis', 'C.S. Lewis', 'Billie Holiday', 'J.R.R. Tolkien', 'Billie Jean King', 'Margaret Thatcher', 'Anne Frank', 'More famous people', 'YOU', 'Simon Bolivar', 'Marie Antoinette', 'Cristiano Ronaldo', 'Emmeline Pankhurst ', 'Emile Zatopek', 'Lech Walesa', 'Julie Andrews', 'Florence Nightingale', 'Marie Curie', 'Stephen Hawking', 'Tim Berners Lee', 'Aung San Suu Kyi', 'Lance Armstrong', 'Shakira', 'Jon Stewart', 'Wright Brothers  Orville', 'Ernest Hemingway', 'Roman Abramovich', 'Tom Cruise', 'Rupert Murdoch', 'Al Gore', 'Sacha Baron Cohen', 'George Clooney', 'Paul Krugman', 'Jimmy Wales', 'Brad Pitt', 'Kylie Minogue', 'Stephen King']
  await last.edit(content=f':sunglasses: Stole **{random.randint(1, 100000)}** :dollar: from {random.choice(people)}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Identity"])
async def identity(ctx):
    async with aiohttp.ClientSession() as identity:
        async with identity.get(f'https://fakerapi.it/api/v1/users?_quantity=1') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                factdata = await jsondata.json()
                
            await ctx.send(f'{factdata["data"]}')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Wheater"])
async def weather(ctx, *, msg):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1b453b589a0691c857ddc95f0921df69'
        r = requests.get(url.format(msg)).json()
        temperature = str(r['main']['temp'])
        description = r['weather'][0]['description'].capitalize()
        icon = r['weather'][0]['icon']
        imgurl = 'http://openweathermap.org/img/w/{}.png'.format(icon)

        embed = discord.Embed(title="Weather for {}".format(msg), description= "**Temperatura: " + temperature + "°C**\n" + "**Descripcion: " + description + "**")
        embed.set_thumbnail(url=imgurl)

        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send("It looks like the source doesn't have any data over that city, or maybe what I read was not a city.")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Kick"])
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason = None):
  if not reason:
    await user.kick()
    embed=discord.Embed(title="Kickeado:", description=f"**{user}** fue kickeado por **no reason**.")
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("✅")
  else:
    await user.kick(reason=reason)
    embed=discord.Embed(title="Kickeado:", description=f"**{user}** ha sido kickeado por **{reason}**.")
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("✅")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Ban"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason = None):
  if not reason:
    await user.ban()
    embed=discord.Embed(title="Baneado:", description=f"**{user}** fue baneado por **no reason**.")
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("✅")
  else:
    await user.ban(reason=reason)
    embed=discord.Embed(title="Baneado:", description=f"**{user}** ha sido baneado por **{reason}**.")
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("✅")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context = True, aliases=["Purge","Clear","purge"])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 100):
    #Admin command
    await ctx.channel.purge(limit = amount)
    await ctx.send("Chat Cleared")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Devalpha","devalpha","DA","Da","dA"])
async def DevAlpha(ctx):
    await ctx.send(f'**Buscando la version de Desarrollo mas nueva...**')
    await asyncio.sleep(10)
    await ctx.send(f'**La version mas nueva de Desarrollo encontrada:** DevAlpha_5.0.0')
    await asyncio.sleep(5)
    embed = discord.Embed(
            color= discord.Colour.dark_teal()
        )
    embed.add_field(name='Version de Desarrollo 5.0.0' ,value='[Discord Soporte]( https://discord.gg/PvJuMs8z2j ) Apreta la imagen y tendras una mejor vista del changelog.', inline=False)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/849348860429467658/858496313070452756/unknown.png?width=775&height=600") 
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="owofy", aliases=["Owofy","Owo","owo"])
async def owofy(ctx, *, text):
    owo_faces = "owo uwu owu uwo u-u o-o OwO UwU @-@ ;-; ;_; ._. (._.) (o-o) ('._.) (｡◕‿‿◕｡)" \
    " (｡◕‿◕｡) (─‿‿─) ◔⌣◔ ◉_◉".split(sep=" ")

    text = text.replace("r", "w")
    text = text.replace("R", "W")
    text = text.replace("n", "ny")
    text = text.replace("N", "NY")
    text = text.replace("ll", "w")
    text = text.replace("LL", "W")
    text = text.replace("l", "w")
    text = text.replace("L", "W")

    text += f" {random.choice(owo_faces)}"

    await ctx.send(text)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="zalgofy", aliases=["Zalgofy","Zalgo","zalgo"])
async def zalgofy(ctx, *, text):
    
    zal_chars = ' ̷̡̛̮͇̝͉̫̭͈͗͂̎͌̒̉̋́͜ ̵̠͕͍̩̟͚͍̞̳̌́̀̑̐̇̎̚͝ ̸̻̠̮̬̻͇͈̮̯̋̄͛̊͋̐̇͝͠ ̵̧̟͎͈̪̜̫̪͖̎͛̀͋͗́̍̊͠ ̵͍͉̟͕͇͎̖̹̔͌̊̏̌̽́̈́͊ͅ ̷̥͚̼̬̦͓͇̗͕͊̏͂͆̈̀̚͘̚ ̵̢̨̗̝̳͉̱̦͖̔̾͒͊͒̎̂̎͝ ̵̞̜̭̦̖̺͉̞̃͂͋̒̋͂̈́͘̕͜ ̶̢̢͇̲̥̗̟̏͛̇̏̊̑̌̔̚ͅͅ ̷̮͖͚̦̦̞̱̠̰̍̆̐͆͆͆̈̌́ ̶̲͚̪̪̪͍̹̜̬͊̆͋̄͒̾͆͝͝ ̴̨̛͍͖͎̞͍̞͕̟͑͊̉͗͑͆͘̕ ̶͕̪̞̲̘̬͖̙̞̽͌͗̽̒͋̾̍̀ ̵̨̧̡̧̖͔̞̠̝̌̂̐̉̊̈́́̑̓ ̶̛̱̼̗̱̙͖̳̬͇̽̈̀̀̎̋͌͝ ̷̧̺͈̫̖̖͈̱͎͋͌̆̈̃̐́̀̈'.replace(" ", "")
    
    
    zalgo_text = ""
    
    for letter in text:
        if letter == " ":
            zalgo_text += letter
            continue

        letter += random.choice(zal_chars)
        letter += random.choice(zal_chars)
        letter += random.choice(zal_chars)
        zalgo_text += letter

    
    
    await ctx.send(zalgo_text)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="emojify", aliases=["Emojify","eMOJIFY"])
async def emojify(ctx, *, text):
    emoji = list("😂😝🤪🤩😤🥵🤯🥶😱🤔😩🙄💀👻🤡😹👀👁👌💦🔥🌚🌝🌞🔫💯")
    b_emoji = "🅱️"
    a_emoji = "🅰️"
    i_emoji = "ℹ️"

    text = text.replace("ab", "🆎")
    text = text.replace("cl", "🆑")
    text = text.replace("b", "🅱️")
    text = text.replace("a", "🅰️")
    text = text.replace("i", "ℹ️")
    text = text.replace("AB", "🆎")
    text = text.replace("CL", "🆑")
    text = text.replace("B", "🅱️")
    text = text.replace("A", "🅰️")
    text = text.replace("I", "ℹ️")

    emoji_text = ""

    for letter in text:
        if letter == " ":
            emoji_text += random.choice(emoji)
        else:
            emoji_text += letter

    await ctx.send(emoji_text)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="cheemify",aliases=["Cheemify","Cheemsify","cheemsify"])
async def cheemify(ctx, *, text):
    text = text.replace("ese", "ms")
    text = text.replace("se", "mse")
    text = text.replace("ck", "mk")
    text = text.replace("ake", "amke")
    text = text.replace("as", "ams")
    text = text.replace("n", "m")
    text = text.replace("ab", "amb")
    text = text.replace("lp", "lmp")
    text = text.replace("ke", "mke")
    text = text.replace("ec", "emc")
    text = text.replace("ig", "img")
    text = text.replace("ob", "omb")
    text = text.replace("pep", "pemp")
    text = text.replace("pop", "pomp")
    text = text.replace("rib", "rimb")

    await ctx.send(text)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="fakewords", aliases=["Fakwords"])
async def fakewords(ctx):
    url = "https://www.thisworddoesnotexist.com/api/random_word.json"
    word = requests.get(url).json()
    arrange = []
    arrange.append("**" + word['word']['word'] + "**")
    arrange.append("*" + word['word']['pos'] + "*")
    arrange.append(word['word']['definition'])
    embed = discord.Embed(title="**Palabra falsa: ** \n\n\n", description=listToString(arrange), color=0xffffff)
    
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Covid"])
async def covid(ctx, *, country_name = 'World'):
    confirmed = 0
    today_cases = 0
    deaths = 0
    today_deaths = 0
    recovered = 0
    active = 0
    critical = 0
    cases_per_mil = 0
    deaths_per_mil = 0
    tests = 0
    tests_per_mil = 0
    try:
        url = f'https://coronavirus-19-api.herokuapp.com/countries/{country_name}'
        stats = requests.get(url)
        json_stats = stats.json()
        country_name = json_stats['country']
        confirmed = json_stats['cases']
        today_cases = json_stats['todayCases']
        deaths = json_stats['deaths']
        today_deaths = json_stats['todayDeaths']
        recovered = json_stats['recovered']
        active = json_stats['active']
        critical = json_stats['critical']
        cases_per_mil = json_stats['casesPerOneMillion']
        deaths_per_mil = json_stats['deathsPerOneMillion']
        tests = json_stats['totalTests']
        tests_per_mil = json_stats['testsPerOneMillion']
    except:
        await ctx.send('Invalid country name.')
        return
    embed = discord.Embed(title = f'Informacion del Covid-19 En {country_name}:', color = discord.Color.red())
    embed.add_field(name = 'Casos Confirmados:', value = f'{format(confirmed, ",d")} Casos', inline = True)
    embed.add_field(name = 'Muertes:', value = f'{format(deaths, ",d")} Muertes', inline = True)
    embed.add_field(name = 'Recuperados:', value = f'{format(recovered, ",d")} Recuperados', inline = True)
    embed.add_field(name = 'Casos confirmados de hoy:', value = f'{format(today_cases, ",d")} Casos', inline = True)
    embed.add_field(name = 'Muertes de hoy:', value = f'{format(today_deaths, ",d")} Muertes', inline = True)
    embed.add_field(name = 'Casos Activos:', value = f'{format(active, ",d")} Casos', inline = True)
    embed.add_field(name = 'Casos cada un Millon:', value = f'{format(cases_per_mil, ",d")} Casos', inline = True)
    embed.add_field(name = 'Muertes cada un Millon:', value = f'{format(deaths_per_mil, ",d")} Muertes', inline = True)
    embed.add_field(name = 'Casos Criticos:', value = f'{format(critical, ",d")} Casos Criticos', inline = True)
    embed.add_field(name = 'Tests hechos:', value = f'{format(tests, ",d")} tests', inline = True)
    embed.add_field(name = 'Test hechos cada un Millon:', value = f'{format(tests_per_mil, ",d")} tests', inline = True)
    embed.add_field(name = '‎', value = '‎', inline = True)
    await ctx.send(embed = embed)
    if client.update_released:
        if random.randint(1, 100) >= 75:
            await ctx.send(f'~~New update! Check the updates command!~~')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["CovidCountryList","CovidcountryList","Covidcountrylist",])
async def covidcountrylist(ctx):
    dm = await ctx.author.create_dm()
    await dm.send(embed = discord.Embed(title = 'Lista de los Paises Soportados 1:', description = """USA
Brazil
India
France
Russia
UK
Italy
Spain
Turkey
Germany
Colombia
Argentina
Poland
Mexico
Iran
Ukraine
South Africa
Peru
Czechia
Indonesia
Netherlands
Chile
Canada
Romania
Belgium
Iraq
Israel
Portugal
Sweden
Philippines
Pakistan
Hungary
Bangladesh
Jordan
Switzerland
Serbia
Austria
Morocco
Japan
Lebanon
UAE
Saudi Arabia
Slovakia
Panama
Malaysia
Bulgaria
Ecuador
Belarus
Georgia
Nepal
Bolivia
Croatia
Greece
Azerbaijan
Dominican Republic
Tunisia
Kazakhstan
Palestine
Ireland
Denmark
Kuwait
Moldova
Lithuania
Costa Rica
Slovenia
Paraguay
Ethiopia
Egypt
Guatemala
Armenia
Honduras
Qatar
Bosnia and Herzegovina
Nigeria
Libya
Oman
Venezuela
Bahrain
Myanmar
Kenya
North Macedonia
Albania
Algeria
Estonia
S. Korea
Latvia
Uruguay
Norway
Sri Lanka
Montenegro
Ghana
Kyrgyzstan
Zambia
Uzbekistan
Finland
Cuba
Mozambique
El Salvador
Luxembourg
Singapore
Afghanistan
Cameroon
Cyprus
Namibia
Ivory Coast
Uganda
Botswana
Jamaica
Senegal
Zimbabwe""", color = discord.Color.dark_red()))
    await dm.send(embed = discord.Embed(title = 'List of supported countries 2:', description = """Malawi
Sudan
Australia
Malta
Thailand
DRC
Madagascar
Maldives
Angola
Rwanda
Guinea
Mayotte
Gabon
Syria
French Polynesia
Mauritania
Eswatini
Cabo Verde
French Guiana
Réunion
Tajikistan
Haiti
Burkina Faso
Belize
Andorra
Hong Kong
Guadeloupe
Somalia
Lesotho
Guyana
South Sudan
Togo
Mali
Congo
Aruba
Suriname
Bahamas
Mongolia
Trinidad and Tobago
Curaçao
Martinique
Djibouti
Benin
Equatorial Guinea
Nicaragua
Iceland
Papua New Guinea
Gambia
CAR
Niger
San Marino
Chad
Gibraltar
Saint Lucia
Seychelles
Yemen
Channel Islands
Sierra Leone
Comoros
Guinea-Bissau
Barbados
Eritrea
Burundi
Liechtenstein
Vietnam
New Zealand
Cambodia
Turks and Caicos
Monaco
Sao Tome and Principe
Sint Maarten
Liberia
St. Vincent Grenadines
Saint Martin
Isle of Man
Caribbean Netherlands
Antigua and Barbuda
Bermuda
Taiwan
Mauritius
Bhutan
St. Barth
Diamond Princess
Faeroe Islands
Timor-Leste
Tanzania
Cayman Islands
Wallis and Futuna
Brunei
Dominica
Grenada
British Virgin Islands
New Caledonia
Fiji
Falkland Islands
Laos
Macao
Saint Kitts and Nevis
Greenland
Vatican City
Anguilla
Saint Pierre Miquelon
Montserrat
Solomon Islands
Western Sahara
MS Zaandam
Marshall Islands
Samoa
Vanuatu
Micronesia
China""", color = discord.Color.dark_red()))
    if client.update_released:
        if random.randint(1, 100) >= 75:
            await ctx.send(f'~~New update! Check the updates command!~~')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Addrole"])
async def addrole(ctx, role: discord.Role , user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)  
        embed = discord.Embed(title = "GIVE ROLE", description =f"Successfully give {role.mention} Role to {user.mention} ")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title = "GIVE ROLE", description =f" {ctx.author.mention} you don't have permissions to use this command")
        await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Hack"])
async def hack(ctx):
  import asyncio
  message = await ctx.send("[:octopus:]`hacking the NASA`")
  await asyncio.sleep(3)
  await message.edit(content="[:key:]**IP FOUND!**")
  await asyncio.sleep(3)
  await message.edit(content="[:warning:] `DDOSING the ip of NASA {127.0.0.1}`")
  await asyncio.sleep(3)
  await message.edit(content="[:sos:]**Deploying botnets and sending 'weareanonymous' in tcp packets...**")
  await asyncio.sleep(4)
  await message.edit(content="> successfully taken down the nasa website now corps will come for ya!")
  await asyncio.sleep(4)
  await message.edit(content="[:wave:]**exiting tor nodes ....**")
  emoji = '\N{THUMBS UP SIGN}'
  await message.add_reaction(emoji)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Invite"])
async def invite(ctx):
	cannel = ctx.channel
	em = discord.Embed(
	    title="Invite",
	    description=
	    "¡Invitame a tu servidor! :star_struck: ",
	    color=discord.Colour.blurple())
	em.add_field(
	    name="Link",
	    value=
	    "[Invite me](https://discord.com/api/oauth2/authorize?client_id=845336978149212186&permissions=8&scope=bot)"
	)
	await ctx.send(embed=em)
	pass

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Minecraft"])
async def minecraft(ctx):
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Minecraft", value="Un juego realmente popular creado por Notch (Markus Persson)")
    embed.add_field(name="Wikipedia", value="https://en.wikipedia.org/wiki/Minecraft")
    embed.add_field(name="Gamepedia", value="https://minecraft.fandom.com/es/")
    embed.add_field(name="Version Actual", value="1.17")
    embed.set_thumbnail(url='https://img.gurugamer.com/resize/740x-/2021/05/10/grass-block-minecraft-a9a3.jpg')
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Lennyfaces","Face"])
async def face(ctx):
    faces=["¯\_(ツ)_/¯", "̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\З= ( ▀ ͜͞ʖ▀) =Ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿", "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)", "(ง ͠° ͟ل͜ ͡°)ง", "༼ つ ◕_◕ ༽つ", "ಠ_ಠ", "(づ｡◕‿‿◕｡)づ", "̿'̿'\̵͇̿̿\З=( ͠° ͟ʖ ͡°)=Ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)", "┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴", "( ͡°╭͜ʖ╮͡° )", "(͡ ͡° ͜ つ ͡͡°)", "(• ε •)", "(ง'̀-'́)ง", "(ಥ﹏ಥ)", "(ノಠ益ಠ)ノ彡┻━┻", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(☞ﾟ∀ﾟ)☞", "| (• ◡•)| (❍ᴥ❍ʋ)", "(◕‿◕✿)", "(ᵔᴥᵔ)", "(¬‿¬)", "(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)", "(づ￣ ³￣)づ", "ლ(ಠ益ಠლ)", "ಠ╭╮ಠ", "̿ ̿ ̿'̿'\̵͇̿̿\з=(•_•)=ε/̵͇̿̿/'̿'̿ ̿", "(;´༎ຶД༎ຶ`)", "༼ つ  ͡° ͜ʖ ͡° ༽つ", "(╯°□°）╯︵ ┻━┻", "( ͡ʘ ͜ʖ ͡ʘ)", "(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)", "(ಠ‿ಠ)", "ಠ╭╮ಠ", "(︶︿︶)", "ರ_ರ", "(⊙ω⊙)", "(._.) ( l: ) ( .-. ) ( :l ) (._.)", "(*≧▽≦)", "ಠoಠ", "[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]", "( ﾟヮﾟ)", "(´・ω・)っ由", "ಠ_ಥ", "(ಥ﹏ಥ)", "☜(⌒▽⌒)☞", "⊙﹏⊙", "ᕙ(⇀‸↼‶)ᕗ"]
    face=random.choice(faces)
    await ctx.send(face)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Tweet"])
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases=["Lovedetect","LoveDetect"])
async def lovedetect(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    shipuser1 = user.name
    shipuser2 = user2.name
    useravatar1 = user.avatar_url
    useravatar2s = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} Love each others", description=f"Love\n`{counter_}` Score:**{score}% **\nLoveName:**{finalName}**", color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            await ctx.send(embed=embed)

@bot.command(aliases=["Hacker"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def hacker(ctx, user: discord.User,):
    progresses = ["▯▯▯▯", "▮▯▯▯", "▮▮▯▯", "▮▮▮▯", "▮▮▮▮"]
    emails = ["icloud.com", "gmail.com", "yahoo.com", "mememail.com", "hotmail.com", "shaggy.org", "idiot.com", "email.gay"]
    passwords = [
        "vizaVilE", "lafozhiy", "ThebestoMan", "RAFUII", "miStotyA", "azHutimi", "nyAvapiG", "lihAepeT", "bzhuvedi", "ktipuvOR",
        "chuAzhTe", "tigoSokE", "kiloCHup", "clavito525", "nyuRYAhu", "lyutDyuH", "peniseater", "obschami", "IvoTsuzh", "duSchuOt",
        "lebiloch", "zerotwobestowaifu", "Shpizhzy", "TheBestPenisEver52", "holologi", "etyaRodV", "schaNIpe", "zumYANii", "nyaichinissannya", "sugonoyu",
        "bakugosimp", "helEzYUm", "dYuoscHi", "koGasAte", "tsaMarit", "saanturu", "edizEsor", "DefenUts", "bivYAoTk", "puNOroen",
        "dOpivogi", "motiveny", "SchatyUn", "chuNyApi", "ieatpenis", "HohoGAsy", "nyunisch", "hevoVomi", "votsisch", "TochaEgu",]
    embed = discord.Embed(
        title= progresses[0], description= "Hacking in progress",
        color= discord.Color(r.randint(0, 0xFFFFFF)))
    msg = await ctx.send(embed= embed)
    await asyncio.sleep(2)

    if not user.bot: data = (
        ("Buscando mail...", "Email", f"{user.name.replace(' ','_')}@{r.choice(emails)}", "❌Intento Bloqueado"),
        ("Encontrando Direccion IP...", "Direccion IP", ".".join(map(str, (r.randint(0, 255) for _ in range(4)))), "❌ Intento Bloqueado"),
        ("Recolectando contraseñas...", "Password", f"||{r.choice(passwords)}||", f"||{r.choice(passwords)}||"), # Always gets user password
        ("Vendiendo datos a Facebook...", "Facebook", "Datos vendidos! :dollar:", "❌ Datos Insignificantes"))
    else: data = (
        ("Hackeando su Base de Datos...", "Database", "jejej. :smiling_imp:", "❌ Intento Bloqueado"),
        ("Cambiando comandos...", "Commands", "Cambiados!", "❌ Intento Bloqueado"),
        ("Cambiando su estado de jugador....", "Estado de jugador", "Hackeado!", "❌ Intento Bloqueado"),
        ("Saliendo de todos sus servidores", "Servers", "Todos fuera!", "❌ Intento Bloqueado"))

    _ = 0
    for action, short, choice1, choice2 in data:
        _ += 1
        embed.title, embed.description= progresses[_], action
        await msg.edit(embed= embed)
        await asyncio.sleep(r.randint(1500, 3000)/ 1000)

        embed.add_field(name= short, value= r.choice([choice1, choice1, choice1, choice2]))
        await msg.edit(embed= embed)
        await asyncio.sleep(2)
    embed.title, embed.description= "Hack Completado", f"Hackeo Completado {user}"
    await msg.edit(embed= embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Slowmode"])
@commands.has_permissions(administrator=True)
async def slowmode(ctx, seconds: int):
	await ctx.channel.edit(slowmode_delay=seconds)
	await ctx.send(
	    f"```{ctx.author} ha hecho que los segundos del slowmode sean: {seconds} segundos!```")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Logo"])
async def logo(ctx, *, text):
    if len(text)>18:
            return await ctx.send("**Your text is too long!** Try again.")
    a = random.choice(['scoobydoo','cnn', 'starWars', 'yahoo', '43things', 'batman', 'SpiderMan', 'harrypotter', 'army', 'blazed', '101puppies'])
    em = discord.Embed(colour=discord.Colour.blue(), title='Your custom logo:')
    brand = text.replace(" ","%20")
    em.set_image(url=f'http://createfunnylogo.com/logo/{a}/{brand}.jpg')
    await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Banlist"])
async def banlist(ctx,help="``Lista de Baneados``"):
    try:
        banlist = await ctx.guild.bans()
    except discord.errors.Forbidden:
        await ctx.send("Can't list them without the `Ban Members` permission.")
        return
    bancount = len(banlist)
    display_bans = []
    bans = None
    if bancount == 0:
        bans = "Vamos!. Nadie ha sido baneado"
    else:
        for ban in banlist:
            if len(", ".join(display_bans)) < 1800:
                display_bans.append(str(ban.user))
            else:
                bans = ", ".join(display_bans) + "\n... y {} mas".format(len(banlist) - len(display_bans))
                break
    if not bans:
        bans = ", ".join(display_bans)
    await ctx.send("Bans Totales: `{}`\n```{}```".format(bancount, bans))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="warn", aliases=["Warn"])
@commands.has_guild_permissions(kick_members=True)
async def warn(ctx, user: discord.Member = None, *, reason=None):
    if user is None or reason is None:
        await ctx.send("Necesito una razon.")
    elif ctx.author.top_role.position <= user.top_role.position and ctx.guild.owner.id != ctx.author.id:
        await ctx.send("No puedes warnear a ese usuario por que el tiene un role mas alto que el tuyo/o no tengo suficientes permisos")
    else:
        print(f"Warneado a {user.name} por {reason}...")

        if str(user) not in warn_count:
            warn_count[str(user)] = 1
        else:
            warn_count[str(user)] += 1

        embed = discord.Embed(
            title=f"{user.name} ha sido Warneado", color=discord.Colour.red())
        embed.add_field(name="Razon", value=reason)
        embed.add_field(name="Este usuario a sido Warneado",
                        value=f"{warn_count[str(user)]} veces")

        await ctx.send(content=None, embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="warncount", aliases=["Warncount"])
async def warncount(ctx, user: discord.Member):
    if str(user) not in warn_count:
        warn_count[str(user)] = 0

        count = warn_count[str(user)]
        await ctx.send(f"{user.mention} ha sido warneado {count} veces")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Bitcoin"])
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("El precio del bitcoin es: $" + response['bpi']['USD']['rate'])

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def passgen( ctx ):
    password = ''
    for i in range( lenght ):
        password += random.choice( chars )
    emb = discord.Embed( description=f'✅ Su contraseña ha sido creada correctamente', colour=0x31f5f5 )
    em = discord.Embed( description=f'✅ Tu Contraseña: {password}\n⚠️ No La Compartas Con Nadie!', colour=0x31f5f5 )
    await ctx.send( embed = emb )
    await ctx.author.send( embed = em )

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Texcat"])
async def textcat(ctx: Context) -> None:
    """Send a random textcat."""
    try:
        embed = Embed(
            description=nekos.textcat(),
            color=0x690E8
        )
        await ctx.send(embed=embed)
    except nekos.errors.NothingFound:
        await ctx.send("Couldn't Fetch Textcat! :(")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="fumo", aliases=["Fumo"])
async def fumo(ctx):
    NEKO_URL = "http://fumoapi.herokuapp.com/fumo"
    neko = requests.get(NEKO_URL).json()
    embed = discord.Embed(title="```Fumo.```")
    embed.set_image(url=neko['URL'])
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="apod", aliases=["Apod"])
async def apod(ctx):
    NEKO_URL = "https://api.nasa.gov/planetary/apod?api_key=aPrygXh2F0jGxUQyJGki9gWhUUaLn1xnyhtEGfN7"
    neko = requests.get(NEKO_URL).json()
    embed = discord.Embed(title="```Foto del Dia segun la NASA```")
    embed.set_image(url=neko['url'])
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(name = "define", aliases=["Define","urban","Urban"])
async def define(ctx, *, query):
    try:
        url = f"http://api.urbandictionary.com/v0/define?term={query}"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        definition = data['list'][0]['definition']
        await ctx.send(f"**{query}: `" + definition + "`**")
    except:
        await ctx.send("**No Encontre una Definicion de: `" + query + "`!**")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Nekos_tags"])
async def nekos_tags(ctx):
	await ctx.send(", ".join(available_tags))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases=["Nekos"])
async def nekos(ctx, arg1, arg2):
	try:
		tag = arg1
		count = int(arg2)
	except ValueError:
		await ctx.send("Mal uso ejemplo: >nekos hug 20")
	else:
		if tag not in available_tags:
			await ctx.send("No es un tag disponible, par ver los tags disponibles usa >nekos_tags")
		elif int(count) > 50:
			await ctx.send("Para evitar problemas, pusimos 50 imagenes de limite (╥_╥)")
		else:
			gallery = [nekosimg(tag) for i in range(count)]

			nekos_embed = discord.Embed(description="Imagenes con el tag \"{}\" en nekos.life".format(tag))
			nekos_embed.set_image(url=gallery[0])
			nekos_embed.set_thumbnail(url="https://nekos.life/static/icons/favicon-194x194.png")
			nekos_embed.set_footer(text="Results: {}/{}".format(1, len(gallery)), icon_url=ctx.author.avatar_url)

			sent = await ctx.send(embed=nekos_embed)

			async def update_embed(img, cnt):
				new_embed = discord.Embed(description="Imagenes con el tag \"{}\" en nekos.life".format(tag))
				new_embed.set_image(url=img)
				new_embed.set_footer(text="Results: {}/{}".format(cnt, len(gallery)), icon_url=ctx.author.avatar_url)
				nekos_embed.set_thumbnail(url="https://nekos.life/static/icons/favicon-194x194.png")
				await sent.edit(embed=new_embed)

			reactions = ["⏪", "⬅", "⏹", "➡", "⏩"]
			"""
			⏪: Ve a la Primera Imagen
			⬅: Ve a la Anterior Imagen
			⏹: Borra el Mensaje
			➡: Ve a la Siguiente Imagen
			⏩: Ve a la Ultima Imagen
			"""

			for reaction in reactions:
				await discord.Message.add_reaction(sent, emoji=reaction)

			def check(react, source):
				return source != bot.user and str(react.emoji) in reactions

			current_image = 0

			while True:
				try:
					reacted, user = await bot.wait_for("reaction_add", timeout=120.0, check=check)
				except asyncio.TimeoutError:
					for emoji in reactions:
						await discord.Message.remove_reaction(sent, emoji=emoji, member=bot.user)
					break
				else:
					if reacted.emoji == "⏪":
						current_image = 0
						await update_embed(gallery[current_image], current_image + 1)
					elif reacted.emoji == "⏩":
						current_image = gallery.index(gallery[-1])
						await update_embed(gallery[current_image], current_image + 1)
					elif reacted.emoji == "⏹":
						await discord.Message.delete(sent)
						break
					elif reacted.emoji == "⬅":
						current_image -= 1

						if current_image < 0:
							current_image = gallery.index(gallery[-1])
							await update_embed(gallery[current_image], current_image + 1)
						else:
							await update_embed(gallery[current_image], current_image + 1)
					elif reacted.emoji == "➡":
						current_image += 1

						if current_image > len(gallery) - 1:
							current_image = 0
							await update_embed(gallery[current_image], current_image + 1)
						else:
							await update_embed(gallery[current_image], current_image + 1)

async def get_imag(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return discord.File(io.BytesIO(await resp.read()), "cool_image.jpeg")














































































listWorks =['Programo una Pagina de Citas y Gano ',
        'Hackeo la NASA y Gano ',
        'Entro a Master Chef y Con su Platillo de Mierda Gano ',
        'Se Masturbo en un Cine y Gano ',
        'Programo un Juego Para una Empresa de Dudosa Presedencia y Gano ',
        'Trabajo en el MCDonalds y Gano ',
        'Se prostituyo y Gano ']













mainshop = [{"name":"Pan Rallado","price":55,"description":"??"},
            {"name":"Empanadas","price":72,"description":"Unas empanadas"},
            {"name":"1Kg de Milanesas","price":100,"description":"Unas milanesas!"},
            {"name":"Reloj","price":100,"description":"Mira el tiempo"},
            {"name":"Leche","price":100,"description":"A tomar."},
            {"name":"Peluche de Felpa","price":125,"description":"No se por que, ¡pero deberias tenerlo!"},
            {"name":"TV","price":350,"description":"Mirar programas de tv."},
            {"name":"Laptop","price":1000,"description":"Para el trabajo"},
            {"name":"PC","price":10000,"description":"Engineer Gaming"},
            {"name":"Ferrari","price":99999,"description":"Auto de Deportes"},
            {"name":"Hogar","price":130000,"description":"Un lugar donde vivir."}]

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(aliases=['bal',"Bal"])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Billetera',color = discord.Color.red())
    em.add_field(name="Dinero en mano", value=wallet_amt)
    em.add_field(name='Dinero en Banco',value=bank_amt)
    await ctx.send(embed= em)

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command(aliases=["Beg","Work","work"])
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f'{ctx.author.mention}' + random.choice(listWorks) + f'{earnings} :coin:!!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(aliases=['wd',"Wd","Withdraw","wD"])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Inserta la cantidad a guardar")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('No tienes suficiente dinero')
        return
    if amount < 0:
        await ctx.send('¡Esa cantidad debe ser positiva! (Ej: 10255 No: 010255!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author.mention} Haz guardado {amount} :coins:')

@commands.cooldown(1, 20, commands.BucketType.user)
@bot.command(aliases=['dp',"Deposit","Dep","dep"])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Inserta la cantidad a guardar")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('No tienes suficiente dinero')
        return
    if amount < 0:
        await ctx.send('¡Esa cantidad debe ser positiva! (Ej: 10255 No: 010255!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'Banco')
    await ctx.send(f'{ctx.author.mention} Depositaste {amount} :coin:')

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(aliases=['Pay',"SendMoney"])
async def pay(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'bank')
    await update_bank(member,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} coins')

@commands.cooldown(1, 500, commands.BucketType.user)
@bot.command(aliases=['rb',"Rob"])
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send('It is useless to rob him :(')
        return

    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    await ctx.send(f'{ctx.author.mention} You robbed {member} and got {earning} coins')

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command(aliases=["Slots"])
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    final = []
    for i in range(3):
        a = random.choice(['X','O','Q'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await ctx.send(f'You won :) {ctx.author.mention}')
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send(f'You lose :( {ctx.author.mention}')

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(aliases=["Shop"])
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(aliases=["Buy"])
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("¿Que?, Ese objeto no esta aqui")
            return
        if res[1]==2:
            await ctx.send(f"No tienes suficiente dinero en manos para comprar {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(aliases=["Bag","Inventory","inventory"])
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Inventario")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@bot.command(aliases=["Sell"])
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("¡Que?, Ese objeto no esta aqui")
            return
        if res[1]==2:
            await ctx.send(f"Tu no tienes {amount} {item} en tu inventario.")
            return
        if res[1]==3:
            await ctx.send(f"Tu no tienes {item} en tu inventario.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.7* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal















bot.run('ODQ1MzM2OTc4MTQ5MjEyMTg2.YKffaQ.-lxOoGJXWBldp-drjwT0MOkvnH8')