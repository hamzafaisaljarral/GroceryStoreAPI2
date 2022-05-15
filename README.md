
Getting Started:
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


Prerequisites:
Before you can run this project you need a install python first on your operating system. You can download python here and choose according to your operating system.
#note : right now my mongodb atlas connection is created feel free to change it from apps.py file


Installing
First, clone this project from github using git command or git gui application like fork.

$ https://github.com/hamzafaisaljarral/GroceryStoreAPI2.git

#note i am using python version python-3.9.6

Making environment for project to isolation python installing libraries for this project only.


**$ pip3 install virtualenv
- $ virtualenv venv <br>
- $ source venv/bin/activate<br>
Installing all libraries needed by this project using pip.**<br>

- **$ pip install -r requirements.txt**<br>
#note always Make a configuration file with name .env with the configrations of db link and key.<br>


Running the project.<br>
**FLASK_APP=wsgi.py FLASK_DEBUG=1 flask run**<br>


Testing<br>
To test api endpoint that has been created you can use curl utility. Before test, you must login first to get jwt token and using it in every request header you sent.<br>
or you can use postman i use post man i will give you instructions for that too.<br>

**Register API<br>
http://localhost:5000/user/register**<br>


<img width="1004" alt="Screen Shot 2022-05-15 at 7 38 55 AM" src="https://user-images.githubusercontent.com/39766112/168456143-394ad6fb-282e-41e1-9667-313b7b1c0a33.png">
<br>




#to create admin user<br>

<br>
**#paramters
{
    "email": "adm@gmail.com",
    "password": "admin123",
    "gender": "M",
    "phone_number": "97150894321",
    "role": {
        "admin": "True"
    }
}**
<br>


#to create client user<br>
#if you will not pass role it will set user by default to client<br>
**{
    "email": "kk@gmail.com",
    "password": "abc123",
    "gender": "M",
    "phone_number": "9715090000",
    "role": {
        "client": "True"
    }
}**
<br>



login API ENDPOINT<br>

**http://localhost:5000/user/login**<br>


<img width="1012" alt="Screen Shot 2022-05-15 at 7 40 55 AM" src="https://user-images.githubusercontent.com/39766112/168456181-52386dba-08db-4d41-b6fe-2c782de6709f.png">

<br>




#params<br>



**{
    "email": "admin2@gmail.com",
    "password": "admin123"
}
<br>


#this will return<br>
{
    "result": {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MjU4MDc2NywianRpIjoiMjQyNjM3MjEtYjRmZC00Nzc2LTgwY2EtMjMwMTUyYjE1ZjdkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjYyN2U2NTdlN2RjNzUyMDQ1NWVmODdmMyIsIm5iZiI6MTY1MjU4MDc2NywiZXhwIjoxNjUzMDEyNzY3fQ.loScx9d2Cw3prZzPnbdqCL4nJB_pUGysH3-piqJmHR8",
        "logged_in_as": "admin2@gmail.com",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MjU4MDc2NywianRpIjoiZGI2ZDUxMWUtMDljYS00M2Q5LWJlZGUtZjg0YzE2ZTNkYTA2IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiI2MjdlNjU3ZTdkYzc1MjA0NTVlZjg3ZjMiLCJuYmYiOjE2NTI1ODA3NjcsImV4cCI6MTY1NTE3Mjc2N30.-Q7zw7WZwNIlBke6HdovxLVjGuFSckKWAbAKPQL84DU"
    }
}**<br>





File upload API for Admin only<br>



**http://127.0.0.1:5000/product**<br>


<img width="1012" alt="Screen Shot 2022-05-15 at 7 42 46 AM" src="https://user-images.githubusercontent.com/39766112/168456223-043dccf7-74a4-4af1-bdcd-7a51017f3282.png">
<br>


<img width="1013" alt="Screen Shot 2022-05-15 at 7 43 41 AM" src="https://user-images.githubusercontent.com/39766112/168456234-c35e0fb8-1107-49bd-991a-ec2d516ec7a2.png">
<br>




<img width="1056" alt="Screen Shot 2022-05-15 at 7 44 25 AM" src="https://user-images.githubusercontent.com/39766112/168456262-e57dc8be-ea27-46d9-a588-c894b104da0a.png">


<br>





#you need to pass the token in header <br>
#you need to pass in params<br>
file = "your csv file"<br>



<br>
Add Product Review<br>
**http://127.0.0.1:5000/product/review**<br>


<img width="1014" alt="Screen Shot 2022-05-15 at 7 45 30 AM" src="https://user-images.githubusercontent.com/39766112/168456309-6e1e5190-a650-4dd4-9128-5e485d35bd76.png">
<br>


#need to pass token in header<br>
params
{
    "barcode": "34567890",
    "review": "new one"
}
<br>




**Search Product pass page and text field <br>

http://127.0.0.1:5000/product/search?page=0**
<br>


<img width="1017" alt="Screen Shot 2022-05-15 at 8 23 48 AM" src="https://user-images.githubusercontent.com/39766112/168457210-75d6a0c2-380e-449a-aa92-0be01f13d59a.png">


<br>

#need to pass token in header<br>
#params

{
    "text": "Product"
}

#result <br>
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
<br>



#Heroku Link to Test these API<br>

https://groceryflaskapi.herokuapp.com/user/register <br>

#parms <br>
[POST]<br>
{
   "email": "k3@gmail.com",
   "password": "admin123",
   "gender": "M",
   "phone_number": "971508953251",
   "role": {
      "client": "True"
   }
}
<br>
https://groceryflaskapi.herokuapp.com/user/login  <br>

#parms <br>
[POST] <br>

{
   "email": "admin2@gmail.com",
   "password": "admin123"
}

-https://groceryflaskapi.herokuapp.com/product<br>
[POST]<br>

#note only admin can upload csv file

params<br>

Token = 'access_token'

-https://groceryflaskapi.herokuapp.com/product/review <br>

[POST]

params<br>

{
   "barcode": "34567890",
   "review": "testing"
}
<br>
-https://groceryflaskapi.herokuapp.com/product/search?page=0<br>

[POST]

params<br>

{
   "text": "Product"
}






