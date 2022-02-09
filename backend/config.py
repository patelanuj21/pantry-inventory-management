import os

DB_HOST = os.environ.get('DB_HOST', default='localhost')
DB_NAME = os.environ.get('DB_NAME', default='pantry')
DB_USER = os.environ.get('DB_USERNAME', default='root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', default='')
DB_PORT = os.environ.get('DB_PORT', default='3306')