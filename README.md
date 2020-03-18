# Pet Exchanger Server
A server for pet exchanger app

## User

+ **Sign up**

POST http://petexchangerserver.herokuapp.com/signup

**Request Body Parameters**

Name | Data Type | Description
--- | ---- | ---
first_name | string | (Required) First name of the user
last_name | string | (Required) Second name of the user
email | string | (Required) Email of the user
password | string | (Required) At least 6 character

+ **Login**

POST http://petexchangerserver.herokuapp.com/login

**Request Body Parameters**

Name | Data Type | Description
--- | ---- | ---
email | string | (Required) Email of the user
password | string | (Required) At least 6 character

## Pet

+ **Get pet by id**

GET https://petexchangerserver.herokuapp.com/pet/{id}

Result - id, pet_name, favorite_food, favorite_toy, location, bio, image_url, user_id

+ **Add a new pet**

POST http://petexchangerserver.herokuapp.com/user/{id}/addpet

**Request Body Parameters**

Name | Data Type | Description
--- | ---- | ---
pet_name | string | (Required) Name of the pet
favorite_food | string | (Optional) Foods that the pet likes
favorite_toy | string | (Optional) Toys that the pet likes
location | string | (Optional) Location
bio | string | (Optional) Bio about the pet
image_url | string | (Optional) URL of the image

## Post

+ **Get all posts**

GET http://petexchangerserver.herokuapp.com/posts

Result - id, item_name, wants, description, location, tags, image_url, user_id

+ **Add a new pet**

POST http://petexchangerserver.herokuapp.com/user/{id}/addpost

**Request Body Parameters**

Name | Data Type | Description
--- | ---- | ---
item_name | string | (Required) Name of the product
wants | string | (Optional) What the user wants
description | string | (Optional) Description of the product
location | string | (Required) Location on where to meet
tags | string | (Optional) Tags about the product
image_url | string | (Optional) URL of the image

+ **Get all posts**

GET http://petexchangerserver.herokuapp.com/post/{id}

Result - id, item_name, wants, description, location, tags, image_url, user_id