import streamlit as st
import sympy as sp

# Configurar página
st.set_page_config(page_title="Calculadora La Solución", layout="centered")

# Fondo profesional con estilo CSS (claro)
st.markdown("""
    <style>
        html, body {
            background-color: #f4f6f9;
        }
        .stApp {
            font-family: 'Segoe UI', sans-serif;
            color: #333;
        }
        .resultado-box {
            background-color: #ffffff;
            padding: 20px;
            border: 2px solid #007acc;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color:#007acc;'>Calculadora La Solución</h1>
        <p style='font-size: 18px;'>Herramienta académica para resolver funciones, derivadas, integrales y límites paso a paso</p>
    </div>
""", unsafe_allow_html=True)

# Inputs
col1, col2 = st.columns(2)
with col1:
    expresion = st.text_input("✍️ Ingresa una expresión matemática:", placeholder="Ej: x**2 + 3*x")
with col2:
    operacion = st.selectbox("📌 Selecciona una operación:", ["Evaluar", "Derivada", "Integral", "Límite"])

x = sp.symbols('x')

# Botón de acción
if st.button("🔍 Calcular"):
    try:
        funcion = sp.sympify(expresion)
        pasos = ""
        if operacion == "Evaluar":
            valor = st.number_input("🔢 Ingresa el valor de x:", value=1.0)
            resultado = funcion.evalf(subs={x: valor})
            pasos = f"Se sustituyó x = {valor} en la expresión y se obtuvo: {resultado}"
        elif operacion == "Derivada":
            derivada = sp.diff(funcion, x)
            resultado = derivada
            pasos = f"Se derivó la expresión {funcion} y se obtuvo: {derivada}"
        elif operacion == "Integral":
            integral = sp.integrate(funcion, x)
            resultado = integral
            pasos = f"Se calculó la integral indefinida de {funcion} y se obtuvo: {integral} + C"
        elif operacion == "Límite":
            punto = st.number_input("📍 ¿Hacia qué valor tiende x?", value=0.0)
            limite = sp.limit(funcion, x, punto)
            resultado = limite
            pasos = f"Se calculó el límite de {funcion} cuando x → {punto} y se obtuvo: {limite}"

        # Mostrar resultado tipo recibo
        st.markdown(f"""
            <div class='resultado-box'>
                <h4>🧾 Resultado:</h4>
                <p><strong>{resultado}</strong></p>
                <hr>
                <p style='font-size:14px;'><strong>Explicación:</strong><br>{pasos}</p>
            </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Hubo un error al procesar la expresión: {e}")

# Pie de página
st.markdown("---")
st.markdown("""
    <div style='text-align:center; font-size:13px; color:gray;'>
        Desarrollado para uso académico | Universidad Privada Domingo Savio – 2025
    </div>
""", unsafe_allow_html=True)