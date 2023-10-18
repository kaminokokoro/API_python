from fastapi import FastAPI
from database import *
from chuyenbay import *
from chungnhan import *
from nhanvien import *
from maybay import *
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#API chuyenbay
@app.get("/chuyenbay")
async def chuyenbay(MaCB):
    return get_chuyenbay(MaCB)

@app.post("/chuyenbay")
async def chuyenbay(MaCB,GaDi,GaDen,GioDi,DoDai,GioDen,ChiPhi):
    return insert_chuyenbay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi)

@app.put("/chuyenbay")
async def chuyenbay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi):
    return update_chuyenbay(MaCB,GaDi,GaDen,DoDai,GioDi,GioDen,ChiPhi)

@app.delete("/chuyenbay")
async def chuyenbay(MaCB):
    return delete_chuyenbay(MaCB)

#API maybay
@app.get("/maybay")
async def maybay(MaMB):
    return get_maybay(MaMB)

@app.post("/maybay")
async def maybay(MaMB,Loai,TamBay):
    return insert_maybay(MaMB,Loai,TamBay)

@app.put("/maybay")
async def maybay(MaMB,Loai,TamBay):
    return update_maybay(MaMB,Loai,TamBay)

@app.delete("/maybay")
async def maybay(MaMB):
    return delete_maybay(MaMB)

#API nhanvien
@app.get("/nhanvien")
async def nhanvien(MaNV):
    return get_nhanvien(MaNV)

@app.post("/nhanvien")
async def nhanvien(MaNV,Ten,Luong):
    return insert_nhanvien(MaNV,Ten,Luong)

@app.put("/nhanvien")
async def nhanvien(MaNV,Ten,Luong):
    return update_nhanvien(MaNV,Ten,Luong)

@app.delete("/nhanvien")
async def nhanvien(MaNV):
    return delete_nhanvien(MaNV)

#API chungnhan
@app.get("/chungnhan")
async def chungnhan(MaNV):
    return get_chungnhan(MaNV)

@app.post("/chungnhan")
async def chungnhan(MaNV,MaMB):
    return insert_chungnhan(MaNV,MaMB)

@app.put("/chungnhan")
async def chungnhan(MaNV,MaMB):
    return update_chungnhan(MaNV,MaMB)

@app.delete("/chungnhan")
async def chungnhan(MaNV):
    return delete_chungnhan(MaNV)


