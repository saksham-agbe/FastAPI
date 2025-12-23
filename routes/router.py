from fastapi import APIRouter, Depends
from db import get_db
from schemas import LibrariesSchema, BooksSchema
from schemas.libraries_schema import LibrariesSchema

router = APIRouter()

""""
Endpoints must use PascalCase naming convention
For example: /Healthcheck, /GetUser, /CreateItem etc.
"""

@router.get("/HealthCheck")
async def healthcheck():
    return {
        "success": True,
        "message": "API service is healthy"
    }

@router.get("/Libraries")
async def get_all_libraries(db = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT id, name, location, manager
        FROM libraries;
        """
    )
    libraries = cursor.fetchall()
    cursor.close()
    return {
        "success": True,
        "data": [
            {
                "id": library[0],
                "name": library[1],
                "location": library[2],
                "manager": library[3]
            }
            for library in libraries
        ]
    }

@router.get("/Books/{library_id}")
async def get_all_books_from_library(library_id: int, db = Depends(get_db)):
    cursor = db.cursor()
    query = """
        SELECT
            b.id,
            b.name,
            b.author,
            b.rating
        FROM books b
        INNER JOIN book_library_mapping blm
            ON b.id = blm.book_id
        WHERE blm.library_id = %s;
    """
    cursor.execute(query, (library_id,))
    books = cursor.fetchall()
    cursor.close()

    data = [
        {
            "id": book[0],
            "name": book[1],
            "author": book[2],
            "rating": book[3]
        }
        for book in books
    ]

    return {
        "success": True,
        "data": data
    }
    
    