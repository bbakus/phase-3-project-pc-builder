import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

# __init__.py
from models.database import CONN, CURSOR, create_tables
from models.components import Component
from models.builds import Build