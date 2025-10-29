"""
SQL Server Connection Test Utility for Windows

This script helps you:
1. List available ODBC drivers
2. Test SQL Server connectivity
3. Verify your connection string

Run this script to troubleshoot SQL Server connection issues.
"""

import pyodbc
import os
from dotenv import load_dotenv

def list_odbc_drivers():
    """List all available ODBC drivers on the system."""
    print("Available ODBC Drivers:")
    print("-" * 40)
    drivers = pyodbc.drivers()
    for i, driver in enumerate(drivers, 1):
        print(f"{i}. {driver}")
    print()

def test_sql_server_connection():
    """Test SQL Server connection using current configuration."""
    load_dotenv()
    
    # Get configuration from environment variables or use defaults
    server = os.environ.get('SQL_SERVER', 'localhost')
    port = os.environ.get('SQL_PORT', '1433')
    database = os.environ.get('SQL_DATABASE', 'testdb')
    username = os.environ.get('SQL_USERNAME', 'sa')
    password = os.environ.get('SQL_PASSWORD', '1')
    driver = os.environ.get('SQL_DRIVER', 'ODBC Driver 18 for SQL Server')
    
    print("Current Configuration:")
    print(f"Server: {server}:{port}")
    print(f"Database: {database}")
    print(f"Username: {username}")
    print(f"Driver: {driver}")
    print()
    
    # Build connection string
    connection_string = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server},{port};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "TrustServerCertificate=yes;"
        "Encrypt=yes;"
        "Connection Timeout=30;"
    )
    
    print("Testing connection...")
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT @@VERSION")
            version = cursor.fetchone()[0]
            print("Connection successful!")
            print(f"SQL Server Version: {version[:100]}...")
            
            # Test a simple query
            cursor.execute("SELECT GETDATE()")
            current_time = cursor.fetchone()[0]
            print(f"Current server time: {current_time}")
            
    except Exception as e:
        print("Connection failed!")
        print(f"Error: {str(e)}")
        print()
        print("Common solutions:")
        print("1. Check if SQL Server is running")
        print("2. Verify server name and port")
        print("3. Check username and password")
        print("4. Ensure SQL Server Authentication is enabled")
        print("5. Check Windows Firewall settings")
        print("6. Try using Windows Authentication (see config.py)")

def test_windows_authentication():
    """Test SQL Server connection using Windows Authentication."""
    load_dotenv()
    
    server = os.environ.get('SQL_SERVER', 'localhost')
    port = os.environ.get('SQL_PORT', '1433')
    database = os.environ.get('SQL_DATABASE', 'testdb')
    driver = os.environ.get('SQL_DRIVER', 'ODBC Driver 18 for SQL Server')
    
    print("Testing Windows Authentication...")
    print(f"Server: {server}:{port}")
    print(f"Database: {database}")
    print(f"Driver: {driver}")
    print()
    
    connection_string = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server},{port};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
        "Encrypt=yes;"
        "Connection Timeout=30;"
    )
    
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT SYSTEM_USER, USER_NAME()")
            user_info = cursor.fetchone()
            print("Windows Authentication successful!")
            print(f"Connected as: {user_info[0]} / {user_info[1]}")
            
    except Exception as e:
        print("Windows Authentication failed!")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("SQL Server Connection Test Utility")
    print("=" * 50)
    print()
    
    # List available drivers
    list_odbc_drivers()
    
    # Test SQL Server Authentication
    test_sql_server_connection()
    print()
    
    # Test Windows Authentication
    print("-" * 50)
    test_windows_authentication()