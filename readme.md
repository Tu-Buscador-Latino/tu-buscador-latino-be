# Tu Buscador Latino (Backend)

## 1. Descripción

Este repositorio contiene el backend del aplicativo web **Tu Buscador Latino**. El backend fue desarrollado en python 3.9 y DjangoRestFramework.
Permite almacenar y consultar las estadisticas sobre las palabras buscadas en el [**Frontend**](https://github.com/Tu-Buscador-Latino/tu-buscador-latino-fe) en una base de datos SQLite.

## 2. Tecnologías

* Python 3.9
* Django/Restframework
* SQLite

## 3. Dependencias

- **Django/Restframework:** https://www.django-rest-framework.org/

## 4. Instalación
***
Este programa está diseñado en Python version 3.9

Para windows ejecutar:
```
$ git clone https://github.com/Tu-Buscador-Latino/tu-buscador-latino-be.git
$ cd ../tu-buscador-latino-be
$ python3 -m venv env
$ env\Scripts\activate.bat
$ pip3 install -r requirements.txt
$ python manage.py runserver
```
Para linux ejecutar:
```
$ git clone https://github.com/Tu-Buscador-Latino/tu-buscador-latino-be.git
$ cd ../tu-buscador-latino-be
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python manage.py runserver
```

## 5. Persistencia de datos

Los datos estan alojados en un Base de Datos SQLite. La estructura de datos se presenta en la siguente tabla.

|Nombre        | Tipo      | Descripcion         |
|--------------|-----------|---------------------|
| id           | integer   | PK, autoincremental |
| word         | string    | palabra o palabras buscadas    |
| count        | integer   | total de búsquedas   |
| start_date   | date      | fecha primera vez de búsqueda|
| last_date    | date      | fecha ultima vez de búsqueda |
| last_results | String    | total de resultados recientes obtenidos|

## 6. URLs API 

| URL                       | Metodo |  Descripcion         |
|---------------------------|--------| ---------------------
|`/search/post/`            | POST   | Guardar o actualizar búsqueda|
|`/search/stats/?max=<Valor>`     | GET    | Obtener estadísticas. **Valor**=número máximo de palabras a buscar |


