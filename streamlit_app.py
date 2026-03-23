import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="Generador de QR", page_icon="🔳")

st.title("Generador de códigos QR")

texto = st.text_input("Escribe un texto o URL", "https://example.com")

if texto:
qr = qrcode.QRCode(
version=1,
box_size=10,
border=4
)
qr.add_data(texto)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

st.image(img, caption="Código QR generado", use_container_width=False)

buffer = BytesIO()
img.save(buffer, format="PNG")

st.download_button(
label="Descargar QR en PNG",
data=buffer.getvalue(),
file_name="codigo_qr.png",
mime="image/png"
)
