"""Use fire `.fire` to brun it"""

from telethon import events

import asyncio

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 200)

    input_str = event.pattern_match.group(1)

    if input_str == "fire":

        await event.edit(input_str)

        animation_chars = [

            "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥🔥",
            "🔥🔥🔥🔥",
            "🔥🔥🔥",
            "🔥🔥",
            "🔥"

  ]

for i in animation_ttl:
await event.edit(animation_chars[i % 14])
