# Demo Database

A Flask web application for database demonstrations.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to `http://localhost:5000`

## Project Structure

```
DemoDatabase/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html
└── static/             # Static files (CSS, JS, images)
```

## Configuration

This project supports environment-based configuration. Use the provided `config.py` and a `.env` file to customize settings.

- Copy the example file and edit values:

```bash
cp .env.example .env
# then edit .env and set your SECRET_KEY and DATABASE_URL
```

- `config.py` provides `Config`, `DevelopmentConfig`, and `ProductionConfig` classes. Example usage in `app.py`:

```python
from config import DevelopmentConfig
app.config.from_object(DevelopmentConfig)
```

The `SECRET_KEY` and `DATABASE_URL` will be read from environment variables if set; otherwise defaults from `.env` will be used when you load them into the environment.

To load `.env` automatically you can install `python-dotenv` and add at the top of `app.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

### SQL Server Configuration for Windows

This application is configured to connect to SQL Server using pyodbc and ODBC drivers. Follow these steps to set up your SQL Server connection:

#### 1. Install SQL Server ODBC Driver

Download and install the Microsoft ODBC Driver for SQL Server:
- [ODBC Driver 18 for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server) (recommended)
- Or use ODBC Driver 17 for SQL Server

#### 2. Configure Connection Settings

Copy the example environment file and update with your SQL Server details:

```bash
cp .env.example .env
```

Edit `.env` with your SQL Server configuration:

```env
# SQL Server Configuration
SQL_SERVER=localhost                    # or your server name/IP
SQL_PORT=1433                          # default SQL Server port
SQL_DATABASE=testdb                    # your database name
SQL_USERNAME=sa                        # SQL Server username
SQL_PASSWORD=MyS3cure_                 # SQL Server password
SQL_DRIVER=ODBC Driver 18 for SQL Server
```

#### 3. Connection Options

**SQL Server Authentication (Username/Password):**
Use the configuration above with `SQL_USERNAME` and `SQL_PASSWORD`.

**Windows Authentication:**
To use Windows Authentication, comment out `SQL_USERNAME` and `SQL_PASSWORD` in your `.env` file, then modify `config.py` to use `DATABASE_URI_WINDOWS_AUTH` instead of `DATABASE_URI`.

**Common Server Names:**
- Local default instance: `localhost` or `127.0.0.1`
- Named instance: `COMPUTERNAME\SQLEXPRESS`
- Remote server: `server.domain.com` or IP address

#### 4. Cross-Platform Setup (Recommended)

Run the automated setup script (works on Windows, macOS, and Linux):

```bash
python setup_sqlserver.py
```

This script will:
- Check your Python environment and dependencies
- List available ODBC drivers for your operating system
- Create .env file from template
- Test your SQL Server connection
- Provide platform-specific installation instructions for ODBC drivers

#### 5. Manual Connection Test

Alternatively, run the connection test utility to verify your setup:

```bash
python test_connection.py
```

This will:
- List available ODBC drivers on your system
- Test your SQL Server connection
- Provide troubleshooting tips if connection fails

#### 6. Platform-Specific ODBC Driver Installation

**Windows:**
- Download [ODBC Driver 18 for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
- Or use ODBC Driver 17 for SQL Server

**macOS:**
```bash
# Using Homebrew
brew tap microsoft/mssql-release
brew install msodbcsql18 mssql-tools18
```

**Linux (Ubuntu/Debian):**
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
```

**Linux (RHEL/CentOS):**
```bash
sudo curl -o /etc/yum.repos.d/mssql-release.repo https://packages.microsoft.com/config/rhel/8/prod.repo
sudo yum remove unixODBC-utf16 unixODBC-utf16-devel
sudo ACCEPT_EULA=Y yum install -y msodbcsql18
```

#### 7. Troubleshooting

If you encounter connection issues:

1. **Check if SQL Server is running:** Open SQL Server Configuration Manager
2. **Verify TCP/IP is enabled:** SQL Server Network Configuration → Protocols
3. **Check firewall settings:** Ensure port 1433 is open
4. **Enable SQL Server Authentication:** If using username/password
5. **Use correct driver:** Run `test_connection.py` to see available drivers

Environment variables supported:

- `SQL_SERVER` - Server name or IP address
- `SQL_PORT` - Port number (default: 1433)  
- `SQL_USERNAME` - SQL Server username
- `SQL_PASSWORD` - SQL Server password
- `SQL_DATABASE` - Database name
- `SQL_DRIVER` - ODBC driver name
