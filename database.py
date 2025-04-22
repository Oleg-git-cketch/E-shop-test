import sqlite3


connection = sqlite3.connect('delivery.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users '
            '(tg_id INTEGER, name TEXT, number TEXT);')
sql.execute('CREATE TABLE IF NOT EXISTS products '
            '(pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, pr_des TEXT, pr_price REAL, '
            'pr_count INTEGER, pr_photo TEXT);')
sql.execute('CREATE TABLE IF NOT EXISTS cart '
            '(user_id INTEGER, user_product TEXT, '
            'product_amount INTEGER);')


def register(tg_id, name, number):
    sql.execute('INSERT INTO users VALUES (?, ?, ?);',
                (tg_id, name, number))
    connection.commit()


def check_user(tg_id):
    if sql.execute('SELECT * FROM users WHERE tg_id=?;', (tg_id,)).fetchone():
        return True
    else:
        return False


def get_pr_buttons():
    all_products = sql.execute('SELECT * FROM products;').fetchall()
    result = [i for i in all_products if i[4] > 0]
    return result


def get_all_pr():
    return sql.execute('SELECT * FROM products;').fetchall()


def get_exact_pr(pr_id):
    return sql.execute('SELECT * FROM products WHERE pr_id=?;', (pr_id,)).fetchone()


def get_exact_price(pr_name):
    return sql.execute('SELECT pr_price FROM products WHERE pr_name=?;', (pr_name,)).fetchone()


def pr_to_db(pr_name, pr_des, pr_price, pr_count, pr_photo):
    if (pr_name,) in sql.execute('SELECT pr_name FROM products;').fetchall():
        return False
    else:
        sql.execute('INSERT INTO products (pr_name, pr_des, pr_price, pr_count, pr_photo) '
                    'VALUES (?, ?, ?, ?, ?);', (pr_name, pr_des, pr_price, pr_count, pr_photo))
        connection.commit()


def change_pr_attr(keyword, new_value, attr=''):
    if attr == 'name':
        sql.execute('UPDATE products SET pr_name=? WHERE pr_name=?;',
                    (new_value, keyword))
    elif attr == 'description':
        sql.execute('UPDATE products SET pr_des=? WHERE pr_name=?;',
                    (new_value, keyword))
    elif attr == 'price':
        sql.execute('UPDATE products SET pr_price=? WHERE pr_name=?;',
                    (new_value, keyword))
    elif attr == 'count':
        sql.execute('UPDATE products SET pr_count=? WHERE pr_name=?;',
                    (new_value, keyword))
    elif attr == 'photo':
        sql.execute('UPDATE products SET pr_photo=? WHERE pr_name=?;',
                    (new_value, keyword))

    connection.commit()


def del_product(pr_name):
    sql.execute('DELETE FROM products WHERE pr_name=?;', (pr_name,))
    connection.commit()


def check_pr():
    if sql.execute('SELECT * FROM products;').fetchall():
        return True
    else:
        return False


def show_cart(tg_id):
    return sql.execute('SELECT * FROM cart WHERE user_id=?;', (tg_id,)).fetchall()


def add_to_cart(tg_id, product, product_amount):
    sql.execute('INSERT INTO cart VALUES (?, ?, ?);', (tg_id, product, product_amount))
    connection.commit()


def clear_cart(tg_id):
    sql.execute('DELETE FROM cart WHERE user_id=?;', (tg_id,))
    connection.commit()


def make_order(tg_id):
    product_names = sql.execute('SELECT user_product FROM cart WHERE user_id=?;', (tg_id,)).fetchall()
    product_quantities = sql.execute('SELECT product_amount FROM cart WHERE user_id=?;', (tg_id,)).fetchall()

    product_counts = [sql.execute('SELECT pr_count FROM products WHERE pr_name=?;', (i[0],)).fetchone()[0] for i in product_names]
    totals = []

    for e in product_quantities:
        for c in product_counts:
            totals.append(c - e[0])

    for t in totals:
        for n in product_names:
            sql.execute('UPDATE products SET pr_count=? WHERE pr_name=?;', (t, n[0]))


    connection.commit()
    return product_counts, totals
