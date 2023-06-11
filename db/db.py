import sqlite3

# Conectarse a la base de datos (se creará si no existe)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear la tabla "Admin"
cursor.execute('''CREATE TABLE IF NOT EXISTS Admin (
                    rowid INTEGER NOT NULL, 
                    Username VARCHAR(200), 
                    Password VARCHAR(200), 
                    PRIMARY KEY (rowid), 
                    UNIQUE (Username), 
                    UNIQUE (Password)
                )''')

# Insertar un administrador y contraseña en la tabla "Admin"
admin_username = "admin"
admin_password = "password"

cursor.execute("INSERT INTO Admin (Username, Password) VALUES (?, ?)", (admin_username, admin_password))

# Crear las demás tablas...

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
