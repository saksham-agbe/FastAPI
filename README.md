## About:

- Create API endpoints using raw Python with database connectivity
- Application to be deployed using AWS Lambda using Localstack

## To Dos:

- Create a connection with PostgreSQL/MySQL (Pool Connection)
- Create a Library Management System where you will create some APIs (Application Programable Interface) to interact with the system
- Learn about APIs as a concept and REST
- Learn about ORMs
- Learn Basics of FastAPI
- Create Table Models in models directory

## List of Tables

1. libraries (Table to store all the libraries)

````json
id
name
location
manager
created_at
updated_at
````

2. books (Table to store all the books)

````json
id
name
author
rating
created_at
updated_at
````

3. book_library_mapping (Table to store which book belongs to which library)

````json
id
library_id
book_id
created_at
updated_at
````

#### Notes :

- One book can be mapped to multiple libraries

## List of APIs:

1. Get a list of all the Libraries -
   **{base_url}/api/libraries** (GET)

#### Expected Response

````json
{
    "success" : true,
    "data" : [
        {
            "id" : 1,
            "name": "Learn Well Library",
            "location": "Sector 66, Badshahpur",
            "manager": "Prem Singh"
        },
        {
            "id" : 2,
            "name": "Achievers Library",
            "location": "MG Road, Gurugram",
            "manager": "Ram Shankar Nikumbh"
        }
    ]
}
````

2. Get all books in a library -
   **{base_url}/api/books/{library_id}** (GET)

#### Expected Response

````json
{
    "success" : true,
    "data" : [
        {
            "id": "1",
            "name": "The Theory of Everything",
            "author": "Stephan J Hawkings",
            "rating": "10",
        },
        {
            "id": "2",
            "name": "The Wings of Fire",
            "author": "Dr. APJ Abdul Kalam",
            "rating": "10",
        }
    ]
}
````

## Core Expectations:

- Database connectivity must be flawless, you can take help from any LLM regarding the queries to be run in order to achieve the database operations.
- Response structure across each api must be uniform and consistent in nature.

## KPIs:

TBD

## About FastAPI

#### Start the server

uvicorn main:app --reload (Runs the server on default port i.e 8000)

#### To use a custom port

uvicorn main:app --port 9000 --reload
echo "# test auto trigger"
sssh