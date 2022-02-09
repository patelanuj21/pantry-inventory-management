def get_all_inventories(connection):
    cursor = connection.cursor()
    query = ("select * from inventories")
    cursor.execute(query)
    response = []
    for (id, name, description, address, creation_date, last_update) in cursor:
        response.append({
            'id': id,
            'name': name,
            'description': description,
            'address': address,
            'creation_date': creation_date,
            'last_update' : last_update
        })
    return response