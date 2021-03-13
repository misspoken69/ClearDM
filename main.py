import discord
class MyClient(discord.Client):
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(message.content=="purge_server"):
            channels=message.channel.guild.channels
        elif(message.content=="change this to anything you want"): # Change that to anything you want so when you type it in the channel it'll delete everything
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            print(channel)
            try:
                async for mss in channel.history(limit=None):
                # Gets all messages, you might want to purge channel by channel to speedup if the server is old
                    if(mss.author==self.user):
                        print(mss.content)
                        try:
                            await mss.delete()
                        except:
                            print("I can't delete any messages.\n") # If this happens you probably purged too many times.
            except:
                print("Hmm, I can't read the history of this DM.\n")
            

client=MyClient(heartbeat_timeout=86400, guild_subscriptions=False)
client.run("YOUR_TOKEN", bot=False)
