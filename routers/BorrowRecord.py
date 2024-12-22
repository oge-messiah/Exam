from fastapi import APIRouter
from schemas.BorrowRecordSchema import BorrowRecordBase


router = APIRouter()

BorrowRecords = [
    BorrowRecordBase(id="BR001", user_id="JJ001", book_id="BG202", borrow_date="2022-01-01", return_date="2022-01-15"),
    BorrowRecordBase(id="BR002", user_id="MS120", book_id="BG605", borrow_date="2022-01-01", return_date="2022-01-01"),
    BorrowRecordBase(id="BR003", user_id="GU600", book_id="BG700", borrow_date="2022-01-05", return_date="2022-01-10"),
    BorrowRecordBase(id="BR004", user_id="VS511", book_id="BG707", borrow_date="2022-01-05", return_date="2022-01-10"),]



@router.get("/")
def borrow_records():
    return {"message": "Here are all the Borrow Records we have", "Data": BorrowRecords}

@router.get("/{user_id}")
def borrow_history(user_id: str):
    return [record for record in BorrowRecords if record.user_id == user_id]


            