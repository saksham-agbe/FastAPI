from pydantic import BaseModel

class LibrariesSchema(BaseModel):
    id : int
    name : str
    location : str
    manager : str
    
    


