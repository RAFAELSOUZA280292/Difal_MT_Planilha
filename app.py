import streamlit as st

st.set_page_config(page_title="Simulador DIFAL - Comparativo", layout="centered")
st.title("Simulador de ICMS DIFAL - Comparativo por Alíquota Interestadual")
st.markdown("Preencha os valores dos produtos para simular o DIFAL com diferentes alíquotas de ICMS interestadual. A alíquota interna de MT será fixada em 17%.")

# Alíquota interna de MT
aliquota_interna = 17.0

# Entrada dos valores dos produtos
valor_4 = st.number_input("Linha 1 - Valor do Produto com ICMS Interestadual de 4%", min_value=0.0, format="%.2f", key="valor_4")
valor_7 = st.number_input("Linha 2 - Valor do Produto com ICMS Interestadual de 7%", min_value=0.0, format="%.2f", key="valor_7")
valor_12 = st.number_input("Linha 3 - Valor do Produto com ICMS Interestadual de 12%", min_value=0.0, format="%.2f", key="valor_12")

def calcular_difal(valor, aliquota_interestadual):
    if valor == 0:
        return 0.0
    base_calculo = valor / (1 - (aliquota_interna / 100))  # cálculo por dentro
    icms_interno = base_calculo * (aliquota_interna / 100)
    icms_origem = valor * (aliquota_interestadual / 100)   # por fora
    difal = icms_interno - icms_origem
    return difal

if st.button("Calcular DIFAL"):
    difal_4 = calcular_difal(valor_4, 4.0)
    difal_7 = calcular_difal(valor_7, 7.0)
    difal_12 = calcular_difal(valor_12, 12.0)

    def format_brl(v):
        return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    st.markdown("### Resultado")
    st.write(f"**Linha 1 - ICMS 4%** → DIFAL: {format_brl(difal_4)}")
    st.write(f"**Linha 2 - ICMS 7%** → DIFAL: {format_brl(difal_7)}")
    st.write(f"**Linha 3 - ICMS 12%** → DIFAL: {format_brl(difal_12)}")
