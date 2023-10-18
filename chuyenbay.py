from database import *

    
def get_chuyenbay(MaCB):
    try:
        if MaCB == "":
            cursor.execute("SELECT * FROM chuyenbay")
        else:
            cursor.execute("SELECT * FROM chuyenbay WHERE MaCB = '"+MaCB+"'")
        result = cursor.fetchall()
        return  result
    except:
        return  "Error"
    
def insert_chuyenbay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi):
    try:
        cursor.execute("INSERT INTO chuyenbay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi) VALUES ('"+MaCB+"','"+GaDi+"','"+GaDen+"','"+DoDai+"','"+GioDi+"','"+GioDen+"','"+ChiPhi+"')")
        db.commit()
        return "Insert success"
    except:
        return "Insert error"

def update_chuyenbay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi):
    try:
        cursor.execute("UPDATE chuyenbay SET GaDi = '"+GaDi+"',GaDen = '"+GaDen+"',DoDai = '"+DoDai+"',GioDi = '"+GioDi+"',GioDen = '"+GioDen+"',ChiPhi = '"+ChiPhi+"' WHERE MaCB = '"+MaCB+"'")
        db.commit()
        return "Update success"
    except:
        return "Update error"
    
def delete_chuyenbay(MaCB):
    try:
        cursor.execute("DELETE FROM chuyenbay WHERE MaCB = '"+MaCB+"'")
        db.commit()
        return "Delete success"
    except:
        return "Delete error"