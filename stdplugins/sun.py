# (c) @UniBorg
# Original edit by @AyushChatterjee
""".sun Plugin for @BotHub"""


from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.sun", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("☀️☀️☀️☀️☀️☀️☀️☀️"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
