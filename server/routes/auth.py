import uuid
import bcrypt
from fastapi import APIRouter, Depends, HTTPException

from database import get_db
from models.user import User
from pydantic_schemas.user_create import UserCreate
from pydantic_schemas.user_login import UserLogin
from sqlalchemy.orm import Session

router=APIRouter()

@router.post('/signup',status_code=201)
def signup_user(user:UserCreate, db: Session=Depends(get_db)):
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

@router.post('/login')
def login_user(user:UserLogin, db:Session=Depends(get_db)):
    #check if a user exist 
    user_db= db.query(User).filter(User.email==user.email).first()
    
    if not user_db:
        raise HTTPException(400,'User with this email does not exits')
    #password check
    is_match=bcrypt.checkpw(user.password.encode(),user_db.password)
    if not is_match:
        raise HTTPException(400,'Incorrect Password')
    return user_db
        