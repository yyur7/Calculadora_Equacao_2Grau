# importação de bibliotecas
 
import streamlit as st  # front end
import numpy as np  # Biblioteca de Notação Científica
import matplotlib.pyplot as plt  # Construção de Gráficos
import math
 
st.set_page_config(
    page_title="Calculadora de Equação do 2° Grau",
    page_icon="📊",
    layout="centered"
)
 
# iniciando variáveis
 
if 'a' not in st.session_state:
    st.session_state.a = 1.0
 
if 'b' not in st.session_state:
    st.session_state.b = 0.0
 
if 'c' not in st.session_state:
    st.session_state.c = 0.0
 
def limpar():
    st.session_state.a = 1.0
    st.session_state.b = 0.0
    st.session_state.c = 0.0
 
# interface
 
st.title("Calculadora de Equação do 2° Grau")
st.latex(r"ax^2+bx+c=0")
st.write("Informe os coeficientes da equação: ")
a = st.number_input('Coeficiente A', key="a")
b = st.number_input('Coeficiente B', key="b")
c = st.number_input('Coeficiente C', key="c")
 
col1, col2 = st.columns(2)
 
with col1:
    calcular = st.button("Calcular")
with col2:
    st.button("Novo Cálculo", on_click=limpar)
 
# Cálculo
 
if calcular:
    if a == 0:
        st.error("O coeficiente 'a' deve ser diferente de 0")
    else:
        delta = b**2 - 4*a*c
 
        st.subheader("Resultado")
        st.write(f"Δ = {delta:.2f}")
 
        X1 = None
        X2 = None
 
        if delta < 0:
            st.warning("Não existe raiz Real")
        elif delta == 0:
            X1 = -b / (2*a)
            st.success("A Equação possui uma raiz real (dupla)")
            st.write(f"X1 = X2 = {X1:.2f}")
        else:
            X1 = (-b + math.sqrt(delta)) / (2*a)
            X2 = (-b - math.sqrt(delta)) / (2*a)
            st.success("A Equação possui raízes reais distintas")
            st.write(f"X1 = {X1:.2f}")
            st.write(f"X2 = {X2:.2f}")

# Gráfico