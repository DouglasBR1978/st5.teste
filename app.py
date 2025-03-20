import streamlit as st

st.set_page_config(page_title="Gestão de clientes", page_icon="📓")

consulta_page = st.Page("pages/consulta.py", title="Consulta", icon=":material/list:")
registro_page = st.Page(
    "pages/registro.py", title="Cadastro", icon=":material/add_circle:"
)


pg = st.navigation([consulta_page, registro_page])
pg.run()
