import sqlite3
import os

class ClienteDatabase:
    def __init__(self, db_name='clientes.db'):
        # Definir la ruta de la carpeta de base de datos
        self.base_datos_dir = os.path.join(os.getcwd(), 'base_dato')
        
        # Crear la carpeta de base de datos si no existe
        if not os.path.exists(self.base_datos_dir):
            os.makedirs(self.base_datos_dir)
        
        # Definir la ruta completa de la base de datos
        self.db_path = os.path.join(self.base_datos_dir, db_name)
        
        # Crear la conexión inicial y la tabla
        self.crear_tabla()

    def crear_conexion(self):
        """Crear y devolver una conexión a la base de datos"""
        try:
            conexion = sqlite3.connect(self.db_path)
            return conexion
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def crear_tabla(self):
        try:
            conexion = self.crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                
                # Tabla de clientes (existente)
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    razon_social TEXT NOT NULL,
                    ruc TEXT UNIQUE NOT NULL,
                    direccion TEXT,
                    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                ''')
                
                # Tabla de personas de contacto (existente)
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS personas_contacto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_ruc TEXT,
                    nombre TEXT,
                    FOREIGN KEY(cliente_ruc) REFERENCES clientes(ruc)
                )
                ''')
                
                # Tabla de áreas de trabajo (existente)
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS areas_trabajo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_ruc TEXT,
                    nombre TEXT,
                    FOREIGN KEY(cliente_ruc) REFERENCES clientes(ruc)
                )
                ''')
                
                # Nueva tabla de direcciones adicionales
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS direcciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_ruc TEXT,
                    direccion TEXT,
                    FOREIGN KEY(cliente_ruc) REFERENCES clientes(ruc)
                )
                ''')
                
                conexion.commit()
                conexion.close()
                print("Tablas de clientes, personas de contacto, áreas de trabajo y direcciones creadas exitosamente")
        except sqlite3.Error as e:
            print(f"Error al crear las tablas: {e}")
            
    def obtener_clientes(self, limite=50):
        try:
            conexion = self.crear_conexion()
            cursor = conexion.cursor()
            cursor.execute('''
                SELECT id, razon_social, ruc, fecha_registro 
                FROM (
                    SELECT id, razon_social, ruc, fecha_registro 
                    FROM clientes 
                    ORDER BY fecha_registro DESC
                    LIMIT ?
                ) 
                ORDER BY fecha_registro ASC
            ''', (limite,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener clientes: {e}")
            return []
        finally:
            if conexion:
                conexion.close()

    # Métodos adicionales para operaciones CRUD se agregarán después