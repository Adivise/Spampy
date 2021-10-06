from __future__ import unicode_literals
import os
import sys
import time
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    import json
except:
    os.system("pip install json")
    import json
try:
    import ctypes
except:
    os.system("pip install ctypes")
    import ctypes
try:
    from halo import Halo
except:
    os.system("pip install halo")
    from halo import Halo
try:
    import discord
except:
    os.system("pip install discord")
    import discord
import random
try:
    import asyncio
except:
    os.system("pip install asyncio")
    import asyncio
try:
    import shutil
except:
    os.system("pip install shutil")
    import shutil
try:
    import threading
except:
    os.system("pip install threading")
    import threading
try:
    from datetime import datetime
except:
    os.system("pip install datetime")
    from datetime import datetime
try:
    import base64
except:
    os.system("pip install base64")
    import base64
import re
try:
    from win10toast import ToastNotifier
except:
    os.system("pip install win10toast")
    from win10toast import ToastNotifier
try:
    from colorama import init, Fore, Back, Style
except:
    os.system("pip install colorama")
    from colorama import init, Fore, Back, Style
init(convert=True)
try:
    import string
except:
    os.system("pip install string")
    import string
try:
    from PIL import Image
except:
    os.system("pip install pillow")
    from PIL import Image
from discord.ext import commands



characters = string.ascii_letters + string.digits

os.system("cls")
os.system("mode 100,30")

try:
    with open("settings.txt") as setup:
        setup = setup.readlines()

except Exception as error:
    print(f" | Did you extract me properly? Did you delete/rename settings.txt? I can't access it\n | Error : {error}")
    time.sleep(10)
    os._exit(0)

token = setup[0].replace('"',"").replace("TOKEN=","")

spinner = Halo(
    text=' | Satan X - Loading',
    spinner={
        'interval': 250,
        'frames': ['.', '..', '...']
    }
)
spinner.start()
sooo = requests.get('https://discordapp.com/api/v8/users/@me', headers={'Authorization': token.strip()})


if sooo.status_code == 200:
    spinner.succeed(' | Token valid - Starting up selfbot')    


else:
    spinner.stop()
    os.system("cls")

    print(' | Invalid token. Put a valid token in settings.txt') 
    try:
        j = json.loads(sooo.text)
        errormessage = j['message']
        print(f" | Error : {errormessage}")
    except:
        pass
    time.sleep(5)
    os._exit(0)

prefix = setup[1].replace('"',"").replace("PREFIX=","") 

scalic = commands.Bot(prefix.strip(), self_bot=True)
scalic.remove_command("help")

editedmessages ={}

spinner = Halo(
    text=' | Satan X - Connecting',
    spinner={
        'interval': 250,
        'frames': ['.', '..', '...']
    }
)
spinner.start()

commandsdone = 0
messagessent = 0

def screen():
    global commandsdone
    global messagessent
    global accountsinprogress
    global tokensmade
    global errorsoccured
    global starttime
    os.system("cls")

    while True:
        os.system("mode 100,30")
        currenttime = time.time()
        timedata = currenttime-starttime
        hours = timedata//3600
        timedata = timedata - 3600*hours
        minutes = timedata//60
        seconds = timedata - 60*minutes
        os.system(f"title Selfbot - Running on {scalic.user.name} - Enjoy")
        logo = f"""

				        {Fore.WHITE}Connected To : {Fore.WHITE}[{Fore.RED}{scalic.user.name}#{scalic.user.discriminator}{Fore.WHITE}]


				        Total Guilds : {Fore.WHITE}[{Fore.RED}{len(scalic.guilds)}{Fore.WHITE}]


				        Time Elapsed : {Fore.WHITE}[{Fore.RED}{'%d:%d:%d' %(hours,minutes,seconds)}{Fore.WHITE}]


        """
        print(logo)
        time.sleep(1)
        os.system("cls")

###
@scalic.event
async def on_command_error(ctx,error):
    global commandsdone
    if isinstance(error, commands.CommandNotFound):
        commandsdone -= 1
    else:
        with open(f'Log/errorlog.txt', 'a') as er:
            er.write(f"[!] You said : \"{ctx.message.content}\" | Error : \"{str(error)}\"\n")

