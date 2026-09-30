from database.connection import get_connection


try:
    connection = get_connection()

    print("✅ Connected to SQL Server successfully!")

    connection.close()

    print("Connection closed")

except Exception as error:
    print("❌ Connection failed:")
    print(error)