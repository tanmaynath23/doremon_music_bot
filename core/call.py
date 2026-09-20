import pyrogram.raw.types
import pyrogram.errors
if not hasattr(pyrogram.raw.types, 'InputGroupCallSlug'):
    pyrogram.raw.types.InputGroupCallSlug = type('InputGroupCallSlug', (), {})
for n in ['GroupcallInvalid','GroupcallForbidden','GroupcallNotModified','GroupcallAlreadyJoined','GroupcallJoinMissing']:
    if not hasattr(pyrogram.errors, n):
        setattr(pyrogram.errors, n, type(n, (Exception,), {}))

from pytgcalls import PyTgCalls
from core.userbot import user
pytg = PyTgCalls(user)
