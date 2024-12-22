from pydantic import BaseModel
from uuid import UUID

class BookBase(BaseModel):
    title: str
    author: str
    id :str
    is_available : bool



     