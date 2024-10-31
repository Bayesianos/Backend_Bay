# import uuid

from pydantic import BaseModel
from .enum_user import Enum_PNO

class User_Receive(BaseModel):#não precisa de construtor, pq o BaseModel já tem um proprio construtor
  idade: int
  genero: bool #true - homem / false - mulher
  moradia: str
  credito: float
  cc: Enum_PNO
  poupanca: Enum_PNO
  duracao: float
  proposito: str

class User_Send(BaseModel):
  emprestimo_valido: bool # true - 70% a 100% / false - 69% a 0%