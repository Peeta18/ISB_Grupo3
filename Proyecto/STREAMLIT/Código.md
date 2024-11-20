*PASOS* 
1. PANTALLA DE INICIO
   import streamlit as st

def login():
    st.title("RehabGest EMG")
    st.subheader("Inicio de Sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if username == "doctor" and password == "password":  # Placeholder de autenticación
            st.success("Inicio de sesión exitoso")
            return True
        else:
            st.error("Usuario o contraseña incorrectos")
    return False

3. D
