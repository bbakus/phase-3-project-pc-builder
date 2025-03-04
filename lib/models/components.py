
from models.database import CONN, CURSOR

class Component:

    all = []


    def __init__(self, name, category, price, id=None):
        self.id = id
        self._name = name
        self._category = category
        self._price = price


    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price_value):
        if not isinstance(price_value, float):
            return
        self._price = price_value

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category_value):
        if not isinstance(category_value, str):
            return
        self._category = category_value

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_value):
        if not isinstance(name_value, str):
            return
        self._name = name_value


 
    
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
        Component.all.append(self)
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