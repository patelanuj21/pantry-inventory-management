from multiprocessing import connection
from backend import app
from backend import inventories_dao
from backend import sql_connection
from flask import request, jsonify   


connection = sql_connection.get_sql_connection()

# Health check API call
@app.route('/alive', methods=['GET'])
def alive():
    return 'alive'


@app.route('/getInventories', methods=['GET'])
def get_inventories():
    inventories = inventories_dao.get_all_inventories(connection)
    response = jsonify(inventories)
    response.headers.add('Access-Controll-Allow-Origin', '*')
    return response