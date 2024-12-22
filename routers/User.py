from fastapi import APIRouter
from schemas.UserSchema import Userbase


router = APIRouter()

Users = [
    Userbase(id="JJ001", name="Jofin James", email="jofinjames@gmail.com", is_active=True),
    Userbase(id="MS120", name="Megan Sampson", email="megan4u@gmail.com", is_active=False),
    Userbase(id="GU600", name="Grace Unuane", email="graceunuane@gmail.com", is_active=True),
    Userbase(id="VS511", name="Vemula Sai", email="vemulasai@gmail.com", is_active=False),
]


@router.get("/")
def get_all_users():
    return Users


@router.get ("/{user_id}")
def get_user_by_id(user_id: str):
    return next((user for user in Users if user.id == user_id), None)

@router.post("/")
def create_user(user: Userbase):
    Users.append(user)
    return {"message": "User created successfully", "user": user}
              
@router.patch("/{user_id}")
def update_user(user_id: str, user: Userbase):
    user_to_update = next((user for user in Users if user.id == user_id), None)
    if user_to_update:
        user_to_update.name = user.name
        user_to_update.email = user.email
        return {"message": "User updated successfully", "user": user_to_update}
    return None


@router.delete("/{user_id}")
def delete_user(user_id:str):
    user_to_delete = next((user for user in Users if user.id == user_id), None)
    if user_to_delete:
        Users.remove(user_to_delete)
        return {"message": "User deleted successfully"}
    return None





        
                 
    

                       
    




