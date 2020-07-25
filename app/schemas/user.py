from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: str
    is_superuser: bool

    class Config:
        orm_mode = True


class User(UserBase):
    pass

class UserCreate(UserBase):
    password : str

    class Config:
        orm_mode = True