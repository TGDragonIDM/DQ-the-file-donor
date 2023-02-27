import os
from pyrogram import Client, filters
from pyrogram.types import Message, User


@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Hello 👋 {message.from_user.mention}, Welcome To {message.chat.username} Happy To Have Here ♥️",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Sad To See You Leaving {message.from_user.mention}, Take Care..!",chat_id=chatid)
	
