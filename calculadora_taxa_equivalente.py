import streamlit as st

def calcular_taxa_equivalente(taxa, n1, n2):
    i1 = taxa / 100
    i2 = (1 + i1) ** (n2 / n1) - 1
    return round(i2 * 100, 4)

# Layout
st.set_page_config(page_title="Calculadora de Taxa Equivalente", layout="centered")
st.title("📈 Cálculo de Taxa Equivalente")

col1, col2 = st.columns(2)
with col1:
    taxa = st.number_input("Taxa de juros (%)", min_value=0.0, format="%.4f")
    resultado_area = st.empty()
with col2:
    periodo_de = st.number_input("Período (de)", min_value=1, step=1, format="%d")

col3, col4 = st.columns(2)
with col3:
    periodo_para = st.number_input("Período (para)", min_value=1, step=1, format="%d")
with col4:
    st.markdown("")

col5, col6 = st.columns([1, 1])
with col5:
    if st.button("CALCULAR"):
        resultado = calcular_taxa_equivalente(taxa, periodo_de, periodo_para)
        resultado_area.markdown(f"**{resultado:.4f} %**")
with col6:
    if st.button("LIMPAR"):
        st.experimental_rerun()
``
