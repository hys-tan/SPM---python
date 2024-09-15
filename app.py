import streamlit as st
import sqlite3
import pandas as pd
import os

# Ruta para almacenar los documentos adjuntos
UPLOAD_FOLDER = "uploads"

# Función para crear la base de datos y la tabla si no existen
def create_database():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        nombre_empresa TEXT,
        ruc TEXT,
        descripcion TEXT,
        dni TEXT,
        fecha TEXT,
        celular TEXT,
        cancelado TEXT,
        fecha_registro TEXT
    )
    ''')
    conn.commit()
    conn.close()

# Función para agregar un cliente a la base de datos
def add_cliente(nombre_empresa, ruc, descripcion, dni, fecha, celular, cancelado, fecha_registro):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO clientes (nombre_empresa, ruc, descripcion, dni, fecha, celular, cancelado, fecha_registro)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre_empresa, ruc, descripcion, dni, fecha, celular, cancelado, fecha_registro))
    conn.commit()
    conn.close()

# Función para obtener los datos de clientes de la base de datos
def get_clientes():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nombre_empresa, ruc, descripcion, cancelado, fecha_registro FROM clientes')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Crear la base de datos y la tabla
create_database()

# Configuración de la página
st.set_page_config(page_title="Dashboard de Clientes", layout="wide")

# Navegación en la barra lateral
page = st.sidebar.selectbox("Selecciona la página", ["Página Principal", "Registrar Cliente"])

if page == "Registrar Cliente":
    # Página de registro de cliente
    st.header("Registrar Nuevo Cliente")
    nombre_empresa = st.text_input("Nombre/Empresa")
    ruc = st.text_input("RUC")
    descripcion = st.text_area("Descripción")
    dni = st.text_input("DNI")
    fecha = st.date_input("Fecha")
    celular = st.text_input("Celular")
    cancelado = st.selectbox("Cancelado", ["No", "Sí"])
    fecha_registro = st.date_input("Fecha de registro")

    # Subir documentos adjuntos
    uploaded_files = st.file_uploader("Adjuntar documentos (PDF, Word, Excel)", type=["pdf", "docx", "xlsx"], accept_multiple_files=True)

    if st.button("Guardar Cliente"):
        # Guardar los documentos adjuntos
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        for uploaded_file in uploaded_files:
            with open(os.path.join(UPLOAD_FOLDER, uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())

        # Guardar los datos del cliente
        add_cliente(nombre_empresa, ruc, descripcion, dni, str(fecha), celular, cancelado, str(fecha_registro))
        st.success("Cliente registrado exitosamente!")

        # Mostrar un mensaje de éxito y redirigir a la página principal
        st.sidebar.button("Regresar a la Página Principal", on_click=lambda: st.experimental_set_query_params(page="Página Principal"))

elif page == "Página Principal":
    # Página principal
    # Mostrar el título de la página principal
    st.markdown('<div class="main-title" style="background-color: #333333;">Registro de Datos</div>', unsafe_allow_html=True)

    # Buscar cliente
    col1, col2 = st.columns([6, 1])
    with col1:
        st.write("")  # Espacio para alinear la búsqueda
    with col2:
        search_query = st.text_input("Buscar", "")

    # Cargar los datos de clientes de la base de datos
    clientes = get_clientes()

    # Convertir los datos a un DataFrame de pandas
    df = pd.DataFrame(clientes, columns=["Nombre/Empresa", "RUC", "Descripción", "Cancelado", "Fecha de registro"])

    # Filtrar los datos en función de la búsqueda
    if search_query:
        df_filtered = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
        if df_filtered.empty:
            st.warning("No se encontraron resultados para la búsqueda.")
        else:
            st.markdown("### Resultados de la Búsqueda")
            st.table(df_filtered)
    else:
        # Mostrar la tabla de registros completa si no hay búsqueda
        st.markdown("### Registro de Clientes")
        st.table(df)
