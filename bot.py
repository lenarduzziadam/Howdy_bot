# bot.py
import os
import logging
from typing import Final
import discord
from dotenv import load_dotenv
from responses import get_response

# Configure the logging
logging.basicConfig(filename='logs/error_log.txt', 
                    level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!!!")
        
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#Bot setup
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

#message functionality
async def send(message: discord.Message, user_message: str) -> None:
    
    if not user_message:
        print("Messge empty: Intents likely not enabled")
    
    is_private = (user_message[0] == "!")
    
    if is_private:
        user_message = user_message[1:]
        
    try:
        response: str = get_response(user_message)
        if is_private:
            await message.author.send(response) 
        else:
            await message.channel.send(response)
    except Exception as e:
        logging.error("Error occurred: %s", e)
        print(e)
        
@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message: str = message.content
    channel = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send(message, user_message)


def main() -> None:
    #run bot
    client.run(TOKEN)
    
if __name__ == "__main__":
    main()

