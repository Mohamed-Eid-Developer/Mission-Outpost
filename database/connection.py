import pyodbc


def get_connection():
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=.;"
        "DATABASE=MissionOutpost;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return connection