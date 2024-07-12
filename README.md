## ORDER TABLE WEB SERVER

This repository contains a Python Flask application designed for managing orders using a MySQL database. It initializes a Flask web server and configures connection parameters to interact with a MySQL database named 'order_table'. The database schema includes fields such as customer name, order status, progress, order date, and country. 

The application provides functionalities to initialize the database (`init_order_db()`), fetch all orders (`get_orders()`), and add new orders (`add_order()`). Two routes are defined: '/' for displaying existing orders and '/add_order' for adding new orders via a web form. The HTML templates ('index.html') use CSS styling for a visually appealing and responsive interface, showcasing order details in a table format and providing a form to submit new orders. This repository serves as an educational example for integrating Flask with MySQL for basic order management tasks.
