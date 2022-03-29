import sqlite3
from sqlite3 import Error


def create_table(conn, sql_to_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_to_create_table)
        c.close()
        return conn
    except Error as e:
        print(e)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_product(conn, product):
    sql = '''INSERT INTO products(product_title, price, quantity)
    VALUES(?, ?, ?)'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
        c.close()
        return c.lastrowid
    except Error as e:
        print(e)
    return None


def update_product_quantity(conn, products):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, products)
        conn.commit()
    except Error as e:
        print(e)


def update_product_price(conn, product):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def delete_product(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


def select_product_by_value(conn, limit_p, limit_q):
    sql = '''SELECT * FROM products WHERE price <= ? and quantity <= ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (limit_p, limit_q))
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)



def search_product(conn,product_title):
    sql = '''SELECT * FROM products WHERE product_title like ?'''
    try:
        c = conn.cursor()
        c.execute(sql, [product_title])
        rows = c.fetchall()
        for r in rows:
            print(r)
    except Error as e:
        print(e)


database = r'hw.db'
conn = create_connection(database)
sql_create_table_students = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0.0
)
'''

if conn is not None:
    print("Successfully Connected!")
    # create_table(conn, sql_create_table_students)

    # create_product(conn, ("Banana", 152, 5))
    # create_product(conn, ("Tomato", 185, 20))
    # create_product(conn, ("Potato", 41, 3))
    # create_product(conn, ("Cucumber", 148, 7))
    # create_product(conn, ("Mandarin", 170, 77))
    # create_product(conn, ("Apple", 80, 14))
    # create_product(conn, ("Carrot", 60, 18))
    # create_product(conn, ("Onion", 40, 10))
    # create_product(conn, ("Milk", 65, 11))
    # create_product(conn, ("Sausage", 235, 9))
    # create_product(conn, ("Biscuit", 320, 100))
    # create_product(conn, ("Coca-Cola, Fanta, Spite", 60, 1))
    # create_product(conn, ("Oil", 170, 3))
    # create_product(conn, ("Ulkon", 65, 12))
    # create_product(conn, ("Beet", 50, 1))

select_all_products(conn)
# delete_product(conn, 3)
# update_product_quantity(conn, (44, 4))
# update_product_price(conn, (280, 11))
# select_product_by_value(conn, 100, 5)
# search_product(conn, 'Apple')
conn.close()