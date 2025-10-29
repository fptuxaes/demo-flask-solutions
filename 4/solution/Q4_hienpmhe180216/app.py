from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import pyodbc
import locale
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

# Set locale for number formatting with thousand separators
locale.setlocale(locale.LC_ALL, '')

load_dotenv()

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
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




@app.route('/login', methods=['POST'])
def login():
    """
    Đăng nhập bằng MemberID và MemberPassword, trả về JWT token nếu hợp lệ.
    """
    try:
        data = request.get_json()
        member_id = data.get('MemberID')
        password = data.get('MemberPassword')

        if not member_id or not password:
            return jsonify({'ok': False, 'error': 'Missing MemberID or MemberPassword'}), 400

        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT MemberID, FullName, EmailAddress, MemberRole 
                FROM AccountMember 
                WHERE MemberID = ? AND MemberPassword = ?
            """, (member_id, password))
            row = cursor.fetchone()

            if not row:
                return jsonify({'ok': False, 'error': 'Invalid credentials'}), 401

            # Tạo payload cho JWT
            claims = {
                "FullName": row[1],
                "EmailAddress": row[2],
                "Role": row[3]
            }

            # Tạo token không có thời hạn
            access_token = create_access_token(
                identity=row[0],  # phải là string hoặc int
                additional_claims=claims,
                expires_delta=False
            )

            return jsonify({

                'token': access_token

            }), 200

    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500

@app.route('/accountmembers', methods=['GET'])
@jwt_required()
def get_account_members():
    """Return all account members (admin only)."""
    try:
        claims = get_jwt()
        if claims.get("Role") != 1:
            return jsonify({'ok': False, 'error': 'Access denied. Admin only'}), 403

        # Kết nối SQL Server
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT MemberID, FullName, EmailAddress, MemberRole
                FROM AccountMember
            """)
            rows = cursor.fetchall()

            # Chuyển sang dạng JSON
            members = [
                {
                    "MemberID": row[0],
                    "FullName": row[1],
                    "EmailAddress": row[2],
                    "MemberRole": row[3],
                }
                for row in rows
            ]

            return jsonify(members)


    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)