from peewee import MySQLDatabase


database = MySQLDatabase(
    'encuestas',
    **{
        'charset': 'utf8mb4',
        'host': 'localhost',
        'port': 3306,
        'user': 'chile',
        'password': '1234',
    }
)
