import streamlit as st
import sympy as sp

x = sp.symbols('x')

st.title("Calculadora La Solución")
st.subheader("Resolución paso a paso - Cálculo I (versión web)")

expresion = st.text_input("Ingresa una expresión en x (ej: x**2 + 3*x):")
operacion = st.selectbox("Selecciona la operación", ["Evaluar", "Derivada", "Integral", "Límite"])

if st.button("Resolver"):
    try:
        funcion = sp.sympify(expresion)
        if operacion == "Evaluar":
            valor = st.number_input("Valor de x para evaluar:", value=1.0)
            resultado = funcion.evalf(subs={x: valor})
            pasos = f"Sustituimos x = {valor} en la expresión y obtenemos el resultado: {resultado}"
        elif operacion == "Derivada":
            derivada = sp.diff(funcion, x)
            resultado = derivada
            pasos = f"Aplicamos reglas de derivación:\nLa derivada de {funcion} es: {derivada}"
        elif operacion == "Integral":
            integral = sp.integrate(funcion, x)
            resultado = integral
            pasos = f"Calculamos la integral indefinida:\n∫({funcion}) dx = {integral} + C"
        elif operacion == "Límite":
            punto = st.number_input("Límite cuando x tiende a:", value=0.0)
            limite = sp.limit(funcion, x, punto)
            resultado = limite
            pasos = f"Evaluamos el límite de {funcion} cuando x → {punto}:\nResultado: {limite}"
        
        st.success(f"Resultado: {resultado}")
        st.markdown("**Pasos:**")
        st.text(pasos)
    except Exception as e:
        st.error(f"Error al procesar la expresión: {e}")

st.markdown("Puedes imprimir esta página con Ctrl+P o desde el navegador.")