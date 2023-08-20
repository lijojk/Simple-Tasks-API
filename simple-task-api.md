# Simple Task API #

This API allows you to CRUD Tasks.

The API is available at `http://127.0.0.1:8000'

## Endpoints ##


### List of Tasks ###

GET `/cr-task/task-list/`

Returns a list of tasks. Requires authentication.


### Get a single task ###

GET '/cr-task/task-details/id/'

Retrieve detailed information about a task. Requires authentication.


### Submit a task ###

POST `/cr-task/task-create/`

Allows you to submit a new task. Requires authentication.

The request body needs to be in JSON format and include the following properties:

```
{
  "title": "Complete Bootstrap Project",
  "due_date": "2023-08-31T23:59:59",
  "completed": "False",
  "description": "first postman task creation."
}
```

Example
```
POST /cr-task/task-create/
Authorization: Token <YOUR TOKEN>

{
  "title": "Complete Bootstrap Project",
  "due_date": "2023-08-31T23:59:59",
  "completed": "False",
  "description": "first postman task creation."
}
```


### Update a task ###

PATCH `/cr-task/task-update/id/`

Update an existing task. Requires authentication.

The request body needs to be in JSON format and allows you to update the following properties:


 Example
```
PATCH /cr-task/task-update/id/
Authorization: Token <YOUR TOKEN>

{
  "description": "postman task creation updated."
}
```

### Delete a task ###

DELETE `/cr-task/task-delete/id/`

Delete an existing task. Requires authentication.

The request body needs to be empty.

 Example
```
DELETE /cr-task/task-delete/id/
Authorization: Token <YOUR TOKEN>
```

## API Authentication ##

To submit or view a task, you need to register your API client.

POST `/cr-user/user-create/`

The request body needs to be in JSON format and include the following properties:

 - `username` - String
 - `password` - String

 Example

 ```
 {
    "username": "postman@gmail.com",
    "password": "@examplepassw"
}
 ```


## for API Token ##

POST `/cr-user/api-token/`

The request body needs to be in JSON format and include the following properties:

 - `username` - String
 - `password` - String

 Example

 ```
 {
    "username": "postman@gmail.com",
    "password": "@examplepassw"
}
 ```

The response body will contain the access token.

**Possible errors**

Status code 409 - "API client already registered." Try changing the values for `username` and `password` to something else.
