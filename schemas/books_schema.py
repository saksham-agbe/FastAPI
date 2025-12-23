from pydantic import BaseModel

class BooksSchema(BaseModel):
    id : int
    name : str
    author : str
    rating : int
    
