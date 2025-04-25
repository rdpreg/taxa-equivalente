import streamlit as st

def calcular_taxa_equivalente(taxa, n1, n2):
    i1 = taxa / 100
    i2 = (1 + i1) ** (n2 / n1) - 1
    return round(i2 * 100, 4)

# Layout
st.set_page_config(page_title="Calculadora de Taxa Equivalente", layout="centered")

# CSS personalizado
st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: flex-end;
        gap: 0.75rem;
        margin-top: 1rem;
    }

    .stButton > button {
        font-weight: 600;
        padding: 0.6em 1.5em;
        border-radius: 6px;
        min-width: 130px;
        white-space: nowrap;
    }

    .stButton.calcular > button {
        background-color: #0067c1;
        color: white;
        border: none;
    }

    .stButton.calcular > button:hover {
        background-color: #0059a8;
    }

    .stButton.limpar > button {
        background-color: white;
        color: #0067c1;
        border: 2px solid #0067c1;
    }

    .stButton.limpar > button:hover {
        background-color: #f1f8ff;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("""
    <h2 style='display: flex; align-items: center; gap: 10px;'>
        <img src="https://emojicdn.elk.sh/📈" width="30"/> 
        <span style='color: #222;'>Cálculo de Taxa Equivalente</span>
    </h2>
""", unsafe_allow_html=True)

# Inputs
col1, col2 = st.columns(2)
with col1:
    taxa = st.number_input("Taxa de juros (%)", min_value=0.0, format="%.4f", step=0.01)
with col2:
    periodo_de = st.number_input("Período (de)", min_value=1, step=1, format="%d")

col3, col4 = st.columns(2)
with col3:
    taxa_equivalente = st.session_state.get("taxa_equivalente", 0.0)
    st.number_input("Taxa equivalente", value=taxa_equivalente, format="%.4f", step=0.01, disabled=True)
with col4:
    periodo_para = st.number_input("Período (para)", min_value=1, step=1, format="%d")

# Botões no canto inferior direito
col5, col6, col7 = st.columns([6, 1, 1])
with col6:
    with st.container():
        btn_calcular = st.button("CALCULAR", key="calcular_btn")
with col7:
    with st.container():
        btn_limpar = st.button("LIMPAR", key="limpar_btn")

# Aplicar classes de estilo usando script
st.markdown("""
    <script>
    const buttons = window.parent.document.querySelectorAll("button");
    buttons.forEach(btn => {
        if (btn.innerText === "CALCULAR") {
            btn.parentElement.classList.add("calcular");
        }
        if (btn.innerText === "LIMPAR") {
            btn.parentElement.classList.add("limpar");
        }
    });
    </script>
""", unsafe_allow_html=True)

# Lógica dos botões
if btn_calcular:
    resultado = calcular_taxa_equivalente(taxa, periodo_de, periodo_para)
    st.session_state["taxa_equivalente"] = resultado

if btn_limpar:
    st.session_state.clear()
    st.experimental_rerun()
