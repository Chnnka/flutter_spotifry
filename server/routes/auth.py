import uuid
import bcrypt
from fastapi import APIRouter

from models.user import User
from pydantic_schemas.user_create import UserCreate

router=APIRouter()

@router.post('/signup')
def signup_user(user:UserCreate):
    #check if the user already exist in db
    user_db=db.query(User).filter(User.email == user.email).first()
    
    if user_db:
        raise HTTPException(400,'Email already taken')
      
    
    hashed_pw = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()),name=user.name,email=user.email, password=hashed_pw)
    #add user to ther db
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    
    return user_db