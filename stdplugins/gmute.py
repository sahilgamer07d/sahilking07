"""
G-Muter Plugin for userbot. //
cmds: .gmute user_id|reply to user messsage	//G-Mutes a User.
	  .ungmute user_id|reply to user messsage //Un-Gmutes a User.
	  .listgmuted //List Currently G-Muted Users.

By:- AyushChatterjee 


"""
from telethon import events
import logging
import asyncio
import sqlalchemy
import sys
from uniborg.util import admin_cmd
try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String, UnicodeText


class GMute(BASE):
    __tablename__ = "gmute"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


GMute.__table__.create(checkfirst=True)


def is_gmuted(sender_id):
    try:
        return SESSION.query(GMute).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def gmute(sender):
    adder = GMute(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def ungmute(sender):
    rem = SESSION.query(GMute).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
