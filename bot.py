from telethon import TelegramClient, events

api_id = 15214434
api_hash = '263d01dd8303c7f55e576eae10c842c5'

client = TelegramClient('user',api_id,api_hash).start()
message = 'Thanks for contacting me.  I will respond soon!'

@client.on(events.NewMessage())
async def handler(event):
  sender = await event.get_input_sender()
  away client.send_message(sender,message)
  
client.run_until_disconnected()
