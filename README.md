# Tarea3-AE-API

## 🤝 Uso

## Validación

Primero, hay que realizar una validación del usuario mediante la siguiente query:

```curl
http://182.160.28.242:5001/admin
```
###
- ☄METODO: POST
- 🔑KEY: admin
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "username":"admin",
    "password":"password"
}
```

Una vez que se efectua la validación del usuario administrador, es capaz de realizar las siguientes peticiones.

### Query 1
Agregar una nueva compañia.
```curl
http://182.160.28.242:5001/api/addcompany
```
#### 
- ☄METODO: POST
- 🔑KEY: addcompany
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "company_name": "company_name",
    "company_api_key": "key_new",
    "username": "admin",
    "password": "password"
}
```

### Query 2
Agregar una nueva locación.
```curl
http://182.160.28.242:5001/api/addlocation
```
#### 
- ☄METODO: POST
- 🔑KEY: addlocation
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "company_id": "2",
    "location_name":"Lugarnuevo2",
    "location_country": "Paisnuevo2",
    "location_city":"Ciudadnueva2",
    "location_meta": "Esta es la locacion nueva 2",
    "user": "admin",
    "password":"password"
}
```
### Query 3
Agregar un nuevo sensor.
```curl
http://182.160.28.242:5001/api/addsensor
```
#### 
- ☄METODO: POST
- 🔑KEY: addsensor
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "location_id": "1",
    "sensor_name": "SensorNuevo",
    "sensor_category": "CategoriaNueva",
    "sensor_meta": "Este es el sensor Nuevo",
    "sensor_api_key": "sensor_nuevo_4",
    "user": "admin",
    "password": "password"
}
```

### Query 4
Obtener la locación de las compañias
```curl
http://182.160.28.242:5001/api/getlocations/<company_api_key>
```
#### 
- ☄METODO: GET
- 🔑KEY: getlocations
- 📃VALUE: \<company_api_key\>

#### Ejemplo de JSON respuesta.
```js
{
    "locations": [
        {
            "company_id": 1,
            "id": 1,
            "location_city": "Ciudadnueva",
            "location_country": "Paisnuevo",
            "location_meta": "Esta es la locacion nueva",
            "location_name": "Lugarnuevo"
        }
    ],
    "status": "success"
}
```

### Query 5
Actualizar la locación
```curl
http://182.160.28.242:5001/api/updatelocation
```
#### 
- ☄METODO: PUT
- 🔑KEY: updatelocation
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "location_id":"1",
    "company_api_key":"key_new",
    "location_name":"Lugarnuevo",
    "location_country":"Paisnuevo",
    "location_city":"Ciudadnueva",
    "location_meta":"Esta es la locacion nueva"
}
```

### Query 6
Eliminar la locación
```curl
http://182.160.28.242:5001/api/deletelocation
```
#### 
- ☄METODO: DELETE
- 🔑KEY: deletelocation
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "location_id":"2",
    "company_api_key":"key_new2"
}
```

### Query 7
Obtener los Sensores
```curl
http://182.160.28.242:5001/api/getsensors/<company_api_key>/<location_id>
```
#### 
- ☄METODO: GET
- 🔑KEY: getsensors
- 📃VALUE: \<company_api_key>/<location_id\>

#### Ejemplo de JSON respuesta.
```js
{
    "sensors": [
        {
            "location_id": 1,
            "sensor_api_key": "sensorone",
            "sensor_category": "Categoria1",
            "sensor_id": 1,
            "sensor_meta": "Este es el sensor1",
            "sensor_name": "Sensor1"
        }
    ],
    "status": "success"
}
```

### Query 8
Actualizar los Sensores
```curl
http://182.160.28.242:5001/api/updatesensor
```
#### 
- ☄METODO: PUT
- 🔑KEY: updatesensor
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "sensor_id":"1",
    "company_api_key":"key_new",
    "sensor_name":"Sensor1",
    "sensor_category":"Categoria1",
    "sensor_meta":"Este es el sensor1",
    "sensor_api_key":"sensorone"
}
```


### Query 9
Eliminar el Sensor
```curl
http://182.160.28.242:5001/api/deletesensor
```
#### 
- ☄METODO: DELETE
- 🔑KEY: deletesensor
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "sensor_id":"2",
    "company_api_key":"key_new2"
}
```

### Query 10
Agregar datos al sensor
```curl
http://182.160.28.242:5001/api/sensordata
```
#### 
- ☄METODO: POST
- 🔑KEY: sensordata
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "sensor_id":"1",
    "sensor_api_key":"sensorone",
    "sensor_data":"datos_nuevos2s"
}
```

### Query 11
Obtener los datos del sensor
```curl
http://182.160.28.242:5001/api/getsensordata/<company_api_key>/from/<time1>/to/<time2>/<sensor_id>
```
#### 
- ☄METODO: GET
- 🔑KEY: getsensordata
- 📃VALUE: \<company_api_key, from, time1, to, time2, sensor_id\>

#### Ejemplo de JSON respuesta.
```js
{
    "data": [
        {
            "data": "datos 1 editado v2",
            "sensor_data_id": 1,
            "sensor_id": 1
        }
    ],
    "status": "success"
}
```


### Query 12
Actualizar los datos del sensor
```curl
http://182.160.28.242:5001/api/updatesensordata
```
#### 
- ☄METODO: PUT
- 🔑KEY: updatesensordata
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "sensor_id":"1",
    "sensor_api_key":"sensorone",
    "sensor_data":"datos 1 editado v2",
    "sensor_data_id":"1"
}
```



### Query 13
Eliminar los datos del sensor
```curl
http://182.160.28.242:5001/api/deletesensordata/
```
#### 
- ☄METODO: DELETE
- 🔑KEY: deletesensordata
- 📃VALUE: \<JSON EJEMPLO\>

#### Ejemplo de JSON a enviar.
```js
{
    "sensor_api_key":"sensorone",
    "sensor_data_id":"2"
}
```
