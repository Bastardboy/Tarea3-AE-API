# Tarea3-AE-API

## 🤝 Uso

La aplicación tiene una API, que a través de los distintos métodos se pueden hacer las siguientes consultas:

### Query
Busca el inventario según la coincidencia de la palabra otorgada, busca en Cache y luego en la Base de Datos.
```curl
curl −−location −−request POST http://182.160.28.242:8000/api/addcompany
```
#### 
- ☄METODO: POST

#### Response example
```js
{
    "site":
        {
            "company_name": "company_name",
            "company_api_key": "key_new",
            "username": "admin",
            "password": "password"
        }
    ]
}
```
