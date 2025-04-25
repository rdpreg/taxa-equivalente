import streamlit as st

def calcular_taxa_equivalente(taxa, n1, n2):
    i1 = taxa / 100
    i2 = (1 + i1) ** (n2 / n1) - 1
    return round(i2 * 100, 4)

st.set_page_config(page_title="Calculadora de Taxa Equivalente", layout="centered")

# Pequeno ajuste visual para o campo de taxa equivalente
st.markdown("""
    <style>
    div[data-testid="stNumberInput"] input[readonly] {
        border: 2px solid #cccccc;
        background-color: #f9f9f9;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("📈 Cálculo de Taxa Equivalente")

# Inputs
col1, col2 = st.columns(2)
with col1:
    taxa = st.number_input("Taxa de juros (%)", min_value=0.0, format="%.2f")
with col2:
    periodo_de = st.number_input("Período (de)", min_value=1, format="%d")

col3, col4 = st.columns(2)
with col3:
    periodo_para = st.number_input("Período (para)", min_value=1, format="%d")

resultado = 0.0
col_a, col_b, col_c = st.columns([5, 1.5, 1.5])
with col_b:
    if st.button("CALCULAR"):
        resultado = calcular_taxa_equivalente(taxa, periodo_de, periodo_para)
with col_c:
    if st.button("LIMPAR"):
        st.rerun()

# Campo de resultado
with col4:
    st.number_input("Taxa equivalente", value=resultado, format="%.4f", key="resultado_visual")
