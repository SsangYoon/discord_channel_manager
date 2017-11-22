import discord
import asyncio
import config

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    
@client.event
async def on_message(message):
    if message.content.startswith('/moveall'):
#    def move_member(self, member, channel):
        
        channel_name = None

        for elem in str.split(message.content)[1:]:
            if channel_name is None:
                channel_name = elem
            else:
                channel_name += " " + elem

        print(channel_name)    

        to_channel = get_correct_channel(channel_name)
        all_member = client.get_all_members()

        if to_channel is None:
            await client.send_message(message.channel, 'Invalid Channel Name : ' + str(to_channel))
        else:
            for member in all_member:
                await client.move_member(member, to_channel)

def get_correct_channel(channel_name):
    for channel in client.get_all_channels():
        if channel_name == channel.name:
            return channel

    return None



client.run("MzgyOTM1MTEyODg4ODc3MDY2.DPdBeg.48lHJw8i0LRYnyfcECOZX-J6AF0")
