import streamlit as st
import sympy as sp

st.set_page_config(page_title="Calculadora La Solución", layout="centered")

# Estilos personalizados avanzados
st.markdown("""
<style>
body {
    background-color: #f0f2f5;
}
.container {
    background-color: #ffffff;
    border-radius: 15px;
    padding: 30px;
    max-width: 700px;
    margin: auto;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
h1 {
    color: #1a1a1a;
    font-size: 28px;
    text-align: center;
}
.sub {
    text-align: center;
    font-size: 16px;
    color: #666;
    margin-bottom: 25px;
}
.button {
    background-color: #007acc;
    color: white;
    border: none;
    padding: 10px 22px;
    font-size: 16px;
    border-radius: 8px;
    cursor: pointer;
}
.result-box {
    background-color: #eaf4ff;
    border-left: 5px solid #007acc;
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
}
.steps {
    background-color: #f9fcff;
    padding: 10px 18px;
    border-radius: 8px;
    margin-top: 10px;
    border-left: 3px solid #b3d9ff;
}
</style>
""", unsafe_allow_html=True)

# Layout principal
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<h1>Calculadora La Solución</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Resuelve funciones, derivadas, integrales y límites paso a paso</div>", unsafe_allow_html=True)

x = sp.symbols('x')
expresion = st.text_input("✏️ Ingresa una función matemática", placeholder="Ej: x**2 + 3*x")
operacion = st.selectbox("🔧 Selecciona una operación", ["Evaluar", "Derivada", "Integral", "Límite"])

if st.button("Calcular", type="primary"):
    try:
        funcion = sp.sympify(expresion)
        resultado = ""
        pasos = []

        if operacion == "Evaluar":
            valor = st.number_input("¿Qué valor tomará x?", value=1.0)
            resultado = funcion.evalf(subs={x: valor})
            pasos.append("1️⃣ Se sustituyó x = {} en la expresión.".format(valor))
            pasos.append(f"2️⃣ Resultado final: {resultado}")
        elif operacion == "Derivada":
            derivada = sp.diff(funcion, x)
            resultado = derivada
            pasos.append("1️⃣ Se derivó cada término de la función.")
            pasos.append(f"2️⃣ Resultado final: {derivada}")
        elif operacion == "Integral":
            integral = sp.integrate(funcion, x)
            resultado = integral
            pasos.append("1️⃣ Se integró la función respecto a x.")
            pasos.append(f"2️⃣ Resultado: {integral} + C")
        elif operacion == "Límite":
            punto = st.number_input("¿Hacia qué valor tiende x?", value=0.0)
            limite = sp.limit(funcion, x, punto)
            resultado = limite
            pasos.append(f"1️⃣ Se evaluó el límite cuando x → {punto}")
            pasos.append(f"2️⃣ Resultado: {limite}")

        st.markdown(f"<div class='result-box'><strong>📊 Resultado:</strong><br>{resultado}</div>", unsafe_allow_html=True)

        st.markdown("<div class='steps'><strong>🧾 Explicación paso a paso:</strong><br>" + "<br>".join(pasos) + "</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Ocurrió un error: {e}")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center; font-size:13px; color:gray;'>Universidad Privada Domingo Savio - Proyecto académico 2025</div>", unsafe_allow_html=True)