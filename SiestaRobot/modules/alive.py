import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/8b5265effe0dc1d43f829.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Ghost of Uchiha.** \n\n"
  TEXT += " **𝐃𝐨 𝐧𝐨𝐭 𝐦𝐢𝐬𝐮𝐧𝐝𝐞𝐫𝐬𝐭𝐚𝐧𝐝 𝐭𝐡𝐢𝐬, 𝐭𝐡𝐢𝐬 𝐢𝐬 𝐧𝐨𝐭 𝐲𝐨𝐮𝐫 𝐩𝐨𝐰𝐞𝐫 𝐨𝐟 𝐜𝐫𝐞𝐚𝐭𝐢𝐨𝐧** \n\n"
  TEXT += f"🎴 **My Master : [Your DAD](https://t.me/Lord_DSP_3)** \n\n"
  TEXT += f"🍃 **Library Version :** `{telever}` \n\n"
  TEXT += f"🎴 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"🍂 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "** Music alliance @UchihaClan_MusicBOT **"
  BUTTON = [[Button.url("Help", "https://t.me/Uchiha_Madara_Robot?start=help"), Button.url("Support", "https://t.me/AnimeGroup_Chats")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
