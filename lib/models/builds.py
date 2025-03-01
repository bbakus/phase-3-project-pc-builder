# build.py
from models.database import CONN, CURSOR
from models.components import Component

class Build:
    def __init__(self, name, description="", id=None):
        self.id = id
        self.name = name
        self.description = description
    
    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO builds (name, description)
                VALUES (?, ?)
            """
            CURSOR.execute(sql, (self.name, self.description))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE builds
                SET name = ?, description = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.description, self.id))
            CONN.commit()
        return self
    
    def get_components(self):
        """Get all components in this build"""
        sql = """
            SELECT c.* FROM components c
            JOIN build_components bc ON c.id = bc.component_id
            WHERE bc.build_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        
        components = []
        for row in CURSOR.fetchall():
            component = Component(row[1], row[2], row[3], row[0])
            components.append(component)
        return components
    
    def add_component(self, component_id):
        """Add a component to this build"""
        sql = """
            INSERT INTO build_components (build_id, component_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.id, component_id))
        CONN.commit()
        return self