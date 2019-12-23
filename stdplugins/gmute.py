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

    user = await get_user_from_event(un_gmute)
    user = user[0]
    if user:
        pass
    else:
        return

    # If pass, inform and start ungmuting
    await un_gmute.edit('
Ungmuting...
')

    if ungmute(user.id) is False:
        await un_gmute.edit("Error! User probably not gmuted.")
    else:
        # Inform about success
        await un_gmute.edit("
Ungmuted Successfully
")


@borg.on(admin_cmd("ungmute ?(.*)", allow_sudo=True))
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

    user, reason = await get_user_from_event(gmute)
    user = user[0]
    if user:
        pass
    else:
        return

    # If pass, inform and start gmuting
    await gspdr.edit("Grabs a huge, sticky duct tape!")
    if gmute(user.id) is False:
        await gspdr.edit(
            'Error! User probably already gmuted.\nRe-rolls the tape.')
    else:
           if reason:
            await gspdr.edit(f"Globally taped!Reason: {reason}")
        else:
            await gspdr.edit("Globally taped!")
