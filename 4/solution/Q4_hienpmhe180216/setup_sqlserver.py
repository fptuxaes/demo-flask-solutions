#!/usr/bin/env python3
"""
Cross-Platform SQL Server Setup Helper
Supports Windows, macOS, and Linux

This script helps set up SQL Server connection for the Flask app
"""

import os
import sys
import platform
import shutil
import subprocess
from pathlib import Path

def print_colored(text, color="white"):
    """Print colored text (cross-platform)"""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m", 
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    
    if platform.system() == "Windows":
        # For Windows, try to enable ANSI colors
        try:
            import colorama
            colorama.init()
            print(f"{colors.get(color, '')}{text}{colors['reset']}")
        except ImportError:
            print(text)  # Fall back to plain text
    else:
        print(f"{colors.get(color, '')}{text}{colors['reset']}")

def check_python_environment():
    """Check if required Python packages are installed"""
    print_colored("Checking Python environment...", "yellow")
    
    required_packages = ["pyodbc", "flask", "dotenv"]
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print_colored(f"✅ {package} is installed", "green")
        except ImportError:
            print_colored(f"❌ {package} is not installed", "red")
            missing_packages.append(package)
    
    if missing_packages:
        print_colored(f"\nTo install missing packages, run:", "yellow")
        print_colored(f"pip install {' '.join(missing_packages)}", "cyan")
        return False
    
    return True

def list_odbc_drivers():
    """List available ODBC drivers"""
    print_colored("\nAvailable ODBC Drivers:", "yellow")
    try:
        import pyodbc
        drivers = pyodbc.drivers()
        if drivers:
            for driver in drivers:
                print_colored(f"  - {driver}", "white")
        else:
            print_colored("  No ODBC drivers found", "red")
            print_platform_specific_driver_info()
    except ImportError:
        print_colored("  Cannot list drivers (pyodbc not installed)", "red")

def print_platform_specific_driver_info():
    """Print platform-specific information about installing ODBC drivers"""
    system = platform.system()
    
    if system == "Windows":
        print_colored("\nWindows ODBC Driver Installation:", "yellow")
        print_colored("1. Download Microsoft ODBC Driver 18 for SQL Server", "cyan")
        print_colored("2. Or use ODBC Driver 17 for SQL Server", "cyan")
        print_colored("3. Download from: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server", "cyan")
    
    elif system == "Darwin":  # macOS
        print_colored("\nmacOS ODBC Driver Installation:", "yellow")
        print_colored("1. Install using Homebrew:", "cyan")
        print_colored("   brew tap microsoft/mssql-release", "cyan")
        print_colored("   brew install msodbcsql18 mssql-tools18", "cyan")
        print_colored("2. Or download from Microsoft website", "cyan")
    
    elif system == "Linux":
        print_colored("\nLinux ODBC Driver Installation:", "yellow")
        print_colored("Ubuntu/Debian:", "cyan")
        print_colored("  curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -", "cyan")
        print_colored("  curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list", "cyan")
        print_colored("  apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18", "cyan")
        print_colored("\nRHEL/CentOS:", "cyan")
        print_colored("  curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo", "cyan")
        print_colored("  yum remove unixODBC-utf16 unixODBC-utf16-devel", "cyan")
        print_colored("  ACCEPT_EULA=Y yum install -y msodbcsql18", "cyan")

def setup_env_file():
    """Setup .env file from template"""
    print_colored("\nSetting up environment file...", "yellow")
    
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if env_file.exists():
        print_colored("✅ .env file already exists", "green")
        return True
    
    if env_example.exists():
        try:
            shutil.copy2(env_example, env_file)
            print_colored("✅ Created .env from .env.example", "green")
            print_colored("Please edit .env file with your SQL Server details", "cyan")
            return True
        except Exception as e:
            print_colored(f"❌ Failed to create .env file: {e}", "red")
            return False
    else:
        print_colored("❌ .env.example not found", "red")
        return False

def test_connection():
    """Test SQL Server connection"""
    print_colored("\nTesting SQL Server connectivity...", "yellow")
    
    try:
        result = subprocess.run([sys.executable, "test_connection.py"], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(result.stdout)
        else:
            print_colored("Connection test failed:", "red")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print_colored("❌ Connection test timed out", "red")
    except FileNotFoundError:
        print_colored("❌ test_connection.py not found", "red")
    except Exception as e:
        print_colored(f"❌ Error running connection test: {e}", "red")

def main():
    """Main setup function"""
    print_colored("SQL Server Setup Helper (Cross-Platform)", "green")
    print_colored("=" * 45, "green")
    print_colored(f"Platform: {platform.system()} {platform.release()}", "white")
    print_colored(f"Python: {sys.version.split()[0]}", "white")
    
    # Check Python environment
    if not check_python_environment():
        print_colored("\n⚠️  Please install missing packages before continuing", "yellow")
        return
    
    # List ODBC drivers
    list_odbc_drivers()
    
    # Setup .env file
    setup_env_file()
    
    # Test connection
    test_connection()
    
    # Final instructions
    print_colored("\nSetup complete! Next steps:", "green")
    print_colored("1. Edit .env file with your SQL Server details", "cyan")
    print_colored("2. Ensure SQL Server is running and accessible", "cyan")
    print_colored("3. Install ODBC drivers if needed (see info above)", "cyan")
    print_colored("4. Run: python app.py", "cyan")

if __name__ == "__main__":
    main()