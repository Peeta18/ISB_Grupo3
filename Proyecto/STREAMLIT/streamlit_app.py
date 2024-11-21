import streamlit as st

# Título de la aplicación
st.title("RehabGest EMG")
st.write("Bienvenido a la plataforma de rehabilitación remota con EMG")

# Inicio de sesión
st.subheader("Inicio de Sesión")
username = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Iniciar sesión"):
    if username == "doctor" and password == "1234":
        st.success("Inicio de sesión exitoso")
        st.write("Seleccione una opción del menú para continuar.")
        # Agregar más funciones aquí
    else:
        st.error("Usuario o contraseña incorrectos")
