# DISCLAIMER
# This is Public Domain provided by sefgit
# Used it "AS IS" on your own responsibility
# ------------------------------------------
import gc
import asyncio
from typing import Optional, Callable
from socketio import AsyncServer, get_tornado_handler
from streamlit.runtime import Runtime
from tornado.web import Application

sio = AsyncServer(
        async_mode='tornado', 
        cors_allowed_origins='*'  # !!! IMPORTANT !!!
      )

class _SocketioRegister:
    @classmethod
    def instance(cls, path:str) -> '_SocketioRegister':
        inst: Runtime = Runtime.instance()
        res: Optional[_SocketioRegister] = getattr(inst, '_streamlit_socketio_register', None)
        if res is None:
            res = _SocketioRegister()
            setattr(inst, '_streamlit_socketio_register', res)
            print(f'  Mounting Socket.IO on {path}')            
            app: Application = next(iter((k for k in gc.get_referrers(Application) if isinstance(k, Application))))
            _handler = get_tornado_handler(sio)
            app.add_handlers(".*", [(path, _handler)])            
        return res

def st_socketio(path: str):
    def wrap(f: Callable):
        rr: _SocketioRegister = _SocketioRegister.instance(path)
        return f
    return wrap
