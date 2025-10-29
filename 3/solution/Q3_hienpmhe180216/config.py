import os
from pathlib import Path
import pyodbc

basedir = Path(__file__).resolve().parent

class Config:
    """Base configuration for cross-platform SQL Server connectivity."""
    # SQL Server connection configuration
    # You can override these using environment variables
    SQL_SERVER = os.environ.get('SQL_SERVER', 'localhost')
    SQL_PORT = os.environ.get('SQL_PORT', '1433')
    SQL_DATABASE = os.environ.get('SQL_DATABASE', 'testdb')
    SQL_USERNAME = os.environ.get('SQL_USERNAME', 'sa')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD', '1')

    # Cross-platform ODBC driver selection
    # Default to ODBC Driver 18, fallback to 17 if not available
    SQL_DRIVER = os.environ.get('SQL_DRIVER', 'ODBC Driver 17 for SQL Server')

    # Build ODBC connection string for pyodbc (works on Windows, macOS, Linux)
    DATABASE_URI = (
        f"DRIVER={{{SQL_DRIVER}}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USERNAME};"
        f"PWD={SQL_PASSWORD};"
        "TrustServerCertificate=yes;"
        "Encrypt=yes;"
        "Connection Timeout=30;"
    )

    """Base configuration for JWT authentication."""
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
