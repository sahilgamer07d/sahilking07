"""Emoji
Available Commands:
.ayush"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 31)

    input_str = event.pattern_match.group(1)

    if input_str == "ayush:

        await event.edit(input_str)

        animation_chars = [

            "👑AYUSH👑👑👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑",

            "◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑",

            "◼️◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑",

            "◼️◼️◼️️👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑",

            "◼️◼️◼️◼️👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑",

            "‎◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑AYUSH👑👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑AYUSH👑👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑AYUSH👑👑AYUSH👑◼️◼️\n◼️👑AYUSH👑👑AYUSH👑👑AYUSH👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑AYUSH👑👑AYUSH👑◼️◼️\n◼️👑AYUSH👑👑AYUSH👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑AYUSH👑👑AYUSH👑◼️◼️\n◼️👑AYUSH👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑AYUSH👑👑AYUSH👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑AYUSH👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            
            "👑 AYUSH 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
