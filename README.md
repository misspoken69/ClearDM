# Purge Self-Bot
Purge all messages in a Discord server or DM! (Your messages only for DMs)

## Usage
- Head over to `main.py`
- Go down the code to line `30`.
- Where it says `"YOUR_TOKEN"`, put your token there.

## Customize
- You can customize the word/prefix you want to say to delete messages in `main.py`.

## Help/Credits
This was made by ! Misspoken#7357 :))) Main account disabled LOL

```            channels=message.channel.guild.channels
        elif(message.content=="change this to anything you want"): # Change that to anything you want so when you type it in the channel it'll delete everything
            channels.append(message.channel)
