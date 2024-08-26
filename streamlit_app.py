import streamlit as st
import socket
from streamlit.web.server.websocket_headers import _get_websocket_headers

headers = _get_websocket_headers()
st.write(headers)

# def get_local_ip():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("8.8.8.8", 80))
#         ip = s.getsockname()[0]
#         s.close()
#         return ip
#     except Exception:
#         return "No IP."

# st.title("IP 주소 확인")
# ip = get_local_ip()
# st.write(f"IP 주소: {ip}")
