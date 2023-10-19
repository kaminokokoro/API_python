from database import *

    
def get_chuyenbay(MaCB):
    try:
        if MaCB == "":
            cursor.execute("SELECT * FROM chuyenbay")
        else:
            cursor.execute("SELECT * FROM chuyenbay WHERE MaCB = '"+MaCB+"'")
        data = cursor.fetchall()
        result ={'chuyenbay':[]}
        for d in data:
            result['chuyenbay'].append({
                "MaCB":d[0],
                "GaDi":d[1],
                "GaDen":d[2],
                "DoDai":d[3],
                "GioDi":d[4],
                "GioDen":d[5],
                "ChiPhi":d[6]
            })
        return  result
    except:
        return  Exception
    
def insert_chuyenbay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi):
    try:
        cursor.execute("INSERT INTO chuyenbay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi) VALUES ('"+MaCB+"','"+GaDi+"','"+GaDen+"','"+DoDai+"','"+GioDi+"','"+GioDen+"','"+ChiPhi+"')")
        db.commit()
        return "Insert success"
    except:
        return Exception

def update_chuyenbay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi):
    try:
        cursor.execute("UPDATE chuyenbay SET GaDi = '"+GaDi+"',GaDen = '"+GaDen+"',DoDai = '"+DoDai+"',GioDi = '"+GioDi+"',GioDen = '"+GioDen+"',ChiPhi = '"+ChiPhi+"' WHERE MaCB = '"+MaCB+"'")
        db.commit()
        return "Update success"
    except:
        return Exception
    
def delete_chuyenbay(MaCB):
    try:
        cursor.execute("DELETE FROM chuyenbay WHERE MaCB = '"+MaCB+"'")
        db.commit()
        return "Delete success"
    except:
        return Exception