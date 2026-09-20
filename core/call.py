# FIX for Render - missing imports patch
import pyrogram.raw.types
import pyrogram.errors

# Patch 1: InputGroupCallSlug
if not hasattr(pyrogram.raw.types, 'InputGroupCallSlug'):
    pyrogram.raw.types.InputGroupCallSlug = type('InputGroupCallSlug', (), {})

# Patch 2: GroupcallForbidden
if not hasattr(pyrogram.errors, 'GroupcallForbidden'):
    class GroupcallForbidden(Exception):
        pass
    pyrogram.errors.GroupcallForbidden = GroupcallForbidden

# Ab asli import
from pytgcalls import PyTgCalls
from core.userbot import user

pytg = PyTgCalls(user)
