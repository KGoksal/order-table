from flask import Flask, request, render_template
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

# Configure MySQL database
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST', 'localhost')
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password#'
app.config['MYSQL_DATABASE_DB'] = 'order_table'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

# Initialize database
def init_order_db():
    order_table = """
    CREATE TABLE IF NOT EXISTS orders (
        id INT NOT NULL AUTO_INCREMENT,
        customer_name VARCHAR(100) NOT NULL,
        status VARCHAR(50) NOT NULL,
        progress INT NOT NULL,
        order_date DATE NOT NULL,
        country VARCHAR(50) NOT NULL,
        PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """
    cursor.execute(order_table)

# Function to fetch all orders
def get_orders():
    query = """
    SELECT * FROM orders;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    orders = [{
        'id': row[0],
        'customer_name': row[1],
        'status': row[2],
        'progress': row[3],
        'order_date': row[4].strftime('%Y-%m-%d'),
        'country': row[5]
    } for row in result]
    return orders

# Function to add a new order
def add_order(customer_name, status, progress, order_date, country):
    insert = f"""
    INSERT INTO orders (customer_name, status, progress, order_date, country)
    VALUES ('{customer_name}', '{status}', {progress}, '{order_date}', '{country}');
    """
    cursor.execute(insert)
    return f'Order for {customer_name} added successfully'

# Route for home page
@app.route('/', methods=['GET'])
def show_orders():
    orders = get_orders()
    return render_template('index.html', orders=orders, developer_name='Oliver')

# Route for adding an order
@app.route('/add_order', methods=['POST'])
def add_order_route():
    customer_name = request.form['customer_name']
    status = request.form['status']
    progress = int(request.form['progress'])
    order_date = request.form['order_date']
    country = request.form['country']
    result = add_order(customer_name, status, progress, order_date, country)
    orders = get_orders()  # Refresh orders list after addition
    return render_template('index.html', orders=orders, result=result, developer_name='Oliver')

# Initialize the database and run the application
if __name__ == '__main__':
    init_order_db()
    app.run(host='0.0.0.0', port=80)
