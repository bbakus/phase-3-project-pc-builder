# component.py
from models.database import CONN, CURSOR

class Component:
    def __init__(self, name, category, price, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
    
    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO components (name, category, price)
                VALUES (?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.category, self.price))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE components
                SET name = ?, category = ?, price = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.category, self.price, self.id))
            CONN.commit()
        return self
    
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM components WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        
        if row:
            return cls(row[1], row[2], row[3], row[0])
        return None
    
    def delete(self):
        sql = "DELETE FROM components WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None
        return self