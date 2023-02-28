import time

import datetime

def time4logs():

    return f'[{datetime.datetime.now().strftime("%d.%m.%Y %h:%M:%S")}]'

print(time4logs(), "Бот запускается")

start = time.time()

import disnake #disnake весь код будет на нём

from disnake.ext import commands #команды

import asyncio

from asyncio import sleep

import os #файлы

import config

import oauth

from config import Auth

print(time4logs(), "Библиотеки импортированы")

#Начало кода бота

release = oauth.release

if release:

    token = Auth.discord_auth["release"]

else:

    token = Auth.discord_auth["debug"]

intents = disnake.Intents().all()

bot = commands.Bot(intents = intents, command_prefix = "?")

@bot.event

async def on_ready():

    print(f"{time4logs()}Бот запущен под ником {bot.user}")

    #Статус

    while True:

        await bot.change_presence(activity=disnake.Game(name="в пинг понг"))

        await sleep(15)

        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="за серверами"))

        await sleep(15)

for filename in os.listdir("./cogs"):

    if filename.endswith(".py") and not filename.startswith("_"):

        bot.load_extension(f'cogs.{filename[:-3]}')

        print(f"[INFO] Module {filename} is loaded!")

@bot.slash_command()

async def reload(ctx, extention):

    if ctx.author.id in [578533097293873162]:

        bot.unload_extension(f"cogs.{extention}")

        bot.load_extension(f"cogs.{extention}")

        embed = disnake.Embed(color = disnake.Color.green(), title = "Reload", description = f"Module ` {extention} ` successfully reloaded")

        await ctx.send(embed=embed)

bot.run(token)
