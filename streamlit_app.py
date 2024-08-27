# import streamlit as st
# import socket
# from streamlit.web.server.websocket_headers import _get_websocket_headers

# headers = _get_websocket_headers()
# st.write(headers)

# # def get_local_ip():
# #     try:
# #         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #         s.connect(("8.8.8.8", 80))
# #         ip = s.getsockname()[0]
# #         s.close()
# #         return ip
# #     except Exception:
# #         return "No IP."

# st.title("IP 주소 확인")
# # ip = get_local_ip()
# # st.write(ip)
# # st.write(f"IP 주소: {ip}")

from st_socketio import sio, st_socketio
import streamlit as st

@sio.on('chat')
async def chat_event(sid, data, auth):
    print('chat ', sid, data, auth)
    await sio.emit('chat', data[::-1], sid);
    return "OK", sid

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)
    #print(environ)
    #print(auth)
    await sio.emit('chat', 'connected', sid);

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)

#@st_socketio(path=r'/socket.io/')
@st_socketio(path=r'/ws/')
def socket_io_handler(path: str):
    pass
