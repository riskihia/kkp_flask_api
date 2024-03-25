# KKP project API

### Requirements:

- Python 3 : [Python](https://www.python.org/)
- Env : See env example
- Database : Make the database to store data

## Installation

Create an environment:

```
py -m venv .venv
```

Activate the environment:

```
.venv\Scripts\activate
```

Install with pip:

```
pip install -r requirements.txt
```

## Database configuration

1. Create new file '.env'
2. Copy isi file '.env.example' ke dalam file '.env'
3. Sesuaikan configurasi database sesuai dengan host, database_name, user_db_name, dan password

## Run Flask

### Run flask for develop

```
$ flask run
```

In flask, Default port is `5000`

Swagger document page: `http://127.0.0.1:5000/swagger-ui`
