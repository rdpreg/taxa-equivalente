import streamlit as st

def calcular_taxa_equivalente(taxa, n1, n2):
    i1 = taxa / 100
    i2 = (1 + i1) ** (n2 / n1) - 1
    return round(i2 * 100, 4)

st.set_page_config(page_title="Calculadora de Taxa Equivalente", layout="centered")
st.title("📈 Cálculo de Taxa Equivalente")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        taxa = st.number_input("Taxa de juros", min_value=0.0, format="%.4f", step=0.01)
    with col2:
        periodo_de = st.number_input("Período (de)", min_value=1, step=1, format="%d")

    col3, col4 = st.columns(2)
    with col3:
        taxa_equivalente_output = st.number_input("Taxa equivalente", value=0.0, format="%.4f", step=0.01, disabled=True)
    with col4:
        periodo_para = st.number_input("Período (para)", min_value=1, step=1, format="%d")

    col5, col6, col7 = st.columns([6, 1, 1])
    with col6:
        if st.button("CALCULAR"):
            resultado = calcular_taxa_equivalente(taxa, periodo_de, periodo_para)
            st.experimental_set_query_params(taxa_equivalente=resultado)
            st.experimental_rerun()
    with col7:
        if st.button("LIMPAR"):
            st.experimental_set_query_params()
            st.experimental_rerun()

# Mostrar taxa equivalente ao recarregar (mantém após cálculo)
query_params = st.experimental_get_query_params()
if "taxa_equivalente" in query_params:
    taxa_equivalente = float(query_params["taxa_equivalente"][0])
    st.session_state["taxa_equivalente"] = taxa_equivalente
    st.session_state["Taxa equivalente"] = taxa_equivalente
    st.session_state["taxa_equivalente_output"] = taxa_equivalente
