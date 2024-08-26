import streamlit as st
import socket
from streamlit.web.server.websocket_headers import _get_websocket_headers

cookies = cookie_manager.get_all()
cookies = cookie_manager.get_all()
st.write(cookies)

def open(self):
    # self.request.remote_ip contains the IP address of the user connecting
    # to the Streamlit app. You could send this to an analytics platform like MixPanel
    ip = self.request.remote_ip
    self._session = self._server._create_report_session(self)
    st.write(ip)

# headers = _get_websocket_headers()
# st.write(headers)

# def get_local_ip():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("8.8.8.8", 80))
#         ip = s.getsockname()[0]
#         s.close()
#         return ip
#     except Exception:
#         return "No IP."

st.title("IP 주소 확인")
# ip = get_local_ip()
open()
# st.write(ip)
# st.write(f"IP 주소: {ip}")
