from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import pyodbc
import locale

# Set locale for number formatting with thousand separators
locale.setlocale(locale.LC_ALL, '')

load_dotenv()

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# Custom filter for formatting numbers with thousand separators
@app.template_filter('format_number')
def format_number(value):
    try:
        return f"{int(value):,}"
    except (ValueError, TypeError):
        return value

# Fetch connection string from config
connection_string = app.config['DATABASE_URI']


@app.route('/')
def home():
    """Fetch products from the database and render the index page."""
    try:
        sort_param = request.args.get('sort')
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            query = """
                SELECT p.ProductId,p.ProductName, c.CategoryName, p.UnitsInStock, p.UnitPrice 
                FROM Products p
                LEFT JOIN Categories c ON p.CategoryID = c.CategoryID
            """
            if sort_param == 'price':
                query += " ORDER BY p.UnitPrice ASC"
            cursor.execute(query)
            products = cursor.fetchall()
            # Convert to list of dictionaries
            product_list = [{ 'id': row[0],'ProductName': row[1], 'CategoryName': row[2], 'UnitsInStock': row[3], 'UnitPrice': row[4]} for row in products]
            return render_template('index.html', products=product_list)
    except Exception as e:
        return render_template('index.html', products=[], error=str(e))


@app.route('/dbtest')
def dbtest():
    """Attempt a simple query to verify DB connectivity using pyodbc."""
    try:
        # Connect to the database using pyodbc
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            return jsonify({'ok': True, 'result': result[0]})
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


@app.route('/statistics')
def statistics():
    """Fetch product statistics and render the statistics page."""
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT COUNT(*), SUM(UnitsInStock), SUM(UnitPrice * UnitsInStock)
                FROM Products
            """)
            stats = cursor.fetchone()
            total_products = stats[0] if stats[0] is not None else 0
            total_units = stats[1] if stats[1] is not None else 0
            total_value = stats[2] if stats[2] is not None else 0
            return render_template('statistics.html', total_products=total_products, total_units=total_units, total_value=total_value)
    except Exception as e:
        return render_template('statistics.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)