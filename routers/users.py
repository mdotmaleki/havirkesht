from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas, models
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from core.security import ALGORITHM, SECRET_KEY, get_password_hash, verify_password
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from core.security import verify_password, get_password_hash, create_access_token
from models import UserModel
from schemas import UserCreate
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from core.security import verify_password, create_access_token

router = APIRouter(
    prefix="/users",
    tags=["Roles & Users"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = crud.get_user_by_username(db, username)
    if user is None:
        raise credentials_exception

    return user



def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()




@router.post("/roles/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.create_role(db=db, role=role)

@router.get("/roles/", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
               current_user: schemas.User = Depends(get_current_user)):
    return crud.get_roles(db, skip=skip, limit=limit)

@router.get("/roles/{role_id}", response_model=schemas.Role)
def read_role(role_id: int, db: Session = Depends(get_db),
              current_user: schemas.User = Depends(get_current_user)):
    db_role = crud.get_role(db, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.put("/roles/{role_id}", response_model=schemas.Role)
def update_role(role_id: int, role: schemas.RoleCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    db_role = crud.update_role(db, role_id, role)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.delete("/roles/{role_id}", response_model=schemas.Role)
def delete_role(role_id: int, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    db_role = crud.delete_role(db, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db),
              current_user: schemas.User = Depends(get_current_user)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    db_user = crud.update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    db_user = crud.delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": user.username})

    return {"access_token": token, "token_type": "bearer"}








