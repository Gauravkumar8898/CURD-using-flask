# Flask API for Employee Nashtech

## Description
This Flask API provides CRUD operations for managing employee data in a MySQL database. It includes endpoints for creating, reading, updating, and deleting employee records.

## Installation
1. Clone the repository: git clone

## Description
This Flask API provides CRUD operations for managing employee data in a MySQL database. It includes endpoints for creating, reading, updating, and deleting employee records.

## Installation
1. Clone the repository: `git clone https://github.com/yourusername/flask-api.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up database connection: Modify `src/utils/constant.py` to specify your MySQL database connection details.
4. Run the Flask server: `python main.py`

## Usage
To use the API, send HTTP requests to the appropriate endpoints using tools like cURL or Postman.

### Endpoints
- `POST /create_table`: Create a new table in the database.
- `POST /insert`: Insert new data into the table.
- `GET /read`: Retrieve all data from the table.
- `GET /read/<id>`: Retrieve data by ID.
- `DELETE /delete/<id>`: Delete data by ID.
- `PUT /update`: Update data by ID.`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up database connection: Modify `src/utils/constant.py` to specify your MySQL database connection details.
4. Run the Flask server: `python app.py`

## Usage
To use the API, send HTTP requests to the appropriate endpoints using tools like cURL or Postman.

### Endpoints
- `POST /create_table`: Create a new table in the database.
- `POST /insert`: Insert new data into the table.
- `GET /read`: Retrieve all data from the table.
- `GET /read/<id>`: Retrieve data by ID.
- `DELETE /delete/<id>`: Delete data by ID.
- `PUT /update`: Update data by ID.

