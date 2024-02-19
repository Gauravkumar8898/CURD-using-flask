from flask import Flask, request, jsonify
from src.utils.constant import mydb, emp_table_name


app = Flask(__name__)


@app.route('/create_table', methods=['POST'])
def create_table():
    """
    Create a new table in the database.
    This endpoint allows creating a new table in the database with the specified table name and columns.
    Request Body:
        - table_name (str): The name of the table to create.
    Returns:
        - JSON response with a success message if the table is created successfully.
        - JSON response with an error message if an error occurs during table creation.
    """
    try:
        table_name = request.json.get('table_name')
        cursor = mydb.cursor()
        cursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY,"
                       " name VARCHAR(255), gender VARCHAR(255) , dept VARCHAR(255))")
        return jsonify({" table created!": table_name})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/insert', methods=['POST'])
def add_data():
    """
    Insert new data into the specified table.
    This endpoint allows inserting a new record into the database table with the specified employee details.
    Request Body:
        - employee_name (str): The name of the employee.
        - employee_gender (str): The gender of the employee.
        - employee_dept (str): The department of the employee.
    Returns:
        - JSON response with a success message if the record is inserted successfully.
        - JSON response with an error message if an error occurs during record insertion.
    """
    try:
        employee_name = request.json.get('employee_name')
        employee_gender = request.json.get('employee_gender')
        employee_dept = request.json.get('employee_dept')
        cursor = mydb.cursor()
        sql = f"INSERT INTO {emp_table_name} (name, gender, dept) VALUES (%s, %s, %s)"
        # val = ("John", "Highway 21")
        val = (employee_name, employee_gender, employee_dept)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")
        return jsonify({"record inserted": cursor.rowcount, })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/read', methods=['GET'])
def show_data():
    """
    Retrieve all data from the specified table.
    This endpoint allows retrieving all records from the database table.
    Returns:
        - JSON response with a list of records if retrieval is successful.
        - JSON response with an error message if an error occurs during retrieval.
    """
    try:
        cursor = mydb.cursor()
        cursor.execute(f"SELECT * FROM {emp_table_name}")
        result = cursor.fetchall()
        print(result)
        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/read/<int:id>', methods=['GET'])
def read_data_id(id):
    """
     Retrieve data from the specified table by ID.
     This endpoint allows retrieving a record from the database table based on the provided ID.
     Parameters:
         - id (int): The ID of the record to retrieve.
     Returns:
         - JSON response with the record if retrieval is successful.
         - JSON response with an error message if an error occurs during retrieval.
     """
    try:
        cursor = mydb.cursor()
        cursor.execute(f"SELECT * FROM {emp_table_name} WHERE id=%s", (id,))
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/delete/<int:id>')
def delete_data_id(id):
    """
    Delete data from the specified table by ID.
    This endpoint allows deleting a record from the database table based on the provided ID.
    Parameters:
        - id (int): The ID of the record to delete.
    Returns:
        - JSON response with a success message if deletion is successful.
        - JSON response with an error message if an error occurs during deletion.
    """
    try:
        cursor = mydb.cursor()
        cursor.execute(f"DELETE FROM {emp_table_name} WHERE id=%s", (id,))
        mydb.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/update', methods=['PUT'])
def data_update():
    """
    Update data in the specified table.
    This endpoint allows updating a record in the database table with the provided employee details.
    Request Body:
        - employee_id (int): The ID of the employee to update.
        - employee_name (str): The updated name of the employee.
        - employee_gender (str): The updated gender of the employee.
        - employee_dept (str): The updated department of the employee.
    Returns:
        - JSON response with a success message if update is successful.
        - JSON response with an error message if an error occurs during update.
    """
    try:
        employee_name = request.json.get('employee_name')
        employee_id = request.json.get('id')
        employee_gender = request.json.get('employee_gender')
        employee_dept = request.json.get('employee_dept')
        cursor = mydb.cursor()
        sql = "UPDATE Nash_employee SET name=%s, gender =%s, dept=%s WHERE id=%s"
        data = (employee_name, employee_gender, employee_dept, employee_id)
        cursor.execute(f"UPDATE {emp_table_name} SET name=%s, gender =%s, dept=%s WHERE id=%s",
                       (employee_name, employee_gender, employee_dept, employee_id))
        mydb.commit()
        resp = jsonify(f'User updated successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.errorhandler(404)
def not_found(error=None):
    """
    Handle 404 errors.
    This function is called when a 404 error occurs (resource not found).
    Parameters:
        - error: The error object (default is None).
    Returns:
        - JSON response with a 404 status code and a message indicating the resource was not found.
    """
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
