from fastapi import FastAPI

from routers.User import router as UserRouter
from routers.Book import router as BookRouter
from routers.BorrowRecord import router as BorrowRecordRouter




app = FastAPI()


app.include_router(UserRouter, prefix="/users")
app.include_router(BookRouter, prefix="/books") 
app.include_router(BorrowRecordRouter, prefix="/borrowrecords")






@app.get("/")
def Home():
    return "Welcome to my API"


