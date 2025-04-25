import streamlit as st

# Mapeamento dos períodos para número de períodos no ano
periodos = {
    "Diário (252)": 252,
    "Mensal (12)": 12,
    "Bimestral (6)": 6,
    "Trimestral (4)": 4,
    "Semestral (2)": 2,
    "Anual (1)": 1
}

def calcular_taxa_equivalente(taxa, de, para):
    i1 = taxa / 100
    n1 = periodos[de]
    n2 = periodos[para]
    i2 = (1 + i1) ** (n2 / n1) - 1
    return round(i2 * 100, 4)

# Layout
st.set_page_config(page_title="Calculadora de Taxa Equivalente", layout="centered")
st.title("📈 Cálculo de Taxa Equivalente")

col1, col2 = st.columns(2)
with col1:
    taxa = st.number_input("Taxa de juros", min_value=0.0, format="%.4f")
with col2:
    periodo_de = st.selectbox("Período (de)", list(periodos.keys()))

col3, col4 = st.columns(2)
with col3:
    taxa_equivalente = st.empty()
with col4:
    periodo_para = st.selectbox("Período (para)", list(periodos.keys()))

col5, col6 = st.columns([1, 1])
with col5:
    if st.button("CALCULAR"):
        if periodo_de and periodo_para:
            resultado = calcular_taxa_equivalente(taxa, periodo_de, periodo_para)
            taxa_equivalente.text(f"{resultado:.4f} %")
with col6:
    if st.button("LIMPAR"):
        st.experimental_rerun()
