from pydantic import BaseModel
from uuid import UUID

class BorrowRecordBase(BaseModel):
    id : str
    user_id : str
    book_id : str
    borrow_date : str
    return_date : str
