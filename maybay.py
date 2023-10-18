from database import *
def get_maybay(MaMB):
    try:
        if MaMB == "":
            cursor.execute("SELECT * FROM maybay")
        else:
            cursor.execute("SELECT * FROM maybay WHERE MaMB = '"+MaMB+"'")
        result = cursor.fetchall()
        return  result
    except:
        return  "Error"
    
def insert_maybay(MaMB,Loai,TamBay):
    try:
        cursor.execute("INSERT INTO maybay(MaMB,Loai,TamBay) VALUES ('"+MaMB+"','"+Loai+"','"+TamBay+"')")
        db.commit()
        return "Insert success"
    except:
        return "Insert error"
    
def update_maybay(MaMB,Loai,TamBay):
    try:
        cursor.execute("UPDATE maybay SET Loai = '"+Loai+"',TamBay = '"+TamBay+"' WHERE MaMB = '"+MaMB+"'")
        db.commit()
        return "Update success"
    except:
        return "Update error"
    
def delete_maybay(MaMB):
    try:
        cursor.execute("DELETE FROM maybay WHERE MaMB = '"+MaMB+"'")
        db.commit()
        return "Delete success"
    except:
        return "Delete error"