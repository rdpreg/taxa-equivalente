import streamlit as st

def calcular_taxa_equivalente(taxa, n1, n2):
    i1 = taxa / 100
    i2 = (1 + i1) ** (n2 / n1) - 1
    return round(i2 * 100, 4)

# Layout da página
st.set_page_config(page_title="Calculadora de Taxa Equivalente", layout="centered")

# CSS para customizar botões
st.markdown("""
    <style>
    div.stButton > button {
        font-weight: 600;
        padding: 0.6em 1.5em;
        border-radius: 6px;
    }

    /* Botão CALCULAR (primeiro botão dentro da div) */
    div.stButton:nth-child(1) > button {
        background-color: #0067c1;
        color: white;
        border: none;
    }

    div.stButton:nth-child(1) > button:hover {
        background-color: #0059a8;
    }

    /* Botão LIMPAR (segundo botão) */
    div.stButton:nth-child(2) > button {
        background-color: white;
        color: #0067c1;
        border: 2px solid #0067c1;
    }

    div.stButton:nth-child(2) > button:hover {
        background-color: #f1f8ff;
    }
    </style>
""", unsafe_allow_html=True)

# Título com emoji
st.markdown(
    """
    <h2 style='display: flex; align-items: center; gap: 10px;'>
        <img src="https://emojicdn.elk.sh/📈" width="30"/> 
        <span style='color: #222;'>Cálculo de Taxa Equivalente</span>
    </h2>
    """,
    unsafe_allow_html=True
)

# Inputs
col1, col2 = st.columns(2)
with col1:
    taxa = st.number_input("Taxa de juros", min_value=0.0, format="%.4f", step=0.01)
with col2:
    periodo_de = st.number_input("Período (de)", min_value=1, step=1, format="%d")

col3, col4 = st.columns(2)
with col3:
    taxa_equivalente = st.session_state.get("taxa_equivalente", 0.0)
    st.number_input("Taxa equivalente", value=taxa_equivalente, format="%.4f", step=0.01, disabled=True)
with col4:
    periodo_para = st.number_input("Período (para)", min_value=1, step=1, format="%d")

# Botões alinhados à direita
col5, col6, col7 = st.columns([6, 1, 1])
with col6:
    if st.button("CALCULAR"):
        resultado = calcular_taxa_equivalente(taxa, periodo_de, periodo_para)
        st.session_state["taxa_equivalente"] = resultado
with col7:
    if st.button("LIMPAR"):
        st.session_state.clear()
        st.experimental_rerun()
