import pyrogram.errors
for _n in ["GroupcallForbidden","GroupCallForbidden","GroupcallInvalid","GroupCallInvalid","GroupcallNotModified","GroupCallNotModified","GroupCallDiscarded"]:
    if not hasattr(pyrogram.errors, _n):
        setattr(pyrogram.errors, _n, type(_n, (Exception,), {}))

from pytgcalls import PyTgCalls
from core.userbot import user
pytg = PyTgCalls(user)
