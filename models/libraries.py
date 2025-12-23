from dataclasses import dataclass

@dataclass
class Library:
    id: int
    name: str
    location: str
    manager: str