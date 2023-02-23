import asyncio
import random
import threading  # Threading need for creating continuously loop
from datetime import datetime

from telethon import TelegramClient

logfilename = 'log.csv'  # Logging events into this file


async def main():
    loop = asyncio.new_event_loop()
    api_id = 23248124  # Your API ID from dev site
    api_hash = 'b3ea5823ce994b7874933c51a6bb03ba'  # Your API HASH from dev site
    client = TelegramClient('duatigatest', api_id, api_hash, loop=loop)
    async with client:
        me = await client.get_me()
        print(me.phone)
        await client.send_message('me', 'Ass!')  # Sending single message to Saved messages chat for wakeup activity
        async for message in client.iter_messages('me'):  # checking for last message in 'me' chat
            print(message.id)
            timenow = datetime.now()
            with open(logfilename, 'a', encoding="utf-8") as file_object:
                file_object.write(f'"{timenow}"\n')  # wtiting to log
            await client.delete_messages('me', message.id)  # deleting message for preventing garbage collection
            break  # we need only one FOR iteration
    return


def runAll():
    global state
    threading.Timer(int(random.choice(range(120, 300))), runAll).start()
    asyncio.run(main())


runAll()
