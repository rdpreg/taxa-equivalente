import streamlit as st

def calcular_taxa_equivalente(taxa, n1, n2):
    i1 = taxa / 100
    i2 = (1 + i1) ** (n2 / n1) - 1
    return round(i2 * 100, 4)

st.set_page_config(page_title="Calculadora de Taxa Equivalente", layout="centered")
st.title("📈 Cálculo de Taxa Equivalente")

# Inputs
col1, col2 = st.columns(2)
with col1:
    taxa = st.number_input("Taxa de juros (%)", min_value=0.0, format="%.2f")
with col2:
    periodo_de = st.number_input("Período (de)", min_value=1, format="%d")

col3, col4 = st.columns(2)
with col4:
    periodo_para = st.number_input("Período (para)", min_value=1, format="%d")

# Resultado será calculado e exibido em tempo real após clique
resultado = None
if "resultado" in st.session_state:
    resultado = st.session_state["resultado"]

# Botões alinhados
col_a, col_b, col_c = st.columns([5, 1.5, 1.5])
with col_b:
    if st.button("CALCULAR"):
        resultado = calcular_taxa_equivalente(taxa, periodo_de, periodo_para)
        st.session_state["resultado"] = resultado
with col_c:
    if st.button("LIMPAR"):
        st.session_state.clear()
        st.rerun()

# Exibição do resultado
col_res, _ = st.columns([0.5, 0.5])
with col_res:
    st.number_input("Taxa equivalente", value=resultado or 0.0, format="%.4f", disabled=True)
