from telethon.sync import TelegramClient, events

# Replace with your API ID and Hash
api_id = 'paste_your_api_id' #you can find it in https://my.telegram.org/ login and create new app copy the api_id and api_hash
api_hash = 'paste_your_api_hash_here'


# Replace with your phone number
phone_number = '+000000001'


chats = []   # List of chats to listen to e.g. ['@testgroup_1', '@testgroup_2', '@testgroup_3']


with TelegramClient('name', api_id, api_hash) as client:
# pattern='(?i).* ')

    print("Listening to chats...")
    @client.on(events.NewMessage(chats, pattern='(?i).*Hello')) #it will answer all the new messages that has Hello in it, if you want it to answer all the messages remove the pattern, and leave just chats = NewMessage(chats)
    async def handler(event):
        await event.reply("Hello!, how can i help you?") #you can replace the answer(text: Hello!, how can i help you?) with your own
        print(f"Message sent: {event.text}")    
    

    client.run_until_disconnected()