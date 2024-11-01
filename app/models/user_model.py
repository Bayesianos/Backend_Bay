from pydantic import BaseModel

class User_Receive(BaseModel):
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