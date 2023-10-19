from database import *
def get_nhanvien(MaNV):
    try:
        if MaNV=="":
            cursor.execute("SELECT * FROM nhanvien")
        else:
            cursor.execute("SELECT * FROM nhanvien WHERE MaNV = '"+MaNV+"'")
        data = cursor.fetchall()
        result = {'nhanvien':[]}
        for d in data:
            result["nhanvien"].append({
                "MaNV":d[0],
                "Ten":d[1],
                "Luong":d[2]
            })
        return  result
    except:
        return  Exception

def insert_nhanvien(MaNV,Ten,Luong):
    try:
        cursor.execute("INSERT INTO nhanvien(MaNV,Ten,Luong) VALUES ('"+MaNV+"','"+Ten+"','"+Luong+"')")
        db.commit()
        return "Insert success"
    except:
        return Exception

def update_nhanvien(MaNV,Ten,Luong):
    try:
        cursor.execute("UPDATE nhanvien SET Ten = '"+Ten+"',Luong = '"+Luong+"' WHERE MaNV = '"+MaNV+"'")
        db.commit()
        return "Update success"
    except:
        return Exception
    
def delete_nhanvien(MaNV):
    try:
        cursor.execute("DELETE FROM nhanvien WHERE MaNV = '"+MaNV+"'")
        db.commit()
        return "Delete success"
    except:
        return Exception

