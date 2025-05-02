import streamlit as st
import sympy as sp

# Configuración de página
st.set_page_config(page_title="Calculadora La Solución", layout="centered")

# Estilo de fondo con imagen
st.markdown("""
<style>
body {
    background-image: url("https://i.imgur.com/h1zC8sZ.png");
    background-size: cover;
}
</style>
""", unsafe_allow_html=True)

# Encabezado con logo y título
st.image("https://i.imgur.com/9p1smVJ.png", width=120)
st.markdown("""
    <div style='text-align: center; padding: 10px; background-color: #f8f9fa; border-radius: 10px;'>
        <h1 style='color: #333;'>🧠 Calculadora <span style="color:#FF4B4B;">La Solución</span></h1>
        <p style='font-size: 18px; color: #666;'>Resuelve funciones, derivadas, integrales y límites paso a paso</p>
    </div>
""", unsafe_allow_html=True)

# Entrada de datos
col1, col2 = st.columns(2)

with col1:
    expresion = st.text_input("✍️ Ingresa una expresión (ej: x**2 + 3*x):", key="exp")
with col2:
    operacion = st.selectbox("📌 Elige una operación:", ["Evaluar", "Derivada", "Integral", "Límite"], key="op")

x = sp.symbols('x')

if st.button("🔍 Resolver"):
    try:
        funcion = sp.sympify(expresion)
        pasos = ""
        if operacion == "Evaluar":
            valor = st.number_input("Valor de x para evaluar:", value=1.0)
            resultado = funcion.evalf(subs={x: valor})
            pasos = f"Sustituimos x = {valor} en la expresión y obtenemos: {resultado}"
        elif operacion == "Derivada":
            derivada = sp.diff(funcion, x)
            resultado = derivada
            pasos = f"Aplicamos la derivada a {funcion}: Resultado = {derivada}"
        elif operacion == "Integral":
            integral = sp.integrate(funcion, x)
            resultado = integral
            pasos = f"Se calcula la integral de {funcion}: Resultado = {integral} + C"
        elif operacion == "Límite":
            punto = st.number_input("Límite cuando x tiende a:", value=0.0)
            limite = sp.limit(funcion, x, punto)
            resultado = limite
            pasos = f"Se evalúa el límite de {funcion} cuando x → {punto}: Resultado = {limite}"
        
        st.success(f"✅ Resultado: {resultado}")
        with st.expander("🧾 Ver pasos explicativos"):
            st.code(pasos)

    except Exception as e:
        st.error(f"❌ Error: {e}")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #999; font-size: 14px;'>
    Creado por <b>Calculadora La Solución</b> | Proyecto académico 2025
</div>
""", unsafe_allow_html=True)