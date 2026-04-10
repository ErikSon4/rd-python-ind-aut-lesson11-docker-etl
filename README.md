# rd-python-ind-aut-lesson11-docker-etl

### Description
This project implements a simple ETL pipeline using Docker:
- loads data from a CSV file
- stores it in MariaDB
- exposes it via an HTTP API

### Architecture
The project consists of 3 containers:
- db (MariaDB) – database
- loader (Python) – loads CSV and inserts data into DB
- api (Flask) – provides REST endpoint

Containers communicate through a custom Docker network `etl_network`.

### Run

```bash
docker compose up --build
```

For clean restart:

```bash
docker compose down -v
docker compose up --build
```

### ETL Process
1. Loader reads CSV file
2. Connects to database (with retry logic)
3. Inserts data into `data` table

### API

Endpoint:
http://localhost:5000/data

Returns JSON:

```json
[
  {"id": 1, "name": "A", "value": 10},
  {"id": 2, "name": "B", "value": 20},
  {"id": 3, "name": "C", "value": 30}
]
```
