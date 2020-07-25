from pydantic import BaseModel, EmailStr

class UserBase():
    username: str
    email: str
    is_superuser: bool


class User(UserBase):
    id: int
    hashed_password: str
