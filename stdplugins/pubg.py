"""COMMAND : ./pubg"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "/pubg":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To PUBG Headquarters...`",
            "`Call Connected.`",
            "`PUBG Headquarters: Hello This is PUBG HQ. Who is this?`",
            "`Me: Yo this is` @AyushChatterjee.`People call me Dr.Anonymous`,`Please Connect me to Mr.David Johnson(Senior Incharge)`",
            "`User Authorised.`",
            "`Calling Mr.David Johnson At +12374441839`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Unban This PUBG Id (5147816390).`",    
            "`David: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @AyushChatterjee,`You may ask Brendan Greene about my name`",
            "`David: OMG!!! I Am FAN Of You Sir...\nI'll Make Sure That Account Will Be Unbanned Within 2Hrs With All Of Its Stats Maintained.`",
            "`David: May I Know Why Was Your Account Banned ?`",
            "`Me: Ya Brah For Hacking`",
            "`David: Ohh, Sir We Are Extremely Sorry We'll Never Ban Your Account Again.Now You Can Apply Hacks Without Any Protection`",
            "`Me: Thanks, See You Later Brah.`",
            "`Daviv: Please Don't Thank Sur, PUBG Is Your's. Just Gimme A Call When You Be Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`David: Yes Sur, There Is A Bug In PUBG v16.0\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`David: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 22])
