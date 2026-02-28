import sqlite3

def get_db():
    return sqlite3.connect("Item.db")

with get_db() as conn:
    curosr=conn.cursor()
    curosr.execute("CREATE TABLE IF NOT EXISTS Items(Id Int PRIMARY KEY, Name TEXT, Price INT,Quantity INT,Type TEXT)")

def get_item(id):
    with get_db() as conn:
        curosr= conn.cursor()
        curosr.execute("SELECT * FROM Items WHERE Id = ?",(id,))
        items=curosr.fetchone()
        if not items : 
            return None
        return {"id":items[0],"name":items[1],"price":items[2],"quantity": items[3],"type" : items[4]}
         

def get_item_with_type(type):
    with get_db() as conn:
        curosr=conn.cursor()
        curosr.execute("SELECT * FROM Items WHERE Type = ?",(type,))
        items=curosr.fetchall()
        if items :
            data=[]   
            for i in items:
                item = {
                "id" : i[0],
                "name" : i[1],
                "price" : i[2],
                "quantity" : i[3],
                "type" : i[4]
                }
                data.append(item)
            return data 
        else:
            return None

def get_all_items():
    with get_db() as conn:
        curosr=conn.cursor()
        curosr.execute("SELECT * FROM Items")
        items=curosr.fetchall()
        if items :
            data=[]   
            for i in items:
                item = {
                "id" : i[0],
                "name" : i[1],
                "price" : i[2],
                "quantity" : i[3],
                "type" : i[4]
                }
                data.append(item)
            return  data 
        else:
            return None

    
def add_item(id,name,price,quantity,type):
    with get_db() as conn:
        curosr=conn.cursor()
        curosr.execute("INSERT INTO Items VALUES(?,?,?,?,?)",(id,name,price,quantity,type))
        return {"Message" : "Added Successfully"}

def update_items(id,price=None,quantity=None):
    with get_db() as conn:
        curosr = conn.cursor()
        if id:
            if price != None and quantity !=None:
                curosr.execute("UPDATE Items SET Price = ? , Quantity = ? WHERE Id = ?",(price,quantity,id))
                row_count=curosr.rowcount()
                if row_count != 0:
                    return {"Message" : "Updated Successfully"}
                else : return None
            elif price ==None and quantity !=None:
                curosr.execute("UPDATE Items SET Quantity = ? WHERE Id = ?",(quantity,id))
                row_count=curosr.rowcount()
                if row_count != 0:
                    return {"Message" : "Updated Successfully"}
                else : return None
            elif price !=None and quantity == None:
                curosr.execute("UPDATE Items SET Price = ? WHERE Id = ?",(price,id))
                row_count=curosr.rowcount()
                if row_count != 0:
                    return {"Message" : "Updated Successfully"}
                else : return None
            elif price == None and quantity == None:
                row_count=curosr.rowcount()
                if row_count != 0:
                    return {"Message" : "Updated Successfully"}
                else : return None
        

def delete_items(id):
    with get_db() as conn:
        curosr = conn.cursor()
        curosr.execute("DELETE FROM Items WHERE Id = ?",(id,))
        row_count=curosr.rowcount()
        if row_count != 0:
            return {"Message" : "Deleted Successfully"}
        else : return None



