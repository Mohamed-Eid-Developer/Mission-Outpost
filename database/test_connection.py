from connection import get_connection


try:
    connection = get_connection()

    print("✅ Connected to SQL Server successfully!")

    connection.close()

except Exception as error:
    print("❌ Connection failed:")
    print(error)