@scalic.event
async def on_connect():
    global starttime
    starttime = time.time()
    spinner.stop()
    os.system("cls")
    threading.Thread(target = screen).start()
    try:

        f = open(f"./data/{str(scalic.user.id)}.ico",'r')
        f.close()
    except:
        response = requests.get(scalic.user.avatar_url, stream=True)
        with open(f"./data/{str(scalic.user.id)}.png", 'wb') as scalic_pfp: 
            shutil.copyfileobj(response.raw, scalic_pfp)

        filename = f"./data/{str(scalic.user.id)}.png"
        img = Image.open(filename)
        img.save(f"./data/{str(scalic.user.id)}.ico",format = 'ICO', sizes=[(32,32)])

def ssspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:

        randcolor = random.randint(0x000000, 0xFFFFFF)
        data = {
          "content": "@everyone **Nuked via scalic** Body-ody-ody-ody-ody-ody-ody-ody Body-yada-yada-yada-yada-yada-yada-yada-yada weeee @@@@@@@@@@@@@@@ sksksksk\n:chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:",
          "embeds": [
            {
              "title": "This server has been nuked via scalic nuker",
              "tts": "true",
              "description": "**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_\n\n**Body-ody-ody-ody-ody-ody-ody-ody**\n\n__Body-ody-ody-ody-ody-ody-ody-ody__\n\n_Body-ody-ody-ody-ody-ody-ody-ody_",
              "url": "https://www.youtube.com/watch?v=X_C26M6MJiY",
              "color": randcolor,
              "fields": [
                {
                  "name": "Scalic Nuker",
                  "value": "Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker"
                },
                {
                  "name": "Nuked by scalic Nuked by scalic",
                  "value": "Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker"
                },
                {
                  "name": "Scalic Nuker Scalic Nuker Scalic Nuker",
                  "value": ":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:"
                },
                {
                  "name": "eee",
                  "value": ":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:  :chains: :chains: :chains:"
                }
              ],
              "author": {
                "name": "Scalic",
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4",
                "icon_url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              },
              "footer": {
                "text": "Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker Scalic Nuker",
                "icon_url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              },
              "image": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              },
              "thumbnail": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              }
            },
            {
              "url": "https://www.youtube.com/watch?v=X_C26M6MJiY",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              }
            },
            {
              "url": "https://www.youtube.com/watch?v=X_C26M6MJiY",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              }
            },
            {
              "url": "https://www.youtube.com/watch?v=X_C26M6MJiY",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
              }
            }
          ],
          "username": "Scalic nuker scalic nuker - an advanced selfbot made open source on github! @@@@",
          "avatar_url": "https://avatars.githubusercontent.com/u/78554732?s=200&v=4"
        }

        spamming = requests.post(webhook, json=data)  
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass #i might have something here later so putting pass in for now

        elif "rate limited" in spammingerror.lower():
            
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)

            except:
                delay = random.randint(5, 10)
                time.sleep(delay)
        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@scalic.command(aliases=['webhookfuck', 'spamwebhooks',"webhooknuke","webhooksnuke","webhooksfuck","spamwebhook","swh"])
async def webhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: #nuked with existing ones too!
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = ssspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1 #+1 just in case any errors idk
    for i in range(webhookamount):  #sooo - a bit about this. 50 webhooks can usually be made at once - it'll give you the option to make more but return "internal error" - this is an efficient way to make the correct amount of channels and get the best possible spam (multiple webhooks in one channel isnt efficient)
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name='SATAN X DISCORD')
                threading.Thread(target = ssspam, args = (webhook.url,)).start()
                f = open(r'data/webhooks-'+str(ctx.guild.id)+".txt",'a')
                f.write(f"{webhook.url} \n")
                f.close()

            except:
                print (f"{Fore.RED} > Webhook Error")

@scalic.command(aliases=['stopwebhookfuck', 'webhookstop',"webhookspamstop","stopwebhooksspam","webhookspamoff","wss"])
async def stopwebhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = False      

scalic.run(token.strip(), bot=False)
