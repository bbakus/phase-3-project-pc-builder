
import sqlite3


CONN = sqlite3.connect('pc_builder.db')
CURSOR = CONN.cursor()



def create_tables():
    
    
    print("Creating database tables...")
    
    
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS components (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    
    
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS builds (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
    """)
    
    
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS build_components (
            id INTEGER PRIMARY KEY,
            build_id INTEGER,
            component_id INTEGER,
            FOREIGN KEY (build_id) REFERENCES builds (id),
            FOREIGN KEY (component_id) REFERENCES components (id)
        )
    """)
    
    CONN.commit()
    print("Tables created successfully!")