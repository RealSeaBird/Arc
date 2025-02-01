#WARNING THIS IS THE EXPERIMENTAL VERSION

#The code your seeing rigth here is for the P-22 Linux update

#VERSION:Alpha 2

import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import app_commands
import os
import random
import praw
import requests


intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await bot.tree.sync()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Please use a valid command.")
    else:
        raise error
    await bot.tree.sync(guild=discord.Object(id=1327411772314878012))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Please use a valid command.")
    else:
        raise error

@bot.tree.command(name="meme", description="Get a random meme!")
async def meme(interaction: discord.Interaction):
    try:
        
        response = requests.get('https://meme-api.com/gimme')
        
        
        if response.status_code == 200:
            meme_data = response.json()
            
            
            meme_url = meme_data['url']

            
            await interaction.response.send_message(meme_url)
        else:
            
            await interaction.response.send_message("Sorry, I couldn't fetch a meme at the moment. Please try again later.")

    except Exception as e:
        
        await interaction.response.send_message(f"An error occurred: {e}")

@bot.command()
async def sync(ctx):
    await bot.tree.sync()
    await ctx.send("Commands have been synced.")

@bot.command()
async def fishroll(ctx):
    await ctx.send("YOU HAVE DISCOVERD A SECRETE COMMAND CLICK THIS TO WATCH THE NEW YONKAGOR SONG  https://www.youtube.com/watch?v=vbbGQpcrH8I")

@bot.command()
async def yourjustlike1mib(ctx):
    await ctx.send("Your just like 1MiB https://www.youtube.com/watch?v=le8U2lF2qis ")

@bot.command()
async def humanenthusiast(ctx):
    await ctx.send("IM A HUMAN ENTHUSIAST https://www.youtube.com/watch?v=WirvCutdVeI ")
@bot.command()
async def rulex(ctx):
    await ctx.send("https://tenor.com/view/yonkagor-furry-song-exist-forgot-gif-24974981")

@bot.tree.command(name="greet", description="Greet a user")
async def greet(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f"Hello, {user.mention}!")

@bot.tree.command(name="goof", description="Stop being goofy!")
async def goof(interaction: discord.Interaction):
    await interaction.response.send_message("Stop being goofy!")

@bot.tree.command(name="archhelp", description="Help on installing arch linux")
async def archhelp(interaction: discord.Interaction):
    await interaction.response.send_message("I recommend watching https://www.youtube.com/watch?v=68z11VAYMS8 Its a great guide")

@bot.tree.command(name="changelogs", description="What has changed in the last update")
async def changelogs(interaction: discord.Interaction):
    await interaction.response.send_message("Added /memes command") #Make sure to update the changelogs

@bot.tree.command(name="iforgor", description="I Forgot that you Exist!")
async def iforgor(interaction:discord.Interaction):
    await interaction.response.send_message("https://tenor.com/view/yonkagor-furry-song-exist-forgot-gif-24974981")

@bot.tree.command(name="fish", description="Kan kan?")
async def fish(interaction: discord.Interaction):
    await interaction.response.send_message("'Kan, ikan, ikan, ikan, ikan, ikan https://www.youtube.com/watch?v=tF6CKxc_2JQ ")

@bot.tree.command(name="wikihow", description="Seadrives website")
async def wikihow(interaction: discord.Interaction):
    await interaction.response.send_message("https://seadrive.vercel.app/")

@bot.tree.command(name="howtofitin", description="How to fit in with the linux community")
async def howtofitin(interaction: discord.Interaction):
    await interaction.response.send_message("Linux users are all either Discord mods, script kids, mentaly insane or Femboys(And or Furrys)")

current_directory = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_directory, '.env')
load_dotenv(dotenv_path=dotenv_path)


load_dotenv(dotenv_path='./.env')

token = os.getenv('DISCORD_BOT_TOKEN')
#print(f"Token: {token}")

if token is None:
    print("The token is not being loaded. Check the .env file.")
else:
    print("Token loaded successfully.")


bot.run(token)
