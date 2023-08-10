"""
This file's function is to ensure startup and to load our events and commands.
"""
# Dependencies
from dotenv import load_dotenv; from os import getenv
import discord, jishaku; from discord.ext import commands
from src.events.join_leave import memberJoin, memberLeave

load_dotenv(dotenv_path = "./src/config/.env") # Get our Environment Variables

intents = discord.Intents.all(); intents.presences = True; intents.members = True
activity = discord.Activity(type=discord.ActivityType.listening, name="to Member count")
client = commands.Bot(command_prefix = ["x."], activity = activity, intents=intents)

@client.event # This event prints out the bot username & calls our .csv file module.
async def on_ready():
    print(f"Logged into the API as {client.user}")
    from src.events import on_start_list; on_start_list.makeMemberList(client=client, GUILD_ID=getenv("GUILD_ID"), FILE_NAME=getenv("FNAME"))
    await client.load_extension("jishaku") # Jishaku is a debugging tool for Discord Bots. [USAGE: x.jsk ...]

@client.event # This event handles the joining of a Member & adds them to the .csv file.
async def on_member_join(member):
    print(f"{member.name} has joined and is being added to {getenv('FNAME')}")
    memberJoin(client=client, GUILD_ID=int(getenv("GUILD_ID")), member=member, FILE_NAME=getenv("FNAME"))

@client.event
async def on_member_remove(member):
    print(f"{member.name}#{member.discriminator} has left and is being removed from {getenv('FNAME')}")
    memberLeave(client=client, GUILD_ID=int(getenv("GUILD_ID")), member=member, FILE_NAME=getenv("FNAME"))

@client.event # This event stops users from interacting with the bot in DM's
async def on_message(message):
  if message.guild is None:
    return
  await client.process_commands(message)

owner = getenv("OWNER")
client.run(getenv("TOKEN")) # Run our bot.