
from models.database import CONN, CURSOR, create_tables
from seed_data import seed_data
from cli import main as run_cli

def setup_database():
    """Initialize and seed the database"""
    print("Setting up database...")
    
    # Create tables
    create_tables()
    
    # Check if components table is empty
    CURSOR.execute("SELECT COUNT(*) FROM components")
    count = CURSOR.fetchone()[0]
    
    if count == 0:
        print("No components found in database. Seeding data...")
        seed_data()
    else:
        print(f"Database already contains {count} components.")

def main():
    # Setup the database first
    setup_database()
    
    # Run the CLI
    run_cli()

if __name__ == "__main__":
    main()