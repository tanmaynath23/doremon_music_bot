import pyrogram.raw.types
import pyrogram.errors

# ye sab missing cheezo ko auto-create kar dega
def _patch_missing(name, module):
    if not hasattr(module, name):
        setattr(module, name, type(name, (Exception,), {}))

# Raw types patch
if not hasattr(pyrogram.raw.types, 'InputGroupCallSlug'):
    pyrogram.raw.types.InputGroupCallSlug = type('InputGroupCallSlug', (), {})

# Errors patch - saare Groupcall wale
for err_name in ['GroupcallInvalid', 'GroupcallForbidden', 'GroupcallNotModified', 'GroupcallAlreadyJoined', 'GroupcallJoinMissing']:
    _patch_missing(err_name, pyrogram.errors)

from pytgcalls import PyTgCalls
from core.userbot import user

pytg = PyTgCalls(user)
