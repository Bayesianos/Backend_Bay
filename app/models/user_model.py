from pydantic import BaseModel
from sqlmodel import Field

class User(BaseModel):#não precisa de construtor, pq o BaseModel já tem um proprio construtor
  id: str = Field(default=None, primary_key=True)
  name: str = Field(index=True)