# Python ETL Example

Este proyecto es un ejemplo simple de un proceso ETL (Extract, Transform, Load) utilizando Python, Pandas, Requests y SQLAlchemy para la manipulación de datos.

## Estructura del Proyecto

- **Extract**: Obtiene datos desde una API.
- **Transform**: Filtra y transforma los datos en un DataFrame.
- **Load**: Carga los datos transformados en una base de datos SQLite.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install pandas requests sqlalchemy python-dotenv
```

## Configuración

El proyecto utiliza variables de entorno para manejar información sensible. En particular, la URL de la API se almacena en un archivo `.env`.

Ejemplo de `.env`:

```
api_url=http://universities.hipolabs.com/search?country=colombia
```

> **Nota:** El archivo `.env` fue subido para mostrar la URL utilizada en este ejemplo, pero **no se recomienda subir este archivo a repositorios públicos**.

## Uso

Ejecuta el script principal para extraer, transformar y cargar los datos:

```bash
python script.py
```

## Verificación de Datos

Para verificar que los datos fueron cargados correctamente en la base de datos SQLite, puedes ejecutar:

```python
from sqlalchemy import create_engine
import pandas as pd

disk_engine = create_engine("sqlite:///data.db")
df = pd.read_sql_query("SELECT * FROM cal_uni", disk_engine)
print(df.head())
```

## Autor

Luis Ángel Casas Ballestas

