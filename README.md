# API_python
## Overview
This API provides access and manipulation to the aviation database.
## API COLLECTION POSTMAN
[AVIATION API](https://github.com/kaminokokoro/API_python/blob/master/AVIATION%20API.postman_collection.json)
## API documentation
[API documentation](https://documenter.getpostman.com/view/30529489/2s9YRB1BZq)
## Aviation Database
[Aviation database](https://github.com/kaminokokoro/API_python/tree/master/database_to_import)
### This database includes:
- `chuyenbay` : this table stores data about information of flight
- `maybay` : this table stores data about the plane
- `nhanvien` : this table stores data about the staff
- `chungnhan` : this table stores data about the certification of staff
## how to run code
- step 1: Dowload code [here](https://github.com/kaminokokoro/API_python/releases/tag/v1.0.0) or clone this repo by git:
```
git clone https://github.com/kaminokokoro/API_python.git
```
- step 2: Import the database by use a folder named [database_to_import](https://github.com/kaminokokoro/API_python/tree/master/database_to_import)
- step 3: Import [APIHangKhong.postman_collection.json](https://github.com/kaminokokoro/API_python/blob/master/APIHangKhong.postman_collection.json) to your Postman
- step 4: Navigate to the project root directory where the `main.py` is located and run this command: 
```
python -m uvicorn main:app --reload
```
- step 5: Run the test in your Postman

  
