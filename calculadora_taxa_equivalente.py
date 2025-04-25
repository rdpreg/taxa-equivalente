import streamlit as st

def calcular_taxa_equivalente(taxa, n1, n2):
    i1 = taxa / 100
    i2 = (1 + i1) ** (n2 / n1) - 1
    return round(i2 * 100, 4)

st.set_page_config(page_title="Calculadora de Taxa Equivalente", layout="centered")

# CSS para botão + espaçamento real entre os dois
st.markdown("""
    <style>
    .button-row {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
        margin-top: 20px;
    }

    .button-row button {
        font-weight: 600 !important;
        padding: 10px 24px;
        border-radius: 6px;
        min-width: 130px;
        white-space: nowrap;
        font-size: 15px;
    }

    .button-row button.calc {
        background-color: #0067c1;
        color: white;
        border: none;
    }

    .button-row button.calc:hover {
        background-color: #0059a8;
    }

    .button-row button.limpar {
        background-color: white;
        color: #0067c1;
        border: 2px solid #0067c1;
    }

    .button-row button.limpar:hover {
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

# Botões com espaçamento real via HTML
col_botao = st.container()
with col_botao:
    col_botao.markdown("""
        <div class="button-row">
            <form action="?action=calcular" method="post">
                <button class="calc" type="submit">CALCULAR</button>
            </form>
            <form action="?action=limpar" method="post">
                <button class="limpar" type="submit">LIMPAR</button>
            </form>
        </div>
    """, unsafe_allow_html=True)

# Captura da ação dos botões HTML (via query param)
query_params = st.experimental_get_query_params()
acao = query_params.get("action", [None])[0]

if acao == "calcular":
    resultado = calcular_taxa_equivalente(taxa, periodo_de, periodo_para)
    st.session_state["taxa_equivalente"] = resultado
    st.experimental_set_query_params()  # limpa a URL

elif acao == "limpar":
    st.session_state.clear()
    st.experimental_set_query_params()  # limpa a URL
    st.experimental_rerun()
