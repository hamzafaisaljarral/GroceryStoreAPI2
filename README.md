
Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Before you can run this project you need a install python first on your operating system. You can download python here and choose according to your operating system.
#note : right now my mongodb atlas connection is created feel free to change it from apps.py file

Installing
First, clone this project from github using git command or git gui application like fork.

$ https://github.com/hamzafaisaljarral/GroceryStoreAPI2.git
Making environment for project to isolation python installing libraries for this project only.

$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
Installing all libraries needed by this project using pip.

$ pip install -r requirements.txt
#note always Make a configuration file with name .env with the configrations of db link and key.


Running the project.
FLASK_APP=wsgi.py FLASK_DEBUG=1 flask run

Testing
To test api endpoint that has been created you can use curl utility. Before test, you must login first to get jwt token and using it in every request header you sent.
or you can use postman i use post man i will give you instructions for that too.

Register API
http://localhost:5000/user/register

#to create admin user
#paramters
{
    "email": "adm@gmail.com",
    "password": "admin123",
    "gender": "M",
    "phone_number": "97150894321",
    "role": {
        "admin": "True"
    }
}

#to create client user
#if you will not pass role it will set user by default to client
{
    "email": "kk@gmail.com",
    "password": "abc123",
    "gender": "M",
    "phone_number": "9715090000",
    "role": {
        "client": "True"
    }
}


login API ENDPOINT

http://localhost:5000/user/login

#params

{
    "email": "admin2@gmail.com",
    "password": "admin123"
}


#this will return
{
    "result": {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MjU4MDc2NywianRpIjoiMjQyNjM3MjEtYjRmZC00Nzc2LTgwY2EtMjMwMTUyYjE1ZjdkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjYyN2U2NTdlN2RjNzUyMDQ1NWVmODdmMyIsIm5iZiI6MTY1MjU4MDc2NywiZXhwIjoxNjUzMDEyNzY3fQ.loScx9d2Cw3prZzPnbdqCL4nJB_pUGysH3-piqJmHR8",
        "logged_in_as": "admin2@gmail.com",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MjU4MDc2NywianRpIjoiZGI2ZDUxMWUtMDljYS00M2Q5LWJlZGUtZjg0YzE2ZTNkYTA2IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiI2MjdlNjU3ZTdkYzc1MjA0NTVlZjg3ZjMiLCJuYmYiOjE2NTI1ODA3NjcsImV4cCI6MTY1NTE3Mjc2N30.-Q7zw7WZwNIlBke6HdovxLVjGuFSckKWAbAKPQL84DU"
    }
}

File upload API for Admin only

http://127.0.0.1:5000/product

#you need to pass the token in header 
#you need to pass in params
file = "your csv file"



Add Product Review
http://127.0.0.1:5000/product/review

#need to pass token in header
params
{
    "barcode": "34567890",
    "review": "new one"
}

Search Product pass page and text field 

http://127.0.0.1:5000/product/search?page=0

#need to pass token in header
#params

{
    "text": "Product"
}

#result
{
    "totalCount": 10,
    "Products": [
        {
            "name": "Product 1",
            "description": "This is sample description",
            "price": 200,
            "available": true,
            "review": [
                {
                    "name": "admin2@gmail.com",
                    "review": "new one"
                }
            ]
        },
        {
            "name": "Product 2",
            "description": "This is sample description",
            "price": 100,
            "available": true,
            "review": []
        },
        {
            "name": "Product 3",
            "description": "This is sample description",
            "price": 150,
            "available": true,
            "review": []
        },
        {
            "name": "Product 4",
            "description": "This is sample description",
            "price": 250,
            "available": true,
            "review": []
        },
        {
            "name": "Product 5",
            "description": "This is sample description",
            "price": 300,
            "available": true,
            "review": []
        },
        {
            "name": "Product 6",
            "description": "This is sample description",
            "price": 350,
            "available": true,
            "review": []
        },
        {
            "name": "Product 7",
            "description": "This is sample description",
            "price": 180,
            "available": true,
            "review": []
        },
        {
            "name": "Product 8",
            "description": "This is sample description",
            "price": 120,
            "available": true,
            "review": []
        },
        {
            "name": "Product 9",
            "description": "This is sample description",
            "price": 110,
            "available": true,
            "review": []
        },
        {
            "name": "Product 10",
            "description": "This is sample description",
            "price": 90,
            "available": true,
            "review": []
        }
    ]
}

#Heroku Link to Test these API

