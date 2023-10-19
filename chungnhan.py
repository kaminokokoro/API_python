from database import *

def get_chungnhan(MaNV):
    try:
        if MaNV=="":
            cursor.execute("SELECT * FROM chungnhan")
        else:
            cursor.execute("SELECT * FROM chungnhan WHERE MaNV = '"+MaNV+"'")
        data = cursor.fetchall()
        result = {'chungnhan':[]}
        for d in data:
            result["chungnhan"].append({
                "MaNV":d[0],
                "MaMB":d[1]
            })
        return  result
    except Exception as e:
        return e

def insert_chungnhan(MaNV,MaMB):
    try:
        cursor.execute("INSERT INTO chungnhan(MaNV,MaMB) VALUES ('"+MaNV+"','"+MaMB+"')")
        db.commit()
        return "Insert success"
    except:
        return Exception

def update_chungnhan(MaNV,MaMB):
    try:
        cursor.execute("UPDATE chungnhan SET MaMB = '"+MaMB+"' WHERE MaNV = '"+MaNV+"'")
        db.commit()
        return "Update success"
    except:
        return Exception

def delete_chungnhan(MaNV):
    try:
        cursor.execute("DELETE FROM chungnhan WHERE MaNV = '"+MaNV+"'")
        db.commit()
        return "Delete success"
    except:
        return Exception