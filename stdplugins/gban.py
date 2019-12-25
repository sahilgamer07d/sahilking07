"""Globally Ban users from all the
Group Administrations bots where you are SUDO
Available Commands:
.gban REASON
.ungban REASON"""

import asyncio
from telethon import events
from uniborg.util import admin_cmd
from sample_config import Config
from datetime import datetime
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from uniborg.util import admin_cmd


gbanned_rights = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True
)

ungbanned_rights = ChatBannedRights(
    until_date=None,
    view_messages=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None
)


@borg.on(admin_cmd(pattern="gban ?(.*)"))
async def _(event):
    if Config.G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            Config.G_BAN_LOGGER_GROUP,
            "GBANNED (tg://user?id={}) {}".format(r_from_id, reason)
        )
    if input_cmd == "gban":
       rights = gbanned_rights
    await event.edit("`GBANNED` [{}](tg://user?id={}).".format(str(user_id),str(user_id)))
    

@borg.on(admin_cmd(pattern="ungban ?(.*)"))
async def _(event):
    if Config.G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            Config.G_BAN_LOGGER_GROUP,
            "UNGBANNED (tg://user?id={}) {}".format(r_from_id, reason)
        )
    if input_cmd == "ungban":
         rights = ungbanned_rights
    await event.edit("`UN-GBANNED` [{}](tg://user?id={}).".format(str(user_id),str(user_id)))
