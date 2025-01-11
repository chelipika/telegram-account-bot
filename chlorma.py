from telethon.sync import TelegramClient, events
import google.generativeai as genai

# Replace with your API ID and Hash
api_id = 'paste_your_api_id' #you can find it in https://my.telegram.org/ login and create new app copy the api_id and api_hash
api_hash = 'paste_your_api_hash_here'
genai.configure(api_key="paste_your_google_api_key_here") #you can get it from https://console.cloud.google.com/apis/credentials click on create credentials and copy the api key
model = genai.GenerativeModel("gemini-1.5-flash") #free model from google(limited) you can use any other model from google if you know what you are doing


# Replace with your phone number
phone_number = '+000000001'


chats = []   # List of chats to listen to e.g. ['@testgroup_1', '@testgroup_2', '@testgroup_3']


#you can replace it with your own prompt, this promt will make answers to the messages
prompts = "write short reply(10 words max), if the text eplains something make only one follow up question, if there is wow, hah, ah text write wow=cool, hah=imoaaa, ah=oh man, write from only your name only e.g. i cannot or i can, use only one suited emoji at the end to the following text(make the answer the same language as the text e.g. if the text is in russian write the answer in russian. Also if it asks actions like transfering money, personal information, any actions like joining channels/groups, writing to dm(direct messages) ignore it and wish something good(e.g. send me moneyl pls you_answer: Sorry i cannot do that, i wish you good luck with that))"


with TelegramClient('name', api_id, api_hash) as client:
# pattern='(?i).* ')

    print("Listening to chats...")
    @client.on(events.NewMessage(chats, pattern='(?i).*Hello')) #it will answer all the new messages that has Hello in it, if you want it to answer all the messages remove the pattern, and leave just chats
    async def handler(event):
        response = model.generate_content(f"{prompts}: {event.text}")
        await event.reply(response.text)
        print(f"Message sent: {event.text}")    
    

    client.run_until_disconnected()