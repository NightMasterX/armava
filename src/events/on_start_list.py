"""
When the bot starts up and is ready, this module is triggered and all existing members are added to our
.csv file
"""

from datetime import datetime

def makeMemberList(client, GUILD_ID: int, FILE_NAME):
    print("makeMemberList has been Loaded.")    
    for guild in client.guilds:
        if guild.id == GUILD_ID:
            print(f'{client.user} is scraping the following server: {guild.name} ,id: {guild.id})')        

        with open(FILE_NAME, mode='w',encoding='utf8') as f:
                f.write('username,join_time\n')
                for member in guild.members:
                    line = '{},{}\n'.format(member.name+"#"+member.discriminator, str(datetime.now()))
                    f.write(line)
                print("Startup Member List Successfully Generated!")
                            