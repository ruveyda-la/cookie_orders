from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash

class Order:

    db="cookie_orders"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.number = data['number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_order(order):
        
        is_valid = True
        if len(order['name'])<1:
            flash("Customer name is required.")
            is_valid = False
        if len(order['name'])<2:
            flash("Please enter a valid name")
            is_valid = False
        if len(order['cookie_type'])<1:
            flash("Cookie type is required.")
            is_valid = False
        if len(order['cookie_type'])<2:
            flash("Please enter a valid cookie type")
            is_valid = False
        if int(order['number'])<1:
            flash("Please enter a valid number")
            is_valid = False
        
        return is_valid

    @classmethod
    def save(cls,data):
        query = """INSERT INTO orders (name, cookie_type, number)
                VALUES (%(name)s,%(cookie_type)s,%(number)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
    
        results = connectToMySQL(cls.db).query_db(query)
        
        orders = []
    
        for result in results:
            orders.append( cls(result) )
        return orders

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM orders WHERE id= %(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return result[0]

    @classmethod
    def change(cls,data):
        query="""UPDATE orders SET name=%(name)s, cookie_type=%(cookie_type)s,
                number=%(number)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result
