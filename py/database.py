import sqlite3

class Database:
    def __init__(self, db_name="clientes.db"):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def create_tables(self):
        """Crea las tablas necesarias."""
        cursor = self.connect().cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                razon_social TEXT NOT NULL,
                ruc TEXT UNIQUE NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS datos_t_persona (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                persona_contacto TEXT NOT NULL,
                FOREIGN KEY(cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS datos_t_area (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                area_trabajo TEXT NOT NULL,
                FOREIGN KEY(cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS datos_t_direx (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                direccion TEXT NOT NULL,
                FOREIGN KEY(cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()

    def insert_cliente(self, razon_social, ruc):
        cursor = self.connect().cursor()
        cursor.execute("INSERT INTO clientes (razon_social, ruc) VALUES (?, ?)", (razon_social, ruc))
        self.conn.commit()
        return cursor.lastrowid

    def insert_dato(self, table, cliente_id, value):
        """Inserta un dato en la tabla especificada."""
        cursor = self.connect().cursor()
        cursor.execute(f"INSERT INTO {table} (cliente_id, {table.split('_')[2]}) VALUES (?, ?)", (cliente_id, value))
        self.conn.commit()

    def fetch_datos(self, table, cliente_id):
        """Obtiene datos de una tabla específica."""
        cursor = self.connect().cursor()
        cursor.execute(f"SELECT id, {table.split('_')[2]} FROM {table} WHERE cliente_id = ?", (cliente_id,))
        return cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
