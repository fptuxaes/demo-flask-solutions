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



@app.route('/api/products', methods=['POST'])
def create_product():
    """API để thêm sản phẩm mới vào bảng Products"""
    try:
        data = request.get_json()

        product_name = data.get('ProductName')
        category_id = data.get('CategoryID')
        units_in_stock = data.get('UnitsInStock')
        unit_price = data.get('UnitPrice')

        if not all([product_name, category_id, units_in_stock, unit_price]):
            return jsonify({'ok': False, 'error': 'Thiếu dữ liệu đầu vào'}), 400

        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO Products (ProductName, CategoryID, UnitsInStock, UnitPrice)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (product_name, category_id, units_in_stock, unit_price))
            conn.commit()

        return jsonify({'message': 'ok'}), 201

    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)