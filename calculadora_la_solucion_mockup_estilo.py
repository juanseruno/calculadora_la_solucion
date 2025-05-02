import streamlit as st
import sympy as sp

st.set_page_config(page_title="Calculadora La Solución", layout="centered")

# Estilos personalizados inspirados en mockup
st.markdown("""
<style>
body {
    background-color: #e8f1fc;
}
.card {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.result-highlight {
    background-color: #ffe066;
    padding: 10px 15px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 22px;
    color: #000;
    text-align: center;
    margin-bottom: 10px;
}
.steps {
    background-color: #f5faff;
    border-radius: 8px;
    padding: 15px;
    font-size: 16px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# Contenedor principal
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("### 📘 Calculadora La Solución")
st.markdown("*Resuelve funciones, derivadas, integrales y límites paso a paso*")

# Entrada de función y operación
expresion = st.text_input("Ingresa una función:", placeholder="Ej: x**2 + 3*x")
operacion = st.selectbox("Selecciona la operación", ["Derivada", "Integral", "Límite", "Evaluar"])

x = sp.symbols('x')

if st.button("📌 Resolver"):
    try:
        funcion = sp.sympify(expresion)
        resultado = ""
        pasos = []

        if operacion == "Evaluar":
            valor = st.number_input("Valor de x:", value=1.0)
            resultado = funcion.evalf(subs={x: valor})
            pasos.append(f"1. Se sustituye x = {valor} en la expresión.")
            pasos.append(f"2. Resultado final: {resultado}")
        elif operacion == "Derivada":
            derivada = sp.diff(funcion, x)
            resultado = derivada
            pasos.append(f"1. Se identifica cada término de la expresión {funcion}.")
            pasos.append(f"2. Se aplica la regla de derivación.")
            pasos.append(f"3. Resultado final: {derivada}")
        elif operacion == "Integral":
            integral = sp.integrate(funcion, x)
            resultado = integral
            pasos.append(f"1. Se aplica la integral indefinida sobre {funcion}.")
            pasos.append(f"2. Resultado: {integral} + C")
        elif operacion == "Límite":
            punto = st.number_input("Límite cuando x tiende a:", value=0.0)
            limite = sp.limit(funcion, x, punto)
            resultado = limite
            pasos.append(f"1. Se analiza el comportamiento de {funcion} cuando x → {punto}.")
            pasos.append(f"2. Resultado final del límite: {limite}")

        # Mostrar resultado destacado
        st.markdown("<br><div class='result-highlight'>Resultado: " + str(resultado) + "</div>", unsafe_allow_html=True)

        # Mostrar pasos explicativos
        st.markdown("#### Resultado de la operación paso a paso:")
        st.markdown("<div class='steps'>" + "<br>".join(pasos) + "</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error al procesar la expresión: {e}")

# Cierre del contenedor
st.markdown("</div>", unsafe_allow_html=True)

# Pie
st.markdown("---")
st.markdown("<div style='text-align:center; color:gray; font-size:13px;'>Universidad Privada Domingo Savio - Proyecto académico 2025</div>", unsafe_allow_html=True)