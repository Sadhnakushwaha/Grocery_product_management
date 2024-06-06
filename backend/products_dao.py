from sql_connection import get_Sql_connection
# import mysql.connector

def get_all_products(connection):
    # cnx = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='grocery_store')

    # cursor = cnx.cursor()
    cursor = connection.cursor()
    query = ("select products.product_id, products.name , products.uom_id,products.price_per_unit,uom.uom_name FROM products inner join uom on products.uom_id = uom.uom_id")
    cursor.execute(query)

    response = []

    for(product_id ,name ,uom_id, price_per_unit, uom_name) in cursor:
        # print(product_id ,name,uom_id, price_per_unit, uom_name)
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id':uom_id,
                'price_per_unit':price_per_unit,
                'uom_name':uom_name
            }
        )

    # cnx.close()

    return response

def insert_new_product(connection , product):
    cursor = connection.cursor()
    query = ("INSERT INTO products"
             "(name ,uom_id ,price_per_unit)"
             "VALUES (%s ,%s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_Sql_connection()
    # print(insert_new_product(connection, {
    #     'product_name': 'cabbage',
    #     'uom_id': '1',
    #     'price_per_unit': '10'
    # }))
    print(delete_product(connection, 15))

    
    
  








