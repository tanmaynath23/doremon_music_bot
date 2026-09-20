import sys
import pyrogram.raw.types as raw_types
import pyrogram.errors as err

# --- AUTO PATCH: jo bhi naam missing ho dummy bana dega ---
def _raw_getattr(name):
    return type(name, (), {})

def _err_getattr(name):
    return type(name, (Exception,), {})

# ye magic hai, koi bhi missing import ab error nahi dega
if not hasattr(raw_types, '__getattr__'):
    raw_types.__getattr__ = _raw_getattr
else:
    orig = raw_types.__getattr__
    def new_raw_getattr(name):
        try:
            return orig(name)
        except (AttributeError, ImportError):
            return type(name, (), {})
    raw_types.__getattr__ = new_raw_getattr

if not hasattr(err, '__getattr__'):
    err.__getattr__ = _err_getattr

# specific wale bhi
if not hasattr(raw_types, 'InputGroupCallSlug'):
    raw_types.InputGroupCallSlug = type('InputGroupCallSlug', (), {})

from pytgcalls import PyTgCalls
from core.userbot import user

pytg = PyTgCalls(user)
