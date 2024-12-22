from pydantic import BaseModel
from uuid import UUID

class Userbase(BaseModel):
    id : str
    name : str
    email : str
    is_active : bool


   