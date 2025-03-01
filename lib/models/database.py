# database.py
import sqlite3

# Create connection to database
CONN = sqlite3.connect('pc_builder.db')
CURSOR = CONN.cursor()

# Add this to models/database.py

def create_tables():
    """Create all necessary tables if they don't exist"""
    
    print("Creating database tables...")
    
    # Create components table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS components (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    
    # Create builds table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS builds (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
    """)
    
    # Create build_components join table
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