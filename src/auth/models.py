from sqlmodel import SQLModel
from datetime import datetime
import uuid

class User(SQLModel, table=True):
    __tablename__ = "users"
    uid : uuid.UUID
    username: str
    email : str
    first_name : str
    last_name : str
    is_verified: bool = False
    created_at: datetime
    updated_at: datetime
