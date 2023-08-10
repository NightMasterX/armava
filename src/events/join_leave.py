"""
This file holds our member join and leave event modules. These modules will be executed when a member either
leaves or joins.
"""

import csv
from datetime import datetime

def memberJoin(client, GUILD_ID, member, FILE_NAME):
    for guild in client.guilds:
        if guild.id == GUILD_ID:
            print("Guild ID ✅")

            with open(FILE_NAME, mode='a', encoding='utf8') as f:
                line = '{},{}\n'.format(member.name + "#" + member.discriminator, str(datetime.now()))
                f.write(line)

def memberLeave(client, GUILD_ID, member, FILE_NAME):
    for guild in client.guilds:
        if guild.id == GUILD_ID:
            print("Guild ID ✅")
            
            with open(FILE_NAME, 'r', encoding='utf8') as file:
                data = file.readlines()
            
            with open(FILE_NAME, 'w', encoding='utf8') as f:
                for line in data:
                    if not line.startswith(f"{member.name}#{member.discriminator},"):
                        f.write(line)
            break