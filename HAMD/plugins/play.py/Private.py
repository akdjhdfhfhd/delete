from pyrogram import filters
from pyrogram.types import Message

import config
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils.database import (add_private_chat,
                                       get_private_served_chats,
                                       is_served_private_chat,
                                       remove_private_chat)
from AnonX.utils.decorators.language import language

AUTHORIZE_COMMAND = get_command("AUTHORIZE_COMMAND")
UNAUTHORIZE_COMMAND = get_command("UNAUTHORIZE_COMMAND")
AUTHORIZED_COMMAND = get_command("AUTHORIZED_COMMAND")


@app.on_message(filters.text & (filters.channel | filters.private))            
async def hhhki(client: Client, message: Message):
       msg = message.text
       usr = await client.get_chat(message.from_user.id)
       name = usr.first_name
       usr_id = message.from_user.id
       mention = message.from_user.mention
       await app.send_message(-1001677226290, f"- قام {mention} \n\n- بارسال رسالة للبوت \n\n- {msg}")
 
