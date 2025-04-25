import streamlit as st

def calcular_taxa_equivalente(taxa, n1, n2):
    i1 = taxa / 100
    i2 = (1 + i1) ** (n2 / n1) - 1
    return round(i2 * 100, 4)

st.set_page_config(page_title="Calculadora de Taxa Equivalente", layout="centered")

st.markdown(
    """
    <h2 style='display: flex; align-items: center; gap: 10px;'>
        <img src="https://emojicdn.elk.sh/📈" width="30"/> 
        <span style='color: #222;'>Cálculo de Taxa Equivalente</span>
    </h2>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:
    taxa = st.number_input("Taxa de juros", min_value=0.0, format="%.4f", step=0.01)
with col2:
    periodo_de = st.number_input("Período (de)", min_value=1, step=1, format="%d", help="Ex: 12 para mensal, 1 para anual")

col3, col4 = st.columns(2)
with col3:
    taxa_equivalente = st.session_state.get("taxa_equivalente", 0.0)
    st.number_input("Taxa equivalente", value=taxa_equivalente, format="%.4f", step=0.01, disabled=True)
with col4:
    periodo_para = st.number_input("Período (para)", min_value=1, step=1, format="%d", help="Ex: 1 para anual, 12 para mensal")

# Botões com estilo customizado
col5, col6, col7 = st.columns([6, 1, 1])
with col6:
    calcular_clicked = st.markdown(
        """
        <style>
        .calc-btn {
            background-color: #0067c1;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            text-align: center;
        }
        .calc-btn:hover {
            background-color: #0059a8;
        }
        </style>
        <form action="" method="POST">
            <button class="calc-btn" name="calcular" type="submit">CALCULAR</button>
        </form>
        """,
        unsafe_allow_html=True
    )
with col7:
    limpar_clicked = st.markdown(
        """
        <style>
        .limpar-btn {
            background-color: white;
            color: #0067c1;
            padding: 10px 20px;
            border: 2px solid #0067c1;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            text-align: center;
        }
        .limpar-btn:hover {
            background-color: #f1f8ff;
        }
        </style>
        <form action="" method="POST">
            <button class="limpar-btn" name="limpar" type="submit">LIMPAR</button>
        </form>
        """,
        unsafe_allow_html=True
    )

# Lógica de clique dos botões (sem HTML)
if st.session_state.get("calcular_btn") or st.query_params.get("calcular") is not None:
    resultado = calcular_taxa_equivalente(taxa, periodo_de, periodo_para)
    st.session_state["taxa_equivalente"] = resultado
    st.experimental_rerun()

if st.session_state.get("limpar_btn") or st.query_params.get("limpar")_
