# DjangoRestApis
This project consists of follwing APIs:

1)**Signup API**: : is used to add a user 
  Endpoint: /signup 
  Mandatory Fields: email, first_name, last_name, phone_number, password
  Sample Request: 
  {
    "email":"your_email@example.com", 
    "first_name":"Your_First_Name",
    "last_name":"Your_Last_Name",
    "phone_number":"2123456789",
    "password":"****"
  }

Sample Response:
  Status Code : 201 Created
  {"message":"Signed Up Successfully"}

2)**Login API**: is used to login a user

Endpoint: /login
Mandatory Fields: email, password
  Sample Request: 
  {
	"email":"your_email@example.com",
	"password":"****"
  }

  Sample Response:
  Status Code : 200 OK
  {
    "refresh": "refresh_token",
    "access": "access_token"
  }

3)**Add User Details API**: Is used to add details for a particular user

Endpoint: /addUserDetails
Request Header: Authorization: Bearer <access_token>
Mandatory Fields: age, dob, profession, address, hobby
  Sample Request: 
  {
	"age":25,
	"dob":"1997-08-05",
	"profession":"Cab Driver",
	"address":"Los Angeles, CA",
	"hobby":"Sleeping"
  }

  Sample Response:
  Status Code : 200 OK
  { "message":"Added User Details Successfully" }
  
 4)**Update User Details API**: Is used to update details for a particular user

 Endpoint: /updateUserDetails
 Request Header: Authorization: Bearer <access_token>
 Optional Fields: age, dob, profession, address, hobby
 Sample Request: 
  {
	"age":24,
	"dob":"1999-07-12",
	"profession":"Accountant",
	"address":"San Diego, CA",
	"hobby":"Swimming"
  }

  Sample Response:
  Status Code : 200 OK
  {"message":"Updated User Details Successfully"}

5)**Delete User**: Is used to delete a particular user from the system & hence delete it's corresponding details
Endpoint: /deleteUsers
Request Header: Authorization: Bearer <access_token>
Status Code : 200 OK
{"message":"Deleted Successfully"}
