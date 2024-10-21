import streamlit as st 
import webbrowser


st.write("### Acompanhamento São Luís 🌴 (Maranhão) - Mottu")
st.sidebar.markdown("Desenvolvido por [Éaco Rocha](https://github.com/Rxz1Eaco)")
button = st.button("Acesse Mottu Store")
if button:
    webbrowser.open_new_tab("https://www.loja.mottu.com.br/")
