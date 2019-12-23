"""Plugin for .gmute 
Made for BotHub By @AyushChatterjee
"""

from uniborg.util import admin_cmd
from telethon import events
import asyncio

@borg.on(admin_cmd("ungmute ?(.*)", allow_sudo=True))
async def ungmoot(un_gmute):

    # Admin or creator check
    chat = await un_gmute.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await un_gmute.edit(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from sql_helpers.gmute_sql import ungmute
    except AttributeError:
        return


    # If pass, inform and start ungmuting
    await un_gmute.edit('Ungmuting...')
    # Inform about success
    await un_gmute.edit("Ungmuted Successfully")


@borg.on(admin_cmd("gmute ?(.*)", allow_sudo=True))
async def gspider(gspdr):
    
    # Admin or creator check
    chat = await gspdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await gspdr.edit(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from sql_helpers.gmute_sql import gmute
    except AttributeError:
        return


    # If pass, inform and start gmuting
    await gspdr.edit("Grabs a huge, sticky duct tape!")
    # Inform about success
    await gspdr.edit(f"Globally taped!Reason: {reason}")
