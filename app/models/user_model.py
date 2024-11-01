# import uuid

from pydantic import BaseModel
from .enum_user import Enum_PNO

class User_Receive(BaseModel):#não precisa de construtor, pq o BaseModel já tem um proprio construtor
  age: int 
  sex: int 
  job: int 
  housing: int 
  saving_accounts: int
  checking_account: int 
  credit_amount: int 
  duration: int 
  purpose: int 

class User_Send(BaseModel):
  emprestimo_valido: bool # true - 70% a 100% / false - 69% a 0%