"""Emoji
Available Commands:
.sahil"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 31)

    input_str = event.pattern_match.group(1)

    if input_str == "sahil":

        await event.edit(input_str)

        animation_chars = [

            "👑sahil👑👑👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑",

            "◼️👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑",

            "◼️◼️👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑",

            "◼️◼️◼️️👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑",

            "◼️◼️◼️◼️👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑",

            "‎◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑👑sahil👑",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑sahil👑👑sahil👑👑sahil👑👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑sahil👑👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑sahil👑👑sahil👑◼️◼️\n◼️👑sahil👑👑sahil👑👑sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑sahil👑👑sahil👑◼️◼️\n◼️👑sahil👑👑sahil👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑sahil👑👑sahil👑◼️◼️\n◼️👑sahil👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑sahil👑👑sahil👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑sahil👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            
            "👑 sahil 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
