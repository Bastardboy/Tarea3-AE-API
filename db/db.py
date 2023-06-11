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

# Crear la tabla "Location"
cursor.execute('''CREATE TABLE IF NOT EXISTS Location (
                    ID INTEGER NOT NULL, 
                    company_id INTEGER NOT NULL, 
                    location_name VARCHAR(200) NOT NULL, 
                    location_country VARCHAR(200) NOT NULL, 
                    location_city VARCHAR(200) NOT NULL, 
                    location_meta VARCHAR(200) NOT NULL, 
                    PRIMARY KEY (ID), 
                    UNIQUE (ID), 
                    FOREIGN KEY(company_id) REFERENCES Company (ID)
                )''')

# Crear la tabla "Company"
cursor.execute('''CREATE TABLE IF NOT EXISTS Company (
                    ID INTEGER NOT NULL, 
                    company_name VARCHAR(200) NOT NULL, 
                    company_api_key VARCHAR(200) NOT NULL, 
                    PRIMARY KEY (ID), 
                    UNIQUE (ID)
                )''')

# Crear la tabla "Sensor"
cursor.execute('''CREATE TABLE IF NOT EXISTS Sensor (
                    sensor_id INTEGER NOT NULL, 
                    location_id INTEGER NOT NULL, 
                    sensor_name VARCHAR(200) NOT NULL, 
                    sensor_category VARCHAR(200) NOT NULL, 
                    sensor_meta VARCHAR(200), 
                    sensor_api_key VARCHAR(200), 
                    PRIMARY KEY (sensor_id), 
                    UNIQUE (sensor_id), 
                    FOREIGN KEY(location_id) REFERENCES Location (ID)
                )''')

# Crear la tabla "SensorData"
cursor.execute('''CREATE TABLE IF NOT EXISTS SensorData (
                    sensor_data_id INTEGER NOT NULL, 
                    sensor_id INTEGER NOT NULL, 
                    data VARCHAR(200), 
                    date INTEGER NOT NULL, 
                    PRIMARY KEY (sensor_data_id), 
                    UNIQUE (sensor_data_id), 
                    FOREIGN KEY(sensor_id) REFERENCES Sensor (sensor_id)
                )''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
