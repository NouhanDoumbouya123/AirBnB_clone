from models.base_model import BaseModel


class User(BaseModel):
    """The User Object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
